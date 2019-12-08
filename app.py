from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from formularios import CadastroForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SHHHHHHHHHH!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DancoDeDados.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False,)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():

    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroForm()

    if form.validate_on_submit():
        novo_user = User(nome=form.nome.data, email=form.email.data, senha=form.senha.data)
        db.session.add(novo_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('cadastro.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)