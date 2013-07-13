from app import db

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
