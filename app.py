from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "HelloWorld"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class SectionForm(FlaskForm):
    name = StringField('Section name', validators=[DataRequired()])
    url = StringField('Url', validators=[DataRequired()])
    icon = StringField('Icon', validators=[DataRequired()])
    submit = SubmitField("Submit")

class Sections(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    url = db.Column(db.String, nullable = False)
    icon = db.Column(db.String, nullable = False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    section = db.Column(db.String, nullable = False)
    text = db.Column(db.Text, nullable = False)
    default = db.Column(db.Boolean, nullable = False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    message = db.Column(db.Text, nullable = False)

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    progress = db.Column(db.Integer, nullable = False)

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text, nullable = False)
    url = db.Column(db.Text, nullable = False)

@app.route('/')
def homepage():
    sections = {}
    data = {
        "sections": sections,
    }
    return render_template("index.html", data = data)

@app.route('/admin',methods=['POST', 'GET'])
def admin():
    form = SectionForm()
    sections = Sections()
    name = None
    url = None
    icon = None
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        if Sections.query.filter_by(name = name).first():
            raise ValidationError('Name must be less than 50 characters')
        url = form.url.data
        icon = form.icon.data
        sections = Sections(name = name, url = url, icon = icon)
        db.session.add(sections)
        db.session.commit()
    data = Sections.query.all ()
    return render_template("admin.html", data = data, form = form)

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
        "details" : "Hey, I'm Dilip Chauhan, a programmer"
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

