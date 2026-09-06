import os
import json


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
    print('1 - CONSULTAR PONTOS E VOUCHERS DISPONÍVEIS')
    print('2 - GERAR VOUCHER')
    print('3 - VER HISTÓRICO DE CONVERSÕES')
    print('4 - GERAR RELATÓRIO DE VOUCHERS')
    print('5 - GERAR ARQUIVO TXT')
    print('6 - EXPORTAR DADOS PARA JSON')
    print('7 - IMPORTAR DADOS DO JSON')
    print('8 - VER IMPACTO AMBIENTAL')
    print('9 - SAIR')


def escolher_opcao():
    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError:
        print("Digite um número válido!")
        voltar_ao_menu_principal()
        return

    match escolha:
        case 1:
            consultar_pontos()

        case 2:
            gerar_voucher()

        case 3:
            mostrar_historico()

        case 4:
            gerar_relatorio()

        case 5:
            gerar_arquivo_txt()

        case 6:
            exportar_json()

        case 7:
            importar_json()

        case 8:
            mostrar_impacto()

        case 9:
            print('\nFinalizando o Soul Pass...')
            finalizar_app()

        case _:
            print('Digite uma Opção válida.')
            voltar_ao_menu_principal()


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


# Funções Principais

def consultar_pontos():
    os.system('cls')
    exibir_nome_soulpass()

    print('CONSULTAR PONTOS E VOUCHERS DISPONÍVEIS\n')
    print(f'Pontos disponíveis: {pontos:.0f}')
    print(f'Vouchers disponíveis: {quantidade_vouchers}')

    voltar_ao_menu_principal()


def gerar_voucher():
    global pontos, quantidade_vouchers

    os.system('cls')
    exibir_nome_soulpass()

    print('GERAR VOUCHER\n')
    print('600 pontos = 1 voucher no valor de R$ 5,52\n')
    print(f'Seu saldo atual: {pontos:.0f} pontos\n')

    # Verifica se o usuário tem pontos suficientes
    if pontos < 600:
        print('Você não possui pontos suficientes para gerar um voucher.')
        voltar_ao_menu_principal()
        return

    try:
        quantidade = int(
            input(
                'Quantos vouchers deseja gerar?'
                '(Digite apenas números inteiros): '
            )
        )
    except ValueError:
        print('Digite apenas números inteiros.')
        voltar_ao_menu_principal()
        return

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


# RELATÓRIO
def gerar_relatorio():
    os.system('cls')
    exibir_nome_soulpass()

    print('RELATÓRIO DE VOUCHERS\n')

    if len(historico) == 0:
        print('Nenhuma conversão foi realizada por aqui.')
    else:
        contador = 1

        for conversao in historico:
            print(f'\nCONVERSÃO {contador}')
            print(
                f"PONTOS UTILIZADOS: "
                f"{conversao['pontos_utilizados']}"
            )
            print(
                f"VOUCHERS GERADOS: "
                f"{conversao['vouchers_gerados']}"
            )
            print(
                f"VALOR TOTAL: "
                f"R$ {conversao['valor_total']:.2f}"
            )
            print('============================================')

            contador += 1

    voltar_ao_menu_principal()


# GERAR ARQUIVO TXT
def gerar_arquivo_txt():
    os.system('cls')
    exibir_nome_soulpass()

    print('GERAR ARQUIVO TXT\n')

    if not historico:
        print('Nenhuma conversão foi realizada por aqui.')
        voltar_ao_menu_principal()
        return

    arquivo = open(
        'relatorio_vouchers.txt',
        'w',
        encoding='utf-8'
    )

    arquivo.write('============================================\n')
    arquivo.write('              SOUL PASS\n')
    arquivo.write('        RELATÓRIO DE VOUCHERS\n')
    arquivo.write('============================================\n\n')

    contador = 1

    for conversao in historico:
        arquivo.write(f'CONVERSÃO {contador}\n')
        arquivo.write(
            f"Pontos utilizados: "
            f"{conversao['pontos_utilizados']}\n"
        )
        arquivo.write(
            f"Vouchers gerados: "
            f"{conversao['vouchers_gerados']}\n"
        )
        arquivo.write(
            f"Valor total: "
            f"R$ {conversao['valor_total']:.2f}\n"
        )
        arquivo.write(
            '--------------------------------------------\n'
        )

        contador += 1

    arquivo.close()

    print('Arquivo TXT criado com sucesso!')
    print('Nome do arquivo: relatorio_vouchers.txt')

    voltar_ao_menu_principal()


# EXPORTAR JSON
def exportar_json():
    os.system('cls')
    exibir_nome_soulpass()

    print('EXPORTAR DADOS PARA JSON\n')

    if len(historico) == 0:
        print('Nenhuma conversão foi realizada por aqui.')
        voltar_ao_menu_principal()
        return

    arquivo = open(
        'historico_vouchers.json',
        'w',
        encoding='utf-8'
    )

    json.dump(
        historico,
        arquivo,
        ensure_ascii=False,
        indent=4
    )

    arquivo.close()

    print('Dados exportados com sucesso!')
    print('Nome do arquivo: historico_vouchers.json')

    voltar_ao_menu_principal()


# IMPORTAR JSON
def importar_json():
    global historico, quantidade_vouchers

    os.system('cls')
    exibir_nome_soulpass()

    print('IMPORTAR DADOS DO JSON\n')

    try:
        arquivo = open(
            'historico_vouchers.json',
            'r',
            encoding='utf-8'
        )

        historico = json.load(arquivo)

        arquivo.close()

        # Recalcula a quantidade total de vouchers
        quantidade_vouchers = 0

        for conversao in historico:
            quantidade_vouchers += conversao['vouchers_gerados']

        print('Dados importados com sucesso!')
        print(
            f'Total de conversões importadas: '
            f'{len(historico)}'
        )
        print(
            f'Total de vouchers importados: '
            f'{quantidade_vouchers}'
        )

    except FileNotFoundError:
        print(
            'Arquivo historico_vouchers.json '
            'não encontrado.'
        )

    except json.JSONDecodeError:
        print(
            'Erro! O arquivo JSON está inválido.'
        )

    voltar_ao_menu_principal()


def mostrar_historico():
    os.system('cls')
    exibir_nome_soulpass()

    print('HISTÓRICO DE CONVERSÕES\n')

    if len(historico) == 0:
        print('Nenhuma conversão foi realizada por aqui.')
    else:
        for conversao in historico:
            print(
                f"\nPONTOS UTILIZADOS: "
                f"{conversao['pontos_utilizados']}"
            )
            print(
                f"VOUCHERS GERADOS: "
                f"{conversao['vouchers_gerados']}"
            )
            print(
                f"VALOR TOTAL: "
                f"R$ {conversao['valor_total']:.2f}"
            )
            print(
                '\n============================================\n'
            )

    voltar_ao_menu_principal()


def mostrar_impacto():
    os.system('cls')
    exibir_nome_soulpass()

    print('IMPACTO AMBIENTAL\n')

    total_vouchers = 0

    for conversao in historico:
        total_vouchers += conversao['vouchers_gerados']

    co2_evitado = total_vouchers * 1.2

    print(f'Total de vouchers gerados: {total_vouchers}')
    print(f'CO₂ evitado estimado: {co2_evitado:.2f} kg')

    voltar_ao_menu_principal()


# Variáveis globais
pontos = float(input('Informe a quantidade de pontos: '))
quantidade_vouchers = 0
historico = []


# Chamada principal
main()
