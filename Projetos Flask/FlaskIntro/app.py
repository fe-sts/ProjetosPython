from flask import Flask

# app é uma instância da classe Flask
# essa instância recebe a var "__name__" -->  
# o interpretador do python cria qndo executa o arquivo. 
# Sempre dá um valor a ela que especifica o qual que é  o arquivo que se está executando (se Principal ou Secundário)
# __name__: ver que vai controlar a aplicação inteira. todo o flask está 'contido' nela.
app = Flask(__name__) 

# decorator --> é uma caracteristica do python. Ele entra sempre antes de uma função.
# está aplicando o método 'route' sobre a função 'index'. Ele vai definir um rota para a página.
@app.route("/")
def index(): #por padrão, foi colocado o nome da pagina de index
    return('Hello world!')

# segurança --> verifica se o usuario está executando o arquivo principal e não um secundário da app.
# flask só vai dar o run se esse for o arquivo Principal
if __name__ == "__main__":
    app.run()
