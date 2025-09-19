# Defines the form used to search for pets
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, RadioField, SubmitField
from wtforms.validators import DataRequired


# Sets up the pet search form with all input fields and validation rules
class PetSearchForm(FlaskForm):
    animal_type = StringField("Animal Type", validators=[DataRequired()])
    location = StringField("Location (City, State or Zip Code)", validators=[DataRequired()])
    breed = StringField("Breed (Optional)")

    age_range = SelectField("Age Range", choices=[
        ("", "Any"), ("baby", "Baby"), ("young", "Young"),
        ("adult", "Adult"), ("senior", "Senior")
    ])

    gender = RadioField("Gender", choices=[
        ("", "Any"), ("male", "Male"), ("female", "Female")
    ])

    include_photos = BooleanField("Only show pets with photos")
    submit = SubmitField("Search")
