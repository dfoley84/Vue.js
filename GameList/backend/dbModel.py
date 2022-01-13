from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), unique=False)
    genre = db.Column(db.String(120), unique=False)
    played = db.Column(db.String(120), unique=False)

    @property
    def serialize(self):
        # Returns Data Object In Proper Format
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'played': self.played
        }
