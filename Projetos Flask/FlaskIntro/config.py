DEBUG = True #sempre que fizer uma alteração nos arquivos e Salvar, não precisa reiniciar o servidor. Ele já atualiza automaticamente

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True #para suprimir o aleta de erro