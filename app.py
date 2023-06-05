from flask import Flask, render_template, request
from pln import pesquisar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    query = request.form['query']
    pesquisar(query)
    return "Busca realizada com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
