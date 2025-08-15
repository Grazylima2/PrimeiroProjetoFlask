from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')

        return render_template("resultado.html", nome=nome, idade=idade)
    
    return render_template("index.html")
    
@app.route('/sobre')
def sobre():
    return "<h2>Esse é um mini projeto Flask com rotas, formulário e template</h2>"

if __name__ == '__main__':
    app.run(debug=True)