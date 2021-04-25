from flask import Flask, abort, url_for
import db
from converters import RegexConverter, ListConverter

app = Flask(__name__)

app.url_map.converters['regex'] = RegexConverter
app.url_map.converters['list'] = ListConverter
#app.url_map.converters retorna um dicionario

@app.route('/')
def root():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            #f"<li><a href = ' /user/{username}'>{user['name']}</a></li>"
            f"<li><a href = '{url_for('user', username=username)}'>{user['name']}</a></li>"
            #eu chamo a função url_for, chamo o nome do endpoint ao invez de passar a url. Ou seja, faz match com o argumento
            #do endpoint da app.add_url_rule.  Dps vc passa os argumentos que a função recebe, ou seja, todos os argumentos
            #que estão mapeados na url, e na definição da função.
        )
    html.append('</ul>')
    return '\n'.join(html)


@app.route('/user2/<list:usernames>/', endpoint='user2')
def profile2(usernames):
    """Retorna um usuario especifico filtrando pelo username"""
    html = ''
    for username in set(usernames):
        user = db.users.get(username)
        if user:
            html += f"""
                <h1>{user['name']}</h1>
                <img src="{user['image']}"/><br/>
                telefone: {user['tel']} <br/>
                <a href="/">Voltar</a>
            """

    return html or abort(404, "user not found")
# a função abort do flask retorna um response com um erro HTTP, com codigo 400 ou 500.


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
#a função abort do flask retorna um response com um erro HTTP, com codigo 400 ou 500.

app.add_url_rule('/user/<username>/', view_func=profile, endpoint='user')

@app.route('/user/<username>/<int:quote_id>/')
def quote(username,quote_id):
    #user = db.users.get(username)  // precisa de retornar um dicionario vazio se nao encontrar nada. Para nao tentar usar
    #o metodo get em um None (em caso do usuario nao ser econtrado na linha 42)
    user = db.users.get(username, {})
    quote = user.get("quotes",{}).get(quote_id)
    if user and quote:
        return f"""
                   <h1>{user['name']}</h1>
                   <img src="{user['image']}"/><br/>
                    <p><q>{quote}</q></p> 
                   <a href="/">Voltar</a>
               """
    else:
        return abort(404, "user or quote not found")

@app.route('/file/<path:filename>/')
def filepath(filename):
    return  f'argumento recebido {filename}'

@app.route('/reg/<regex("a.*"):name>/')
def reg(name):
    return  f'argumento iniciado com a letra "a" {name}'

@app.route('/reg/<regex("b.*"):name>/')
def reg_b(name):
    return  f'argumento iniciado com a letra "a" {name}'

app.run(use_reloader = True)
#reloader faz com que mudanças no codigo reflitam na aplicação, sem ter q ficar reiniciando ela.



