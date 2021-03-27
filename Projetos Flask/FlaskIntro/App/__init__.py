#cada __init__ indica um módulo

from flask import Flask

# app é uma instância da classe Flask
# essa instância recebe a var "__name__" -->  
# o interpretador do python cria qndo executa o arquivo. 
# Sempre dá um valor a ela que especifica o qual que é  o arquivo que se está executando (se Principal ou Secundário)
# __name__: ver que vai controlar a aplicação inteira. todo o flask está 'contido' nela.
app = Flask(__name__) 

from App.controlers import default


#if __name__ == "main":
#    app.run() --> foi para o run.py
