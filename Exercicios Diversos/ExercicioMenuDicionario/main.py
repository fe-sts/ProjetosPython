from funcoes import *

#usuarios = {}
opcao = perguntar ()

while True: #opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        #print("opcao 11")
        inserir()
        print(usuarios)
        pass
    elif opcao == 2:
        pesquisar()
    elif opcao ==  3:
        excluir()
    elif opcao == 4:
        listar()
    opcao = perguntar()