from flask_wtf import FlaskForm
from wtforms import StringField, URLField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddPetForm(FlaskForm):
    pet_name = StringField("Pet name", validators=[InputRequired()])
    pet_species = SelectField("Pet species",choices=[("cat", "Cat"), ("dog", "Dog"), ("porc", "Porcupine")],validators=[InputRequired()])
    pet_pic = URLField("Pet photo", validators=[Optional()])
    pet_age = FloatField("Pet age", validators=[NumberRange(min=0, max=30, message="Age should be between 0 and 30")])
    more_info = StringField("Notes about pet")
    is_available = BooleanField("Available?" ,default="True")