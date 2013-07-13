
import requests
from api import *

from flask import Flask, render_template, request, session, redirect, url_for, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)
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
    email = db.Column(db.Text, unique=True)
    jobs = db.relationship('Jobposting', secondary=saved_jobs, backref=db.backref('jobposting', lazy='dynamic'))

    def __init__(self, access_token=None, email=None):
        self.access_token = access_token
        self.email = email

    def __repr__(self):
        return '<User %r Email: %s>' % (self.id, self.email)


class Jobposting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Text, nullable=False)
    company_description = db.Column(db.Text, nullable=False)
    industry = db.Column(db.Text, nullable=False)
    job_title = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Text, nullable=False)
    employment_type = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    desired_skills = db.Column(db.Text, nullable=False)
    university = db.Column(db.Text, nullable=False)

    def __init__(self, company, company_description, industry, job_title, experience, employment_type, job_description, desired_skills, university):
        self.company = company
        self.company_description = company_description
        self.industry = industry
        self.job_title = job_title
        self.experience = experience
        self.employment_type = employment_type
        self.desired_skills = desired_skills
        self.job_description = job_description
        self.university = university

    def __repr__(self):
        return '<JobPosting %r>' % self.id


@app.route("/")
def index():
    if 'access_token' in session:
        return redirect(url_for('student_profile'))
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
    email = User.query.filter_by(email=user['email']).count()
    if not email:
        newuser = User(access_token=token, email=user['email'])
        db.session.add(newuser)
        db.session.commit()
        print 'user saved to db'
    return render_template('profile.html', user=user, job=job)


@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('index'))


@app.route('/index')
def dashboard():
    return render_template('index.html')


@app.route('/postjob', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        jobpost = JobPosting(
            company = request.form['company'],
            company_description = request.form['company_discription'],
            industry = request.form['industry'],
            job_title = request.form['job_title'],
            experience = request.form['experience'],
            employment_type = request.form['employment_type'],
            job_description = request.form['job_description'],
            desired_skills = request.form['desired_skills'],
            university = request.form['university'])
        db.session.add(jobpost)
        db.session.commit()
    return render_template('postjob.html')


app.secret_key = '\xf8\x98\x80\xea\xde\xad\x9d\xf9\x90\xf58\x19\x062\x13]&f\x90\xb6Q\x1b\xf6\xb8'

if __name__ == '__main__':
    app.run()


