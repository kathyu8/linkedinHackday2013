from app import db

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Text, nullable=False)
    company_description = db.Column(db.Text, nullable=False)
    industry = db.Column(db.Text, nullable=False)
    job_title = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Text, nullable=False)
    employment_type = db.Column(db.Text, nullable=False)
    desired_skills = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    university = db.Column(db.Text, nullable=False)
    

def __init__(self, company, company_description, industry, job_title,
                experience, employment_type, desired_skills, 
                job_description, university):
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
