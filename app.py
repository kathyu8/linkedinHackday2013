import requests

from flask import Flask, render_template, request, session
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/hola")
def hola():
    code = request.args.get('code')
    redirect_uri = "http://localhost:5000/hola"
    r = requests.get('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code='+code+'&redirect_uri='+redirect_uri+'&client_id=dkqwsero67sh&client_secret=GGxpjoa5b5NFCOxU')
    return r.content

app.secret_key = 'tumaieslagorda'

if __name__ == "__main__":
    app.run()
