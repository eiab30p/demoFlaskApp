"""
Creating Registration Form Validation and Queries.

The script below is an example of how to screate, validate, regex, options, and
other useful information when creating we parts for a website.

"""
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, SubmitField,\
    TextAreaField
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

    This basic form shows how to create inputs, dropdown, radio, validation
     and more.
    """

    # DataRequired is telling the field this is a required for the user
    # the function name_regex_validator is called from above
    first_name = StringField('First Name', validators=[
        DataRequired("Please Enter Your First Name"),
        name_regex_validator
    ])
    middle_name = StringField('Middle Name', validators=[
        one_char_regex_validator
    ])
    last_name = StringField('Last Name', validators=[
        DataRequired("Please Enter Your Last Name"),
        name_regex_validator
    ])
    # EmailField will have a semi good regex looking for the  @ simple
    email = EmailField('Email Address', validators=[
        DataRequired("Please Enter Your Email")
    ])
    # Select is used for your dropdown but the options can also be pulled from
    # a query as well. The choices need to be the value for the application
    # and the display text value.
    random_select_option = SelectField('Random Select For Test', validators=[
        DataRequired("Please Select an Option")
    ],
        choices=[
        ('', ''), ('Puppies', 'Puppies'), ('Kitties', 'Kitties'),
        ('Travel', 'Travel')
    ])
    # TextArea For A Message to be sent via Email
    email_message = TextAreaField('Send A Special Message', validators=[
        DataRequired("Please Send Me A Message.")
    ])
    # BooleanField are used as they are a checkbox, this one is required
    # for TOS
    accept_tos = BooleanField('Are You Sure?', validators=[
        DataRequired("Select The CheckBox if You Really Want To Send the Email")
    ])
    # SubmitField to sned the data
    submit = SubmitField("Submit Content")
