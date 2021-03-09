from flask import Flask, abort
import db

app = Flask(__name__)

@app.route('/')
def root():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f"<li><a href = ' /user/{username}'>{user['name']}</a></li>"
        )
    html.append('</ul>')
    return '\n'.join(html)

def profile(username):
    """Retorna um usuario especifico filtrando pelo username"""
    user = db.users.get(username)

    if user:
        return f"""
            <h1>{user['name']}</h1>
            <img src="{user['image']}"/><br/>
            telefone: {user['tel']} <br/>
            <a href="/">Voltar</a>
        """
    else:
        return abort(404, "user not found")


app.run(use_reloader = True)

                # exemplos de rotas

#from flask import Flask, jsonify, render_template

# app = Flask(__name__, template_folder="./static")
#
# @app.route('/')
# def root():
#     return f'oi'

# @app.route('/')
# def root():
#     return render_template('index.html')
#
# @app.route('/<variavel>')
# def variavel(variavel):
#     return f'Site Flask com parametro "{variavel}"'
#
# @app.route('/path/<parametro>')
# def path_com_variavel(parametro):
#     return f'Site Flask com path + parametro "{parametro}"', 201
#
# @app.route('/json/<valor>')
# def json(valor):
#     r = {
#         'nome': valor,
#         'idade': 18
#     }
#     return jsonify(r)

#app.run()