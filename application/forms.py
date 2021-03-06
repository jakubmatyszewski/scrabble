"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ResultForm(FlaskForm):
    """Result Form."""
    points = IntegerField(
        'Points',
        validators=[
            DataRequired(message="What was the SUM of scores in the game?\
                [Integer]"),
        ]
    )
    time = IntegerField(
        'Time',
        validators=[
            DataRequired(message="How many minutes did the game last?\
                [Integer]"),
        ]
    )
    submit = SubmitField('Submit')
