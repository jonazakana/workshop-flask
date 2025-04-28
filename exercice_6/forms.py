from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = None #qq chose (je suis sympa vous avez deja les import)
    submit = None #qq chose egalement...
