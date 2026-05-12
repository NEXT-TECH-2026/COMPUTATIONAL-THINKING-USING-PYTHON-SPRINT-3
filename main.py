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
    print('1 - CONSULTAR PONTOS E VOUCHERS')
    print('2 - GERAR VOUCHER')
    print('3 - VER HISTÓRICO DE CONVERSÕES')
    print('4 - VER IMPACTO AMBIENTAL')
    print('5 - SAIR')


def escolher_opcao():
    escolha = int(input('Escolha uma opção: '))

    match escolha:
        case 1:
            consultar_pontos()
        case 2:
            gerar_voucher()
        case 3:
            print('teste')
        case 4:
            print('teste')
        case 5:
            print('Finalizando o Soul Pass...')
            finalizar_app()
        case _:
            print('Digite uma Opção válida.')

def finalizar_app():
    print('Obrigado por utilizar o Soul Pass')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def main():
    os.system('cls')
    exibir_nome_soulpass()
    opcoes()
    escolher_opcao()

# Funcões Principais

def consultar_pontos():
    os.system('cls')
    exibir_nome_soulpass()

    print('CONSULTAR PONTOS E VOUCHERS\n')
    print(f'Pontos disponíveis: {pontos:.0f}')
    print(f'Vouchers disponíveis: {quantidade_vouchers}')

    voltar_ao_menu_principal()


def gerar_voucher():
    global pontos, quantidade_vouchers

    os.system('cls')
    exibir_nome_soulpass()

    print('GERAR VOUCHER\n')
    print('600 pontos = 1 voucher de R$ 5,52\n')
    print(f'Seu saldo atual: {pontos:.0f} pontos\n')

    # Verifica se o usuário tem pontos suficientes
    if pontos < 600:
        print('Você não possui pontos suficientes para gerar um voucher.')
        voltar_ao_menu_principal()
        return

    quantidade = int(input('Quantos vouchers deseja gerar?(Digite apenas números inteiros): '))

    if quantidade <= 0:
        print('Digite uma quantidade válida.')
        voltar_ao_menu_principal()
        return

    pontos_necessarios = quantidade * 600

    if pontos_necessarios > pontos:
        print('Você não possui pontos suficientes.')
        voltar_ao_menu_principal()
        return

    valor_total = quantidade * 5.52

    # Atualiza saldos
    pontos -= pontos_necessarios
    quantidade_vouchers += quantidade

    # Salva no histórico com dicionário
    conversao = {
        'pontos_utilizados': pontos_necessarios,
        'vouchers_gerados': quantidade,
        'valor_total': valor_total
    }

    historico.append(conversao)

    print('\nVoucher gerado com sucesso!')
    print(f'Quantidade de vouchers: {quantidade}')
    print(f'Valor total: R$ {valor_total:.2f}')
    print(f'Pontos restantes: {pontos:.0f}')

    voltar_ao_menu_principal()

# def mostrar_historico():

# def mostrar_impacto():


# Variáveis globais
pontos = float(input('Informe a quantidade de pontos: '))
quantidade_vouchers = 0
historico = []

# Chamada principal
main()
