from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    petName = db.Column(db.String(120), unique=False)
    petOwner = db.Column(db.String(120), unique=False)
    aptDate = db.Column(db.String(120), unique=False)
    aptNote  = db.Column(db.String(120), unique=False)

    @property
    def serialize(self):
        # Returns Data Object In Proper Format
        return {
            'id': self.id,
            'petName': self.petName,
            'petOwner': self.petOwner,
            'aptDate': self.aptDate,
            'aptNote': self.aptNote
        }
