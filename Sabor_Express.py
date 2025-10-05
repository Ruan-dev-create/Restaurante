import os

#Data 03/10/2025

restaurantes = [{'Nome': "Mc Donalds",'categoria':'Brasil', 'ativo':False}, 
                {'Nome':'Pizza Supremaa', 'categoria':'Italiana', 'ativo':True},
                {'Nome':'Cantina', 'categoria':'Chines', 'ativo':False}]

def exibirNomePrograma():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")


def voltar_menu_princ():
    '''

    -> Essa funcão ela é responsável por voltar ao menu do aplicativo precionando a tecla ENTER

    '''
    input('\nPrecione ENTER para voltar ao menu principal')
    main()


def exibirOp():
    '''

    -> Essa função ela é responsável por mostrar todas as opções do usuário
    
    '''

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair do app')


def encerrandoPrograma():
    '''

    -> Essa função ela é responsável por encerrar o programa
    
    '''
    
    os.system('cls')
    print('encerrando Programa... \n')


def op_invalida():
    '''

    -> Essa função ela é responsável por não poluir a tela de erros, somente mostra uma mensagem de erro
    
    '''
    
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main() 


def exibir_subtitulo(texto):
    '''
    -> Essa função ela é responsável por deixar o código mais legivel,
      mostrando títulos para o usuário não se perca no aplicativo
    '''

    os.system('cls')
    linha = '-' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print('\n')


def cadastro_novo_restaurante():
    '''
    
    -> Essa função é responsável por cadastrar um novo restaurante.
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
     
    '''

    exibir_subtitulo('Cadastro de Novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_rest = {'Nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} 
    
    restaurantes.append(dados_do_rest)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')
    voltar_menu_princ()


def lista_restaurantes():
    '''
    
    -> Essa função é responsável por listar todos os restaurantes cadastrados no aplicativo.
    
    Prints:
    - Nome do restaurante
    - Categoria do restaurante
    - Status do restaurante

    '''

    exibir_subtitulo('Listagem de restaurantes cadastrados')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
    print('-' * 60)
    for c in restaurantes:
        nome_rest = c['Nome']
        categoria = c['categoria']
        ativado = "Ativo" if c['ativo'] else 'Desativado'
        print(f' -> {nome_rest.ljust(20)} | {categoria.ljust(20)} | {ativado}')
    voltar_menu_princ()


def alterar_estado_rest():
    '''

    -> Essa função é responsável por alterar o status do restaurante, ativar e desastivar.

    Inputs:
    - Nome do restaurante que deseja ativar ou desativar

    '''
    
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_rest = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_rest == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_rest} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_rest} foi desativado com sucesso!'
            print(mensagem)
    voltar_menu_princ()

def escolherOp():
    '''
    -> Essa função é responsável por ir no caminho de onde o usuário digitar dependendo da escolha do usuário
    '''
    
    try:
        escolha = int(input('\nEscolha uma opção: '))
        print(f'Você escolheu a opção {escolha}.')

        if escolha == 1:
            cadastro_novo_restaurante()
        elif escolha == 2:
            lista_restaurantes()
        elif escolha == 3:
            alterar_estado_rest()
        elif escolha == 4:
            encerrandoPrograma()
        else:
            op_invalida()
    except:
        op_invalida()
        

def main():
    '''
    -> Essa função é responsável por mandar o usuário á tela inicial do programa
    '''

    os.system('cls')
    exibirNomePrograma()
    exibirOp()
    escolherOp()


if __name__ == '__main__':
    '''
    -> Essa função é a que define o código como o PRINCIPAL do programa
    '''

    main()
