from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return '<h1><u>Welcome to search4letter on the Web!</u></h1>'


@app.route('/search4', methods = ['GET', 'POST'])
def do_search() -> str:
    return str(search4letters('', 'eiru,!'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')


app.run()
