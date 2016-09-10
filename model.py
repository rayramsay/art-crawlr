from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


class Artwork(db.Model):
    """save artwork information"""
    __tablename__ = "artworks"

    artwork_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    artist = db.Column(db.Text, nullable=True)
    credit_line = db.Column(db.Text, nullable=True)
    lat = db.Column(db.Float(10), nullable=False)
    lng = db.Column(db.Float(10), nullable=False)
    location_description = db.Column(db.Text, nullable=True)
    medium = db.Column(db.Text, nullable=True)
    title = db.Column(db.Text, nullable=True)
    zipcode = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<lat=%s lng=%s title=%s artist=%s zipcode=%s>" % (self.lat, self.lng, self.title, self.artist, self.zipcode)


# class User(db.Model):
#     """Save User info"""
#      __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    


    
    



