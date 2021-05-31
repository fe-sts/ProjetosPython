usuarios = {}

def perguntar():
    return int(input("O que deseja realizar?\n" +
                 "1 - Inserir usuário\n" +
                 "2 - Pesquisar usuário\n" +
                 "3 - Excluir usuário\n" +
                 "4 - Listar usuário: "))


# não precisa do retorno, pq é a memória
def inserir():
    nome = str(input('Digite o nome do contato: ').strip().upper())
    telefone = int(input('Digite telefone: ').strip())
    if usuarios.get(nome):
        print("Ja existe este contato")
    else:
        usuarios[nome] = telefone #Para trabalhar com dicionarios, deve se usar o sistema Chave (nome), Valor(telefone)
 
def pesquisar():
    nome = input("Digite o usuario que deseja buscar: ").upper()
    if usuarios.get(nome):
        print(usuarios.get(nome))    

def listar():
    for nome, telefone in usuarios.items():
        print(nome +": "+str(telefone))

def excluir():
    for nome, telefone in usuarios.items():
        print(nome +": "+str(telefone))
    nome_exc = input("Digite o login que deseja excluir: ").upper()
    del usuarios[nome_exc]
    print(f"Usuario, {nome_exc} removido com sucesso!")