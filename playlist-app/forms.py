"""Forms for playlist app."""

from wtforms import SelectField, StringField,TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this 
    name = StringField('Playlist Name',validators=[InputRequired()])
    description = TextAreaField('Playlist Description',validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField('Song',validators=[InputRequired()])
    artist = StringField('Song Artist', validators=[InputRequired()])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
