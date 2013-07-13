from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)
from flask.ext.sqlalchemy import SQLAlchemy
     
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/post-job')
def post_job():
    retval = {'title': 'Job Posting',
            }
    if request.method == 'POST':
        print 'post'
        return 'post'
    print 'get'
    return render_template('post-job.html', None)
    

if __name__ == '__main__':
    app.run()
