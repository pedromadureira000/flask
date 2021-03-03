from flask import Flask, jsonify, render_template

app = Flask('flask', template_folder='./static')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<variavel>')
def variavel(variavel):
    return f'Site Flask com parametro "{variavel}"'

@app.route('/path/<parametro>')
def path_com_variavel(parametro):
    return f'Site Flask com path + parametro "{parametro}"', 201

@app.route('/json/<valor>')
def json(valor):
    r = {
        'nome': valor,
        'idade': 18
    }
    return jsonify(r)



app.run()