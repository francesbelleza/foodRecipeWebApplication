# Need to create:
#  [DONE] Recipe form with following:
#       [x] title [string, required]
#       [x] description [TextArea, required]
#       [x] ingredients [TextArea, required]
#       [x] instructions [TextArea, required
#       [x] submit field

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets.core import TextArea


class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NewRecipe(FlaskForm):
    title = StringField('Recipe Title', validators = [DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit = SubmitField('Save')

