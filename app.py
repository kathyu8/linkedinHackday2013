import requests
import json

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/hola")
def hola():
    code = request.args.get('code')
    redirect_uri = "http://localhost:5000/hola"
    r = requests.get('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code='+code+'&redirect_uri='+redirect_uri+'&client_id=dkqwsero67sh&client_secret=GGxpjoa5b5NFCOxU')
    response = json.loads(r.content)
    session['access_token'] = response['access_token']
    return redirect(url_for('profile'))


@app.route("/profile")
def profile():
    token = session['access_token']
    profile = requests.get('https://api.linkedin.com/v1/people/~:(first-name,last-name,email-address,summary,specialties,positions,picture-url,skills)?format=json&oauth2_access_token='+token)
    return profile.content

app.secret_key = '\xf8\x98\x80\xea\xde\xad\x9d\xf9\x90\xf58\x19\x062\x13]&f\x90\xb6Q\x1b\xf6\xb8'

if __name__ == "__main__":
    app.run()
