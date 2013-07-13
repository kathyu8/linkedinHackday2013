from app import db
from job_postings import JobPosting


# class SavedJobs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(80))
#     parent = db.relationship('JobPosting', backref='children', lazy='select', remote_side=[id])
#     parent_id = db.Column(db.Integer, db.ForeignKey('JobPosting.id'))
