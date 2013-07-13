import requests
from api import *

from flask import Flask, render_template, request, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


saved_jobs = db.Table('saved_jobs',
    db.Column('user.id', db.Integer, db.ForeignKey('user.id')),
    db.Column('jobposting.id', db.Integer, db.ForeignKey('jobposting.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.Text)
    email = db.Column(db.Text)
    expires_in = db.Column(db.DateTime)
    saved_jobs = db.relationship('JobPosting', secondary='saved_jobs', backref=db.backref('pages', lazy='dynamic'))


class Jobposting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Text, nullable=False)
    company_description = db.Column(db.Text, nullable=False)
    industry = db.Column(db.Text, nullable=False)
    job_title = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Text, nullable=False)
    employment_type = db.Column(db.Text, nullable=False)
    desired_skills = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    university = db.Column(db.Text, nullable=False)


@app.route("/")
def index():
    if 'access_token' in session:
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route("/hola")
def hola():
    code = request.args.get('code')
    redirect_uri = "http://localhost:5000/hola"
    token = api.get_access_token(code=code, redirect_uri=redirect_uri)
    session['access_token'] = token
    return redirect(url_for('profile'))


@app.route("/profile")
def student_profile():
    token = session['access_token']
    profile = requests.get('https://api.linkedin.com/v1/people/~:(first-name,last-name,email-address,summary,specialties,positions,picture-url,skills,educations)?format=json&oauth2_access_token='+token)
    job = {
        'company': 'linkedin',
        'job_title': 'Software Engineer Intern',
        'desired_skills': 'C++, Git',
        'job_description': 'Looking for a summer intern to do some work.',
        'university': 'CMU'
    }
    user = get_student_profile(profile.content)
    return render_template('profile.html', user=user, job=job)


@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('index'))

@app.route('/index')
def dashboard():
    return render_template('index.html')

app.secret_key = '\xf8\x98\x80\xea\xde\xad\x9d\xf9\x90\xf58\x19\x062\x13]&f\x90\xb6Q\x1b\xf6\xb8'

if __name__ == "__main__":
    app.run()
