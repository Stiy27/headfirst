from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return '<h1><u>Hello world from Flask!</u></h1>'

@app.route('/user')
def user() -> str:
    return '<h1>Esta é a página do usuário.</h1>'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything!', 'eiru,!'))
    

app.run()