from logging import error
from flask import Flask, redirect, url_for, request, render_template, jsonify
import os
from flask.wrappers import Request
from pymongo import MongoClient
from dotenv import load_dotenv
import datetime
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

client = MongoClient(
    "mongodb+srv://user:Mypassword123@cluster0.w2btl.mongodb.net/translate_db?retryWrites=true&w=majority")

db = client.get_database("translate_db")
Translate = db.translate

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


@app.route("/translated", methods=['GET'])
def translated():
    val = next_text()
    trans = list(Translate.find())
    print(val, "---------")
    return render_template("pages/translated.html", text=val, translates=trans)


@app.route('/next', methods=['GET'])
def next_text():
    lines = open(file_name).read().splitlines()
    selected = random.choice(lines)
    print(selected+"\n")

    return selected


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
