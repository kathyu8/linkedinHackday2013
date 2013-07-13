import requests
import json


def get_access_token(code, redirect_uri):
    r = requests.get('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code='+code+'&redirect_uri='+redirect_uri+'&client_id=dkqwsero67sh&client_secret=GGxpjoa5b5NFCOxU')
    response = json.loads(r.content)
    return response['access_token']


def get_student_profile(content):
    data = json.loads(content)
    user = {}
    user['schoolName'] = data['educations']['values'][0]['schoolName']
    user['email'] = data['emailAddress']
    user['first_name'] = data['firstName']
    user['last_name'] = data['lastName']
    user['picture'] = data['pictureUrl']
    return user
