# IMPORTS
from flask import Flask, render_template, request, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# CONFIGUATION
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "HelloWorld"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# FORM
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField("Submit")

# TABLES
class Configuation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    conf_name = db.Column(db.String, unique = True)
    conf_value = db.Column(db.String, nullable = False)

class Sections(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    disp_name = db.Column(db.String, nullable = False, default = name)
    url = db.Column(db.String, nullable = False)
    icon = db.Column(db.String, nullable = False)
    is_active = db.Column(db.Boolean, default = True)

class About(db.Model):
    id = db.Column(db.Integer, primary_key = True)
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

# ADMIN
admin_area = Admin(app)
admin_area.add_view(ModelView(Configuation, db.session))
admin_area.add_view(ModelView(Sections, db.session))
admin_area.add_view(ModelView(About, db.session))
admin_area.add_view(ModelView(Skills, db.session))
admin_area.add_view(ModelView(Projects, db.session))
admin_area.add_view(ModelView(Contact, db.session))

# VIEWS
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    sections = Sections.query.filter_by(is_active = True).all()
    return render_template("home.html", sections = sections)

@app.route('/about')
def about():
    data = None
    section = Sections.query.filter_by(name = "about", is_active = True).first()
    sections = None
    if section is not None: 
        sections = Sections.query.filter_by(is_active = True).all()
        data = About.query.filter_by(default = True).first()
    return render_template("about.html", data = data, sections = sections)

@app.route('/skills')
def skills():
    skills = None
    sections = None
    section = Sections.query.filter_by(name = "skills", is_active = True).first()
    if section is not None: 
        skills = Skills.query.all()
        sections = Sections.query.filter_by(is_active = True).all()
    return render_template("skills.html", data = skills, sections = sections)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = None
    section = Sections.query.filter_by(name = "contact", is_active = True).first()
    sections = Sections.query.filter_by(is_active = True).all()
    if section is not None: 
        form = ContactForm()
        name = None
        email = None
        message = None
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            message = form.message.data
            contact = Contact(name = name, email = email, message = message)
            db.session.add(contact)
            db.session.commit()
            form.name.data = None
            form.email.data = None
            form.message.data = None
    return render_template("contact.html", form = form, sections = sections)

@app.route('/projects')
def project():
    sections = Sections.query.filter_by(is_active = True).all()
    return render_template("projects.html", sections = sections)


# MAIN
if __name__ == '__main__':
    app.run(debug = True)

