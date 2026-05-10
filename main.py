import os

def exibir_nome_soulpass():
    print(r"""
  ____              _   ____               
 / ___|  ___  _   _| | |  _ \ __ _ ___ ___ 
 \___ \ / _ \| | | | | | |_) / _` / __/ __|
  ___) | (_) | |_| | | |  __/ (_| \__ \__ \
 |____/ \___/ \__,_|_| |_|   \__,_|___/___/
                                           
""")


# Funções de Navegação
def opcoes():
    print('1 - CONSULTAR SALDO DE PONTOS')
    print('2 - CONSULTAR PONTOS EM CRÉDITOS')
    print('3 - GERAR VOUCHER')
    print('4 - VER HISTÓRICO DE CONVERSÕES')
    print('5 - VER IMPACTO AMBIENTAL')
    print('6 - SAIR')


def escolher_opcao():
    escolha = int(input('Escolha uma opção: '))

    match escolha:
        case 1:
            print('teste')
        case 2:
            print('teste')
        case 3:
            print('teste')
        case 4:
            print('teste')
        case 5:
            print('teste')
        case 6:
            print('Finalizando o Soul Pass...')
            finalizar_app()
        case _:
            print('Digite uma Opção válida.')

def finalizar_app():
    print('Obrigado por utilizar o Soul Pass')

def main():
    os.system('cls')
    exibir_nome_soulpass()
    opcoes()
    escolher_opcao()

# Funcões Principais

# def consultar_pontos():

# def converter_pontos():

# def gerar_pontos():

# def mostrar_historico():

# def mostrar_impacto():


# Variáveis globais
pontos = float(input('Informe a quantidade de pontos: '))
saldo_credito = 0
historico = []

# Chamada principal
main()
