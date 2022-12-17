from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return '<h1><u>Welcome to search4letter on the Web!</u></h1>'


@app.route('/search4', methods = ['GET', 'POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    
    return render_template('results.html', the_phrase = phrase,
                           the_letters = letters, the_results = results, the_title = title)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')


app.run(debug=True)
