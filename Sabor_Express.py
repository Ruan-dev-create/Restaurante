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
    input('\nPrecione ENTER para voltar ao menu principal')
    main()

def exibirOp():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair do app')

def encerrandoPrograma():
    os.system('cls')
    print('encerrando Programa... \n')


def op_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main() 


def exibir_subtitulo(texto):
    os.system('cls')
    print("\n", texto,"\n")



def cadastro_novo_restaurante():
    exibir_subtitulo('Cadastro de Novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_rest = {'Nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} 
    
    restaurantes.append(dados_do_rest)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')
    voltar_menu_princ()


def lista_restaurantes():
    exibir_subtitulo('Listagem de restaurantes cadastrados')
    for c in restaurantes:
        nome_rest = c['Nome']
        categoria = c['categoria']
        ativado = "Ativo" if c['ativo'] else 'Desativado'
        print(f' -> {nome_rest} | {categoria} | {ativado}')
    voltar_menu_princ()


def alterar_estado_rest():
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
    os.system('cls')
    exibirNomePrograma()
    exibirOp()
    escolherOp()


if __name__ == '__main__':
    main()
