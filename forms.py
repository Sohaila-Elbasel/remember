from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

VALUES = [('all', 'All'), ('Anime', 'Anime'), ('English series', 'English series')]

class Addshow(FlaskForm):
    name = StringField('Name', validators = [ DataRequired(), Length(min=1, max=50)])
    last_ep = StringField('Last_ep', validators= [DataRequired(), Length(min=1, max=5)])
    season = StringField('Season', validators= [DataRequired(), Length(min=1, max=5)])
    type = SelectField('type', validators = [DataRequired()], choices=VALUES)
    submit = SubmitField('Add')
