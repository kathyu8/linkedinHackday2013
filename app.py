
import requests
from api import *
import json

from flask import Flask, render_template, request, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Savedjobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    jobid = db.Column(db.Integer)

    def __init__(self, userid=None, jobid=None):
        self.userid = userid
        self.jobid = jobid


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    recruiter = db.Column(db.Boolean)
    picture = db.Column(db.Text)
    public_profile_url = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'access_token': self.access_token,
            'email': self.email,
            'recruiter': self.recruiter,
            'picture': self.picture,
            'public_profile_url': self.public_profile_url
        }

    def __init__(self, access_token=None, email=None, recruiter=None, picture=None, public_profile_url=None):
        self.access_token = access_token
        self.email = email
        self.recruiter = recruiter
        self.picture = picture
        self.public_profile_url = public_profile_url

    def __repr__(self):
        return '<User %r Email: %s>' % (self.id, self.email)


class Jobposting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    company = db.Column(db.Text, nullable=False)
    company_description = db.Column(db.Text, nullable=False)
    industry = db.Column(db.Text, nullable=False)
    job_title = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Text, nullable=False)
    employment_type = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    desired_skills = db.Column(db.Text, nullable=False)
    year = db.Column(db.Text, nullable=False)
    university = db.Column(db.Text, nullable=False)
    tags = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'company_description': self.company_description,
            'industry': self.industry,
            'job_title': self.job_title,
            'experience': self.experience,
            'employment_type': self.employment_type,
            'job_description': self.job_description,
            'desired_skills': self.desired_skills,
            'year': self.year,
            'university': self.university,
            'tags': self.tags,
            'location': self.location,
            'date': self.date,
        }

    def __init__(self, company=None, company_description=None, industry=None, job_title=None, experience=None, employment_type=None, job_description=None, desired_skills=None, university=None, tags=None, year=None, userid=None, location=None, date=None):
        self.company = company
        self.company_description = company_description
        self.industry = industry
        self.job_title = job_title
        self.experience = experience
        self.employment_type = employment_type
        self.desired_skills = desired_skills
        self.job_description = job_description
        self.university = university
        self.year = year
        self.tags = tags
        self.userid = userid
        self.location = location
        self.date = date

    def __repr__(self):
        return u'<Job Posting: %r>' % self.id


@app.route("/")
def index():
    session.pop('user', None)
    if 'access_token' in session:
        return redirect(url_for('student_profile'))
    return render_template('login.html')


@app.route("/student_login")
def hola_student():
    code = request.args.get('code')
    redirect_uri = "http://localhost:5000/student_login"
    r = requests.get('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code='+code+'&redirect_uri='+redirect_uri+'&client_id=dkqwsero67sh&client_secret=GGxpjoa5b5NFCOxU')
    response = json.loads(r.content)
    session['access_token'] = response['access_token']
    return redirect(url_for('student_profile'))


@app.route("/recruiter_login")
def hola_recruiter():
    code = request.args.get('code')
    redirect_uri = "http://localhost:5000/recruiter_login"
    r = requests.get('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code='+code+'&redirect_uri='+redirect_uri+'&client_id=dkqwsero67sh&client_secret=GGxpjoa5b5NFCOxU')
    response = json.loads(r.content)
    session['access_token'] = response['access_token']
    return redirect(url_for('recruiter_profile'))


@app.route("/student_profile")
def student_profile():
    token = session['access_token']
    profile = requests.get('https://api.linkedin.com/v1/people/~:(first-name,last-name,email-address,summary,specialties,positions,picture-url,skills,educations,public-profile-url)?format=json&oauth2_access_token='+token)
    user = get_student_profile(profile.content)
    me = User.query.filter_by(email=user['email']).first()

    # Save user to db if not already there
    if not me:
        newuser = User(access_token=token, email=user['email'], recruiter=False, picture=user['picture'], public_profile_url=user['public_profile_url'])
        db.session.add(newuser)
        db.session.commit()
        session['user'] = newuser.to_dict()
        print 'user saved to db'
    else:
        session['user'] = me.to_dict()

    # Get jobs that apply to user and convert them to python dicts
    query = Jobposting.query.filter_by(university=user['schoolName'])
    jobs = []
    for item in query:
        jobs.append(item.to_dict())

    query2 = Savedjobs.query.filter_by(userid=session['user']['id'])
    saved = []
    for item in query2:
        job = Jobposting.query.filter_by(id=item.jobid).one()
        saved.append(job.to_dict())
    return render_template('student.html', jobs=jobs, saved=saved)


