from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           the_title=title,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')


# Permite executar app.run localmente, mas impede que AythonAnywhere o execute
# Localmente __name__ será '__main__', na núvem __name será 'vsearch4web' \
    # o proprio arquivo/módulo importado por PythonAnywhere
if __name__ == '__main__':
    app.run(debug=True)
