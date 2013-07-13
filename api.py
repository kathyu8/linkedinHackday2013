import requests
import json


def get_student_profile(content):
    data = json.loads(content)
    user = {}
    user['schoolName'] = data['educations']['values'][0]['schoolName']
    user['email'] = data['emailAddress']
    user['first_name'] = data['firstName']
    user['last_name'] = data['lastName']
    user['picture'] = data['pictureUrl']
    return user
