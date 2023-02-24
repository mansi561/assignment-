from sqlalchemy import PickleType
class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    images = db.Column(PickleType)