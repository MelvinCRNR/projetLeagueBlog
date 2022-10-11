from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Rester connecté')
    submit = SubmitField("Se connecter")


class RegistrationForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    email = StringField('Adresse mail', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirmez votre mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("S'enregistrer")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Nom d'utilisateur déjà utilisé.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Adresse mail non valide.')


class EditProfileForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    about_me = TextAreaField('À propos de moi', validators=[Length(min=0, max=140)])
    champion = TextAreaField('Champion favori', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enregister')


class EmptyForm(FlaskForm):
    submit = SubmitField('Enregistrer')


class PostForm(FlaskForm):
    post = TextAreaField('Message', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Publier')