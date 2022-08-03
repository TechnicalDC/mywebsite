from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Sections(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

@app.route('/')
def homepage():
    data = {
        "title": "technicaldc",
        "name" : "Welcome"
    }
    return render_template("index.html", data = data)

if __name__ == '__main__':
    app.run(debug = True)

