# Need to create:
#  [DONE] Recipe form with following:
#       [x] title [string, required]
#       [x] description [TextArea, required]
#       [x] ingredients [TextArea, required]
#       [x] instructions [TextArea, required
#       [x] submit field

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets.core import TextArea


class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NewRecipe(FlaskForm):
    title = StringField('Recipe Title', validators = [DataRequired()])
    description = TextArea('Description', validators = [DataRequired()])
    ingredients = TextArea('Ingredients', validators=[DataRequired()])
    instructions = TextArea('Instructions', validators=[DataRequired()])
    submit = SubmitField('Save')

