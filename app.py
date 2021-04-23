from flask import Flask, abort, url_for
import db

app = Flask(__name__)

@app.route('/')
def root():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            #f"<li><a href = ' /user/{username}'>{user['name']}</a></li>"
            f"<li><a href = '{url_for('user',username=username)}'>{user['name']}</a></li>"
            #eu chamo a função url_for, chamo o nome do endpoint ao invez de passar a url. Ou seja, faz match com o argumento
            #do endpoint da app.add_url_rule.  Dps vc passa os argumentos que a função recebe, ou seja, todos os argumentos
            #que estão mapeados na url, e na definição da função.
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


app.run(use_reloader = True)
#reloader faz com que mudanças no codigo reflitam na aplicação, sem ter q ficar reiniciando ela.

