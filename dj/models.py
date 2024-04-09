"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(15), nullable=False, unique=True)
    description = db.Column(db.Text)

 

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)


    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlist_song'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))

    playlist = db.relationship("Playlist", backref="playlist_song")
    song = db.relationship("Song", backref="playlist_song")

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
