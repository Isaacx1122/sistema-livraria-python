print('\n---Seja bem vindo! a livraria Central---')
lista_livros = []
id_global = 1
def cadastrar_livro(id):
    nome = input('Digite o nome do livro que deseja cadastrar: ')
    Autor = input('Digite o Autor do livro que deseja cadastrar: ')
    Editora = input('Digite a editora do livro que deseja cadastrar: ')
    livro = {'id': id , 'nome': nome, 'autor': Autor, 'editora': Editora}
    lista_livros.append(livro.copy())


def consultar_livro():
    if len(lista_livros) == 0:
        print('Ainda nao possui nenhum livro para consultar! ')
        print('-=' *20)
        return
    while True:
        print('1 - Consultar todos os livros!')
        print('2 - Consultar livros por ID! ')
        print('3 - Consultar livros pelo Autor!')
        print('4 - Sair')
        print('-=' *20)
        consultar = int(input('Qual opção você deseja? '))
        if consultar == 1:
            if len(lista_livros) == 0:
                print('Nenhum livro cadastrado até o momento! ')
                print('-=' * 20)
                return
            else:
                for livro in lista_livros:
                     print('-=' *20)
                     print(f'ID: {livro["id"]} | Nome: {livro["nome"]} | Autor: {livro["autor"]} | Editora: {livro["editora"]}')
                     print('-=' *20)
        elif consultar == 2:
            Id = int(input('Digite o ID do livro que você deseja buscar! '))
            for livro in lista_livros:
                if livro['id'] == Id:
                    print(f'ID: {livro["id"]} | Nome: {livro["nome"]} | Autor: {livro["autor"]} | Editora: {livro["editora"]}')
        elif consultar == 3:
            Autor = input('Digite o nome do autor do livro: ')
            for livro in lista_livros:
                if livro['autor'] == Autor:
                    print(f'ID: {livro["id"]} | Nome: {livro["nome"]} | Autor: {livro["autor"]} | Editora: {livro["editora"]}')
        elif consultar == 4:
            print('Saindo da livraria de Isaac! VOLTE SEMPRE!')
            return
        else:
            print('Digite uma das opções estabelecidas 1 , 2 , 3 ou 4')


def remover_livros():
    if len(lista_livros) == 0:
        print('Nenhum livro cadastrado até o momento!')
        return
    while True:
        Id_remover = int(input('Digite o ID do livro que deseja remover: '))
        for livro in lista_livros:
            if livro['id'] == Id_remover:
                lista_livros.remove(livro)
                print('Livro removido com sucesso!')
                return
        else:
            print('Digite um ID válido! ')
while True:
    print('---------MENU--------')
    print(' 1 - Cadastrar Livro:')
    print(' 2 - Consultar livro:')
    print(' 3 - Remover Livro:')
    print(' 4 - Encerrar Programa:')
    print('-=' *20)
    opção = int(input('Digite uma opção: '))
    if opção == 1:
        cadastrar_livro(id_global)
        id_global += 1
    elif opção == 2:
        consultar_livro()
    elif opção == 3:
        remover_livros()
    elif opção == 4:
        print('Encerrando o programa, volte sempre!')
        break
    else:
        print('Digite uma opção estabelecida 1 , 2 , 3 ou 4 ')
