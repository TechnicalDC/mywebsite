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

@app.route('/home')
def home():
    data = {
        "title": "technicaldc",
        "name" : " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed elementum nulla. In turpis ex, vulputate vel porttitor sed, elementum non arcu. Proin volutpat magna id justo pretium, id laoreet lorem faucibus. Maecenas facilisis luctus velit, sed molestie erat rhoncus at. Vestibulum magna felis, tempor et mi et, volutpat ornare enim. Curabitur sit amet sem vitae neque maximus suscipit a ac est. Donec egestas eget lacus a feugiat. Donec vestibulum ex nulla, id finibus odio lacinia ac. Morbi efficitur, ex non mattis luctus, ipsum leo pretium neque, in rutrum metus dolor eget neque. Donec in felis lorem. Aenean id viverra mauris. Aliquam sit amet enim dignissim sem semper porta. Maecenas commodo vulputate ultricies. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Curabitur tincidunt lacus velit, nec efficitur ex laoreet quis. Cras at lectus neque. Integer sit amet est ut ligula bibendum ullamcorper. Aliquam laoreet quam vel risus laoreet congue. Praesent at lobortis mi. In ultricies quam sed massa pharetra maximus. Sed ullamcorper orci vitae dolor ullamcorper, at scelerisque neque vestibulum. Proin ornare diam augue. Nullam at velit lectus. "
    }
    return render_template("home.html", data = data)

@app.route('/about')
def about():
    data = {
        "title": "technicaldc",
        "name" : " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed elementum nulla. In turpis ex, vulputate vel porttitor sed, elementum non arcu. Proin volutpat magna id justo pretium, id laoreet lorem faucibus. Maecenas facilisis luctus velit, sed molestie erat rhoncus at. Vestibulum magna felis, tempor et mi et, volutpat ornare enim. Curabitur sit amet sem vitae neque maximus suscipit a ac est. Donec egestas eget lacus a feugiat. Donec vestibulum ex nulla, id finibus odio lacinia ac. Morbi efficitur, ex non mattis luctus, ipsum leo pretium neque, in rutrum metus dolor eget neque. Donec in felis lorem. Aenean id viverra mauris. Aliquam sit amet enim dignissim sem semper porta. Maecenas commodo vulputate ultricies. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Curabitur tincidunt lacus velit, nec efficitur ex laoreet quis. Cras at lectus neque. Integer sit amet est ut ligula bibendum ullamcorper. Aliquam laoreet quam vel risus laoreet congue. Praesent at lobortis mi. In ultricies quam sed massa pharetra maximus. Sed ullamcorper orci vitae dolor ullamcorper, at scelerisque neque vestibulum. Proin ornare diam augue. Nullam at velit lectus. "
    }
    return render_template("about.html", data = data)

@app.route('/skills')
def skills():
    data = {
        "title": "technicaldc",
        "name" : " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed elementum nulla. In turpis ex, vulputate vel porttitor sed, elementum non arcu. Proin volutpat magna id justo pretium, id laoreet lorem faucibus. Maecenas facilisis luctus velit, sed molestie erat rhoncus at. Vestibulum magna felis, tempor et mi et, volutpat ornare enim. Curabitur sit amet sem vitae neque maximus suscipit a ac est. Donec egestas eget lacus a feugiat. Donec vestibulum ex nulla, id finibus odio lacinia ac. Morbi efficitur, ex non mattis luctus, ipsum leo pretium neque, in rutrum metus dolor eget neque. Donec in felis lorem. Aenean id viverra mauris. Aliquam sit amet enim dignissim sem semper porta. Maecenas commodo vulputate ultricies. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Curabitur tincidunt lacus velit, nec efficitur ex laoreet quis. Cras at lectus neque. Integer sit amet est ut ligula bibendum ullamcorper. Aliquam laoreet quam vel risus laoreet congue. Praesent at lobortis mi. In ultricies quam sed massa pharetra maximus. Sed ullamcorper orci vitae dolor ullamcorper, at scelerisque neque vestibulum. Proin ornare diam augue. Nullam at velit lectus. "
    }
    return render_template("skills.html", data = data)

@app.route('/contact')
def contact():
    data = {
        "title": "contact",
        "name" : " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed elementum nulla. In turpis ex, vulputate vel porttitor sed, elementum non arcu. Proin volutpat magna id justo pretium, id laoreet lorem faucibus. Maecenas facilisis luctus velit, sed molestie erat rhoncus at. Vestibulum magna felis, tempor et mi et, volutpat ornare enim. Curabitur sit amet sem vitae neque maximus suscipit a ac est. Donec egestas eget lacus a feugiat. Donec vestibulum ex nulla, id finibus odio lacinia ac. Morbi efficitur, ex non mattis luctus, ipsum leo pretium neque, in rutrum metus dolor eget neque. Donec in felis lorem. Aenean id viverra mauris. Aliquam sit amet enim dignissim sem semper porta. Maecenas commodo vulputate ultricies. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Curabitur tincidunt lacus velit, nec efficitur ex laoreet quis. Cras at lectus neque. Integer sit amet est ut ligula bibendum ullamcorper. Aliquam laoreet quam vel risus laoreet congue. Praesent at lobortis mi. In ultricies quam sed massa pharetra maximus. Sed ullamcorper orci vitae dolor ullamcorper, at scelerisque neque vestibulum. Proin ornare diam augue. Nullam at velit lectus. "
    }
    return render_template("contact.html", data = data)


if __name__ == '__main__':
    app.run(debug = True)

