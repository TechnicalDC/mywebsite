from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Sections(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    icon = db.Column(db.String, nullable = False)

@app.route('/')
def homepage():
    sections = {}
    data = {
        "sections": sections,
    }
    return render_template("index.html", data = data)

@app.route('/home')
def home():
    sections = {}
    data = {
        "sections": sections,
    }
    return render_template("home.html", data = data)

@app.route('/about')
def about():
    sections = {}
    data = {
        "sections": sections,
    }
    return render_template("about.html", data = data)

@app.route('/skills')
def skills():
    sections = {}
    data = {
        "sections": sections,
    }
    return render_template("skills.html", data = data)

@app.route('/contact')
def contact():
    sections = {}
    data = {
        "sections": sections,
    }
    return render_template("contact.html", data = data)


if __name__ == '__main__':
    app.run(debug = True)

