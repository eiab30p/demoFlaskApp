"""
Creating Registration Form Validation and Queries.

The script below is an example of how to screate, validate, regex, options, and
other useful information when creating we parts for a website.

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Regexp, DataRequired

# This is the Regex to validate name variables mostly for first and last
name_regex_validator = Regexp(
    "^[a-zA-Z]([a-zA-Z ']{2,250})$",
    message="Only letters, \"-\" and ' allowed, should start with a letter\
    , and be 2 to 250 characters"
)
# This will allow only zero(0) or one (1) chars to be entered
one_char_regex_validator = Regexp(
    "^[a-zA-Z]([a-zA-Z]{0,1})$",
    message="Only one (1) letter allowed for middle initial."
)
# Validationg an email Address
email_regex_validator = Regexp(
    "\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@\
    (?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\z",
    message="Email Does Not Match"
)


class RegistrationForm(FlaskForm):
    """
    Basic Registration Form.

    This basic form shows how to create inputs, dropdown,
    radio, validation and more.
    """

    # DataRequired is telling the field this is a required for the user
    # the function name_regex_validator is called from above
    first_name = StringField('First Name', validators=[
        DataRequired("Please Enter Your First Name"),
        name_regex_validator
    ])
    last_name = StringField('Last Name', validators=[
        DataRequired("Please Enter Your Last Name"),
        name_regex_validator
    ])
    # EmailField will have a semi good regex looking for the  @ simple
    email = EmailField('Email Address', validators=[
        DataRequired("Please Enter Your Email")
    ])
    # TextArea For A Message to be sent via Email
    email_message = TextAreaField('Send A Special Message', validators=[
        DataRequired("Please Enter Message.")
    ])
    # SubmitField to sned the data
    submit = SubmitField("Send Email")
