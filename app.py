from logging import error
from flask import Flask, redirect, url_for, request, render_template, jsonify
import os
from flask.wrappers import Request
from pymongo import MongoClient
from dotenv import load_dotenv
import datetime
import random
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import translate as trans

client = MongoClient("mongodb+srv://user:Mypassword123@cluster0.w2btl.mongodb.net/translate_db?retryWrites=true&w=majority")
# client = MongoClient("mongodb://user:Mypassword123@cluster0-shard-00-00.w2btl.mongodb.net:27017,cluster0-shard-00-01.w2btl.mongodb.net:27017,cluster0-shard-00-02.w2btl.mongodb.net:27017/translate_db?ssl=true&replicaSet=atlas-laukbb-shard-0&authSource=admin&retryWrites=true&w=majority")

# "mongodb+srv://<username>:<password>@cluster0.w2btl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# "mongodb://user:Mypassword123@cluster0-shard-00-00.w2btl.mongodb.net:27017,cluster0-shard-00-01.w2btl.mongodb.net:27017,cluster0-shard-00-02.w2btl.mongodb.net:27017/translate_db?ssl=true&replicaSet=atlas-laukbb-shard-0&authSource=admin&retryWrites=true&w=majority"
db = client.get_database("translate_db")
Translate = db.main

load_dotenv()

app = Flask(__name__)

input_sentences = []
file_name = "static/words/english-only.txt"

username = ""


@app.route("/")
def index():
    val = next_text()
    print(val, request.remote_addr, "---------")
    return render_template("index.html", text=val, ipAdress=request.remote_addr)


@app.route("/about")
def about():
    val = next_text()
    print(val, "---------")
    return render_template("pages/about.html", text=val)


@app.route("/contact")
def contact():
    val = next_text()
    print(val, "---------")
    return render_template("pages/contact.html", text=val)


@app.route("/try")
def try_model():
    return render_template("pages/try.html")


@app.route("/translated", methods=['GET'])
def translated():
    val = next_text()
    count_translate = Translate.count_documents(
        {"date": datetime.now().strftime("%d-%m-%Y")})
    trans = list(Translate.find(
        {"date": datetime.now().strftime("%d-%m-%Y")}, {"_id": 0}))
    print(val, "---------")
    return render_template("pages/translated.html", text=val, translates=trans, count=count_translate)


@app.route("/specific", methods=['GET', 'POST'])
def specific():
    if request.method == 'POST':
        date = str(request.form['date'])
        print(date, "******FFFFFF**")

        date_split = date.split("-")
        print(date_split, "******DDDDDDDDD**")

        date = str(date_split[2]+"-"+date_split[1]+"-"+date_split[0])
        count_translate = Translate.count_documents(
            {"date": date})
        trans = list(Translate.find(
            {"date": date}, {"_id": 0}))
        return render_template("pages/specific.html",  translates=trans, count=count_translate, date=date)
    else:
        date = datetime.now().strftime("%d-%m-%Y")
        count_translate = Translate.count_documents(
            {"date": date})
        trans = list(Translate.find(
            {"date": date}, {"_id": 0}))
        return render_template("pages/specific.html", translates=trans, count=count_translate, date=date)


@app.route('/next', methods=['GET'])
def next_text():
    lines = open(file_name).read().splitlines()
    selected = random.choice(lines)
    print(selected+"\n")

    return selected


@app.route('/insert', methods=['GET'])
def insert():
    Translate.insert_many([
        {
            "date": "10-02-2021",
            "english": "Try to enjoy yourselves.",
            "ip": "127.0.0.1",
            "pidgin": "For enjoy we.",
            "user": {
                "name": "Jay"
            }
        },
        {
            "date": "10-02-2021",
            "english": "I take my hat off to you.",
            "ip": "127.0.0.1",
            "pidgin": "I move my cap for you.",
            "user": {
                "name": "Jay"
            }
        },
    ])


@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        user = request.form['user']
        from_statement = request.form['from']
        to_statement = request.form['to']
        new_translate = {
            "english": from_statement,
            "pidgin": to_statement,
            "date": datetime.now().strftime("%d-%m-%Y"),
            "user": {
                "name": user,
                "ip": str(request.remote_addr)
            },
        }

        print(new_translate)
        val = next_text()

        try:
            Translate.insert_one(new_translate)
            print("res", "*************")
        except:
            return (error)
        return render_template("index.html", text=val, user=str(user))


def seperate_sentences():
    global input_sentences
    count = 0
    for line in open(r'fra.txt', encoding="utf-8"):
        count += 1

        if line == None:
            break

        if '\t' not in line:
            continue

        input_sentence = line.split('\t', 1)[0]
        input_sentences.append(input_sentence)

    for el in input_sentences:
        new_file = open("english-only.txt", "a")
        new_file.write(el+"\n")
        new_file.close()

    return "Post"


@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        from_lang = request.form['from']
        sentence = request.form['sentence']
        if from_lang != 'en':
            to_lang = 'en'
            input_word = trans.get_translation(sentence, to_lang)
            # print(input_word, 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
        else:
            input_word = sentence

        trans.translate_word(input_word)         
        return render_template("pages/try.html")
