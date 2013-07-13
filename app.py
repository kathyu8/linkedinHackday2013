from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)
from flask.ext.sqlalchemy import SQLAlchemy
from models import *

     
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/postjob', methods=['POST'])
def post_job():
    if request.method == 'POST':
        jobpost = JobPosting(
            company = request.form['company'],
            company_discription = request.form['company_discription'],
            industry = request.form['industry'],
            job_title = request.form['job_title'],
            experience = request.form['experience'],
            employment_type = request.form['employment_type'],
            job_description = request.form['job_description'],
            desired_skills = request.form['desired_skills'],
            university = request.form['university'])
        db.context.add(jobpost)
        db.context.commit()
        posts = JobPost.query.all()
        for post in posts:
            print post
    return render_template('postjob.html')

if __name__ == '__main__':
    app.run()
