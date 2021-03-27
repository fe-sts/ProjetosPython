# arquivo separado para o controler --> função de Rota

#importa a var "app" de __init__.py
from App import app

# decorator --> é uma caracteristica do python. Ele entra sempre antes de uma função.
# está aplicando o método 'route' sobre a função 'index'. Ele vai definir um rota para a página.
@app.route("/")
def index(): #por padrão, foi colocado o nome da pagina de index
    return('Hello world!')
