#cada __init__ indica um módulo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand





# app é uma instância da classe Flask
# essa instância recebe a var "__name__" -->  
# o interpretador do python cria qndo executa o arquivo. 
# Sempre dá um valor a ela que especifica o qual que é  o arquivo que se está executando (se Principal ou Secundário)
# __name__: ver que vai controlar a aplicação inteira. todo o flask está 'contido' nela.
app = Flask(__name__) 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' #Aqui entra a String de conexão com o banco de dados #essa configuração está agora no arquivo 'config.py'
app.config.from_object('config') #o arquivo de configuração é setado aqui. Contém a string de conexão com o BD.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app) #cuida dos comandos ao inicializar a aplicação (runserver)
manager.add_command('db', MigrateCommand)

from App.controlers import default


#if __name__ == "main":
#    app.run() --> foi para o run.py
