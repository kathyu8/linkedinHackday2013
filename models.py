from app import db

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

