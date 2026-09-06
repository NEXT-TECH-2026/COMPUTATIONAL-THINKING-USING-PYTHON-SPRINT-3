import os
import sys
from datetime import datetime, date
import json


def exibir_nome_soulpass():
    print(r"""
  ____              _   ____               
 / ___|  ___  _   _| | |  _ \ __ _ ___ ___ 
 \___ \ / _ \| | | | | | |_) / _` / __/ __|
  ___) | (_) | |_| | | |  __/ (_| \__ \__ \
 |____/ \___/ \__,_|_| |_|   \__,_|___/___/
                                           
""")

# <<< ALTERAÇÃO DE LAYOUT >>> Nova função para padronizar as mensagens de aviso
def exibir_aviso(*linhas, largura=60):
    print("\n" + "═" * largura)
    for linha in linhas:
        print(f" {linha}")
    print("═" * largura + "\n")


def main():
    os.system('cls')
    exibir_nome_soulpass()
    opcoes()
    escolher_opcao()


# Funções de Navegação
def opcoes():
    print('1 - CONSULTAR PONTOS E VOUCHERS DISPONÍVEIS')
    print('2 - GERAR VOUCHER')
    print('3 - VER HISTÓRICO DE CONVERSÕES')
    print('4 - VER IMPACTO AMBIENTAL')
    print('5 - CADASTRAR OUTRA CONTA')
    print('6 - ALTERAR DADOS CADASTRAIS')
    print('7 - EXCLUIR CONTA')
    print('8 - GERAR RELATÓRIO DE VOUCHERS')
    print('9 - IMPRIMIR NOTA FISCAL DAS CONVERSÕES')
    print('10 - EXPORTAR DADOS PARA JSON')
    print('11 - IMPORTAR DADOS DO JSON')
    print('12 - SAIR')


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
            mostrar_impacto()
        case 5:
            cadastrar_cliente(lista_clientes)
            opcao_cadastro = 0
            validarCadastro(opcao_cadastro)
            main()
        case 6:
            cpf = input("Digite seu cpf: ")
            indice = buscar_cliente(lista_clientes, cpf)
            while(indice == -1):
                cpf = input("CPF não encontrado, digite um número válido: ")
                indice = buscar_cliente(lista_clientes, cpf)
            alterar_cliente(lista_clientes, indice)
            voltar_ao_menu_principal()              
        case 7:
            cpf = input("Digite seu cpf: ")
            indice = buscar_cliente(lista_clientes, cpf)
            confirmar_exclusao = int(input("Deseja realmente excluir sua conta (1 - Sim / 2 - Não): "))
            if (confirmar_exclusao == 1):
                excluir_cliente(lista_clientes, indice)
                opcao_cadastro = 0
                validarCadastro(opcao_cadastro)
            elif (confirmar_exclusao == 2):
                exibir_aviso("Exclusão não realizada!")  # <<< ALTERAÇÃO DE LAYOUT >>>
                voltar_ao_menu_principal()
            else:
                exibir_aviso("Opção inválida!")  # <<< ALTERAÇÃO DE LAYOUT >>>
                voltar_ao_menu_principal()
        case 8:
            gerar_relatorio()

        case 9:
            gerar_arquivo_txt()

        case 10:
            exportar_json()

        case 11:
            importar_json()

        case 12:
            print('\nFinalizando o Soul Pass...')
            finalizar_app()

        case _:
            exibir_aviso("Opção inválida! Digite um número correspondente a uma opção do menu.")  # <<< ALTERAÇÃO DE LAYOUT >>>
            voltar_ao_menu_principal()


