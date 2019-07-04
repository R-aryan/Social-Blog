#blog_posts/forms

from flask_wtf import FlaskForm
from wtforms import SelectField,TextField,SubmitField, TextAreaField,StringField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title= StringField('Enter The Title of the Post',validators=[DataRequired()])
    text= TextAreaField('Enter Text', validators=[DataRequired()])
    submit=SubmitField('Post')
