from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)
from flask.ext.sqlalchemy import SQLAlchemy

     
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.debug = True

    
class JobPosting(db.Model):
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
    

    def __init__(self, company, company_description, industry, job_title,
                experience, employment_type, job_description, 
                desired_skills, university):
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
        
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.Text)
    email = db.Column(db.Text)
    expires_in = db.Column(db.DateTime)
    
    def __init__(self, access_token=None, email=None):
        self.access_token = access_token
        self.email = email
    

    def __repr__(self):
        return '<User %r>' % self.id

@app.route('/')
def hello_world():
    db.create_all()
    return 'Hello World!'
    
@app.route('/postjob', methods=['GET','POST'])
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

if __name__ == '__main__':
    app.run()
