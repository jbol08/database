"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    description = db.Column(db.Text,nullable=False)

    songs = db.relationship('Song',secondary='playlists_songs',backref='playlist')
    
    
    # def songs(self):
    #     '''make a dictionary to call in app routes'''
    
    #     return {
    #         "artist":self.artist,
    #         "title":self.title,}
    
    
    def __repr__(self):
        """Get all pets matching that species."""

        return f'<Playlist {self.name}>'

class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.Text,nullable=False)
    artist = db.Column(db.Text,nullable=False)

    songs = db.relationship('PlaylistSong')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlists_songs'
    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    playlist_id = db.Column(db.Integer,db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer,db.ForeignKey('songs.id'))

    # songs = db.relationship('Song')   
    playlist = db.relationship('Playlist') 

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
