from funcoes import *

opcao = perguntar ()

while True: #opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        inserir()
    elif opcao == 2:
        pesquisar()
    elif opcao ==  3:
        excluir()
    elif opcao == 4:
        listar()
    opcao = perguntar()