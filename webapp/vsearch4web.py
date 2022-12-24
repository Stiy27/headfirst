from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


# O argumento 'req' é atribuido ao objeto de requisição/solicitação do flask,
# enquanto que, o argumento 'res'é atribuido aos resultados da chamada
# da função search4letters.
# "flask_request" é apenas uma notação de argumento da função,
# documentação, o interpretador ignora, não executa
def log_request(req: 'flask_request', res: str) -> None:
    ''' Criar/Salva logs de requisição e resultados '''
    with open('webapp/logs/vsearch.log', 'a') as logs:
        print(req.form, req.remote_addr,
              req.user_agent, res, file=logs, sep=' | ')


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> 'html':
    ''' Extrai os dados postados no formulário; executa a busca;
        retorna os resultados '''
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           the_title=title,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    ''' Exibe este webapp em formato HTML '''
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    ''' Exibe o conteúdo do log na página '''
    with open('webapp/logs/vsearch.log') as log:
        # read() lé o arquivo todo de uma só vez
        contents = log.read()
    # "escape" do flask, converte e exibe os caracteres especiais
    return escape(contents)


# Permite executar app.run localmente, mas impede que AythonAnywhere o execute
# Localmente __name__ será '__main__', na núvem __name será 'vsearch4web' \
    # o proprio arquivo/módulo importado por PythonAnywhere
if __name__ == '__main__':
    app.run(debug=True)
