#from App import app
from App import manager

# segurança --> verifica se o usuario está executando o arquivo principal e não um secundário da app.
# flask só vai dar o run se esse for o arquivo Principal
if __name__ == "__main__":
    #app.run()
    manager.run()