@app.route("/recruiter_profile")
def recruiter_profile():
    token = session['access_token']
    profile = requests.get('https://api.linkedin.com/v1/people/~:(first-name,last-name,email-address,summary,specialties,positions,picture-url,skills,educations,public-profile-url)?format=json&oauth2_access_token='+token)
    user = get_student_profile(profile.content)
    me = User.query.filter_by(email=user['email']).first()

    # Save user to db if not already there
    if not me:
        newuser = User(access_token=token, email=user['email'], recruiter=True, picture=user['picture'], public_profile_url=user['public_profile_url'])
        db.session.add(newuser)
        db.session.commit()
        session['user'] = newuser.to_dict()
        print 'user saved to db'
    else:
        session['user'] = me.to_dict()

    # Get info relevant to recruiter
    query = Jobposting.query.filter_by(userid=session['user']['id'])
    jobs = []
    students = []
    for item in query:
        res = item.to_dict()
        res['count'] = Savedjobs.query.filter_by(jobid=item.id).count()
        jobs.append(res)
        ids = Savedjobs.query.all()
        if ids:
            for sid in ids:
                s = User.query.all()[0]
                students.append(s.to_dict())

    return render_template('company-recruiter.html', jobs=jobs, students=students)

@app.route("/applicants")
def applicants():
    token = session['access_token']
    profile = requests.get('https://api.linkedin.com/v1/people/~:(first-name,last-name,email-address,summary,specialties,positions,picture-url,skills,educations)?format=json&oauth2_access_token='+token)
    user = get_student_profile(profile.content)
    me = User.query.filter_by(email=user['email']).first()

    # Save user to db if not already there
    if not me:
        newuser = User(access_token=token, email=user['email'], recruiter=True)
        db.session.add(newuser)
        db.session.commit()
        session['user'] = newuser.to_dict()
        print 'user saved to db'
    else:
        session['user'] = me.to_dict()

    # Get info relevant to recruiter
    query = Jobposting.query.filter_by(userid=session['user']['id'])
    jobs = []
    students = []
    for item in query:
        res = item.to_dict()
        res['count'] = Savedjobs.query.filter_by(jobid=item.id).count()
        jobs.append(res)
        ids = Savedjobs.query.all()
        if ids:
            for sid in ids:
                s = User.query.all()[0]
                students.append(s.to_dict())

    return render_template('applicants.html', jobs=jobs, students=students)

@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('index'))


@app.route('/student')
def student_dashboard():
    return render_template('student.html')


@app.route('/company-recruiter')
def recruiter_dashboard():
    return render_template('company-recruiter.html')


@app.route('/recruiter')
def recruiterTemplate():
    return render_template('recruiter_stream_job_card.html')


@app.route('/editpost')
def edit_post():
    return render_template('edit_post.html')


@app.route('/postjob', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        jobpost = Jobposting(
            userid=session['user']['id'],
            company=request.form['company'],
            company_description=request.form['company_description'],
            industry=request.form['industry'],
            job_title=request.form['job_title'],
            experience=request.form['experience'],
            employment_type=request.form['employment_type'],
            job_description=request.form['job_description'],
            desired_skills=request.form['desired_skills'],
            university=request.form['university'],
            tags=request.form['tags'],
            location=request.form['location'],
            date=request.form['date'],
            year=request.form['year'])
        db.session.add(jobpost)
        db.session.commit()
        return redirect(url_for('recruiter_profile'))
    return render_template('postjob.html')


@app.route('/savejob')
def save_job():
    uid = request.args.get('userid')
    jid = request.args.get('jobid')
    job = Savedjobs(userid=uid, jobid=jid)
    db.session.add(job)
    db.session.commit()
    return redirect(url_for('student_profile'))


@app.route('/contact_student')
def contact_student():
    return('sueno.html')


app.secret_key = '\xf8\x98\x80\xea\xde\xad\x9d\xf9\x90\xf58\x19\x062\x13]&f\x90\xb6Q\x1b\xf6\xb8'

if __name__ == '__main__':
    app.run()