def finalizar_app():
    exibir_aviso("Obrigado por utilizar o Soul Pass!")  # <<< ALTERAÇÃO DE LAYOUT >>>
    sys.exit()


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Funcões Principais

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
        exibir_aviso("Você não possui pontos suficientes para gerar um voucher.")  # <<< ALTERAÇÃO DE LAYOUT >>>
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
        exibir_aviso("Digite uma quantidade válida.")  # <<< ALTERAÇÃO DE LAYOUT >>>
        voltar_ao_menu_principal()
        return

    pontos_necessarios = quantidade * 600

    if pontos_necessarios > pontos:
        exibir_aviso("Você não possui pontos suficientes.")  # <<< ALTERAÇÃO DE LAYOUT >>>
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

    # <<< ALTERAÇÃO DE LAYOUT >>> Bloco de sucesso agrupado em um único aviso
    exibir_aviso(
        "Voucher gerado com sucesso!",
        f"Quantidade de vouchers: {quantidade}",
        f"Valor total: R$ {valor_total:.2f}",
        f"Pontos restantes: {pontos:.0f}"
    )

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
    arquivo.write('             NOTA FISCAL\n')
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

    print('Nota fiscal gerada com sucesso!')
    print('Consulte no arquivo: relatorio_vouchers.txt')

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
        exibir_aviso("Nenhuma conversão foi realizada.")  # <<< ALTERAÇÃO DE LAYOUT >>>
    else:
        for conversao in historico:
            # <<< ALTERAÇÃO DE LAYOUT >>> Trocado o separador "====" por exibir_aviso
            exibir_aviso(
                f"PONTOS UTILIZADOS: {conversao['pontos_utilizados']}",
                f"VOUCHERS GERADOS: {conversao['vouchers_gerados']}",
                f"VALOR TOTAL: {conversao['valor_total']}"
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

#CRUD PARA CRIAR A CONTA DO CLIENTE
def buscar_cliente(lista_clientes, cpf):
    indice = -1
    for i in range(len(lista_clientes)):
        if (cpf == lista_clientes[i]['CPF']):
            indice = i
            break
    return indice

def validar_usuario(lista_clientes, usuario):
    indice_usuario = -1
    for i in range(len(lista_clientes)):
        if (usuario == lista_clientes[i]['Usuário']):
            indice_usuario = i
            break
    return indice_usuario

def validar_senha(lista_clientes, senha):
    indice_senha = -1
    for i in range(len(lista_clientes)):
        if (senha == lista_clientes[i]['Senha']):
            indice_senha = i
            break
    return indice_senha

def calcular_idade(data_nascimento: date):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

def cadastrar_cliente(lista_clientes):
    try:
        cpf = input("Digite o seu CPF para iniciar o seu cadastro: ")
        indice = buscar_cliente(lista_clientes, cpf)
        while(indice != -1):
            cpf = input("O CPF informado já está associado a uma conta. Para iniciar o cadastro, informe um CPF que ainda não foi cadastrado:")
            indice = buscar_cliente(lista_clientes, cpf)
        id = len(lista_clientes)
        nome = input("Digite o seu nome: ")
        email = input("Digite o seu email: ")
        usuario = input("Digite o nome de usuario que deseja criar: ")
        indice_usuario = validar_usuario(lista_clientes, usuario)
        while(indice_usuario != -1):
            usuario = input("O nome de usuário informado já existe, digite um nome de usuário que não está em uso: ")
            indice_usuario = validar_usuario(lista_clientes, usuario)
        senha = input("Digite a senha que deseja criar: ")
        indice_senha = validar_senha(lista_clientes, senha)
        while(indice_senha != -1):
            senha = input("A senha informada já existe, digite uma senha que não está em uso: ")
            indice_senha = validar_senha(lista_clientes, senha)
        data_digitada = input("Digite a sua data de nascimento (dd/mm/aaaa): ")
        data_nascimento = datetime.strptime(data_digitada, "%d/%m/%Y").date()
        idade = calcular_idade(data_nascimento) 
        if(idade < 18):
            # <<< ALTERAÇÃO DE LAYOUT >>> Trocado o bloco de "-----" por exibir_aviso
            exibir_aviso("Você precisa ter no mínimo 18 anos para realizar o cadastro.")
            return
        # while(idade < 18):
        #     print("Você precisa ter no mínimo 18 anos para realizar o cadastro!")
        #     data_digitada = input("Digite a sua data de nascimento: ")
        #     data_nascimento = datetime.strptime(data_digitada, "%d/%m/%Y").date()
        #     idade = calcular_idade(data_nascimento)
    except ValueError:
        # <<< ALTERAÇÃO DE LAYOUT >>>
        exibir_aviso("Data de nascimento inválida ou não foi escrita no formato dd/mm/aaaa.", "Tente novamente!", largura=80)
    else:
        dados_cliente = {
            'id': id,
            'Nome': nome,
            'Email': email,
            'Usuário': usuario,
            'Senha': senha,
            'Idade': idade,
            'CPF': cpf
        }
        lista_clientes.append(dados_cliente)
        # <<< ALTERAÇÃO DE LAYOUT >>>
        exibir_aviso("Cadastro finalizado com sucesso!", "Agora você pode acessar a nossa plataforma com a sua conta!")

def alterar_cliente(lista_clientes, indice):
        #Resgatando novos valores
        print(f"O seu nome é: {lista_clientes[indice]['Nome']}")
        novo_nome = input("Digite um novo nome: ")
        print(f"O seu email é: {lista_clientes[indice]['Email']}")
        novo_email = input("Digite um novo email: ")
        senha = lista_clientes[indice]['Senha']
        confirmacao_senha = input("Confirme sua senha para alterá-la: ")
        while(confirmacao_senha != senha):
            confirmacao_senha = input(("Senha incorreta! Tente novamente: "))
        nova_senha = input("Digite sua nova senha: ")
        indice_senha = validar_senha(lista_clientes, nova_senha)
        while(indice_senha != -1):
            nova_senha = input("A senha informada já existe, digite uma senha que não está em uso: ")
            indice_senha = validar_senha(lista_clientes, nova_senha)

        #Alterando os dados
        lista_clientes[indice]['Nome'] = novo_nome
        lista_clientes[indice]['Email'] = novo_email
        lista_clientes[indice]['Senha'] = nova_senha
        exibir_aviso("Dados alterados com sucesso!")  # <<< ALTERAÇÃO DE LAYOUT >>>

def excluir_cliente(lista_clientes, indice):
    lista_clientes.pop(indice)
    exibir_aviso("Conta excluída com sucesso!")  # <<< ALTERAÇÃO DE LAYOUT >>> (era o exemplo que você mandou)

lista_clientes = []
opcao_cadastro = 0

def validarCadastro(opcao_cadastro):
    while (opcao_cadastro != 3):
        exibir_nome_soulpass()
        print("-----CADASTRO DE CONTA-----\n")
        print("1 - Já sou cadastrado!")
        print("2 - Ainda não sou cadastrado")
        print("3 - Sair")
        opcao_cadastro = int(input("Digite a opção correspondente: "))
        if (opcao_cadastro >= 1 and opcao_cadastro <= 3):
            match opcao_cadastro:
                case 1:
                    for i in range (3):
                        usuario = input("Informe seu usuário: ")
                        indice_usuario = validar_usuario(lista_clientes, usuario)
                        senha = input("Digite a senha: ")
                        indice_senha = validar_senha(lista_clientes, senha)

                        if (indice_usuario != -1 and indice_usuario == indice_senha):
                            os.system('cls')
                            return 3
                        else:
                            # <<< ALTERAÇÃO DE LAYOUT >>>
                            exibir_aviso("Usuário ou senha incorretos.", f"Você ainda tem mais {2-i} tentativa(s).")
                case 2:
                    cadastrar_cliente(lista_clientes)
                case 3:
                    print("Saindo...")
                    finalizar_app()
        else:
            exibir_aviso("Opção inválida. Tente novamente!")  # <<< ALTERAÇÃO DE LAYOUT >>>


# Variáveis globais
validarCadastro(opcao_cadastro)
pontos = float(input('Informe a quantidade de pontos: '))
quantidade_vouchers = 0
historico = []
main()