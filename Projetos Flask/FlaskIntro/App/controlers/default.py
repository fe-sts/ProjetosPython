# arquivo separado para o controler --> função de Rota

#importa a var "app" de __init__.py
from flask import render_template
from App import app


# decorator --> é uma caracteristica do python. Ele entra sempre antes de uma função.
# está aplicando o método 'route' sobre a função 'index'. Ele vai definir um rota para a página.
@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user): #por padrão, foi colocado o nome da pagina de index
    return render_template('index.html', user=user) # função recebe uma arquivo .html e o renderiza # junto com o html, envia as variavel que utilizar na pagina. No caso, o Usuário
    









'''
@app.route("/test", defaults={'name': None}) #define como padrão None, assim não dá erro caso çao tenha nome do usuário
@app.route("/test/<name>")
def teste(name):
    return
    if name:
        return "Olá, %s!" % name
    else:
        return("Olá, usuário!")

#@app.route("/test/", methods=['GET'])
'''