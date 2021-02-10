from flask import Flask, redirect, url_for, request, render_template, jsonify
import os
from flask.wrappers import Request
import pymongo
from dotenv import load_dotenv
import datetime
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import firebase_admin
# from firebase_admin import credentials, db
# from firebase import firebase


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "translate_database.db"))


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Translate(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    english = db.Column(db.String(50))
    pidgin = db.Column(db.String(200))
    date = db.Column(db.String(200))
    ip = db.Column(db.String(10))


def __init__(self, user, english, pidgin, date, ip):
    self.user = user
    self.english = english
    self.pidgin = pidgin
    self.date = date
    self.ip = ip


def __repr__(self):
    return "<User: {}>".format(self.user)


db.create_all()

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
    trans = Translate.query.all()

    print(val, "---------")
    return render_template("pages/translated.html", text=val, translates=trans)
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
        translate = Translate(user=user, english=from_statement,
                              pidgin=to_statement, ip=str(request.remote_addr), date=datetime.now().strftime("%d-%m-%Y"))
        # translate = {
        #     "user": user,
        #     "english": from_statement,
        #     "pidgin": to_statement
        # }
        print(translate)
        val = next_text()
        try:
            # res = ref.set(translate)
            # new_translate = Translate.insert_one(translate)

            # res = firebase.post("/translate", translate)
            db.session.add(translate)
            db.session.commit()
            print("res", "*************")
        except:
            return ("error")
        return render_template("index.html", text=val, user=user)
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
