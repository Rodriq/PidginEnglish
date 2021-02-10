from flask import Flask, redirect, url_for, request, render_template, jsonify
import os
from flask.wrappers import Request
import pymongo
from dotenv import load_dotenv
import datetime
import random
import firebase_admin
from firebase_admin import credentials, db


# from firebase import firebase


load_dotenv()

app = Flask(__name__)

# client = pymongo.MongoClient(os.getenv("MONGO_URI"))


# db = client.test_database
# Post = db.post

# Translate = db.translate

# cred = credentials.Certificate(
#     "pidgin-english-firebase-adminsdk-q740s-8b0b1796f9.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://pidgin-english-default-rtdb.firebaseio.com/'
# })

# ref = db.reference('translate/')
# pidgin_ref = ref.child('pidgin')

input_sentences = []
file_name = "static/words/english-only.txt"

username = ""


@app.route("/")
def index():
    val = next_text()
    print(val, request.remote_addr, "---------")
    return render_template("index.html", text=val, ipAdress = request.remote_addr)


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
    print(val, "---------")
    return render_template("pages/translated.html", text=val)
# @app.route("/")
# def hello():
#     post = {"author": "Mike", "text": "My first blog post!", "tags": [
#         "mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
#     post_id = Post.insert_one(post).inserted_id
#     # return ({"post": post, "id" : post_id})


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
        translate = {
            "user": user,
            "english": from_statement,
            "pidgin": to_statement
        }

        print(translate)
        val = next_text()
        try:
            # res = ref.set(translate)
            # new_translate = Translate.insert_one(translate)
            
            # res = firebase.post("/translate", translate)
            print("res", "*************")
        except:
            return ("error")
        return render_template("index.html", text=val, user=translate["user"])
        # return jsonify(new_translate)


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
