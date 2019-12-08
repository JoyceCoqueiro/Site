from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CadastroForm(FlaskForm):
    nome = StringField('Nome')
    email = StringField('Email')
    senha = PasswordField('Senha')
    botao = SubmitField('CADASTRAR')

class LoginForm(FlaskForm):
    email = StringField('Email')
    senha = PasswordField('Senha')
    botao = SubmitField('LOGAR')