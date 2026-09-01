import os
from datetime import datetime, date

def exibir_nome_soulpass():
    print(r"""
  ____              _   ____               
 / ___|  ___  _   _| | |  _ \ __ _ ___ ___ 
 \___ \ / _ \| | | | | | |_) / _` / __/ __|
  ___) | (_) | |_| | | |  __/ (_| \__ \__ \
 |____/ \___/ \__,_|_| |_|   \__,_|___/___/
                                           
""")

def main():
    os.system('cls')
    exibir_nome_soulpass()
    opcoes()
    escolher_opcao()


# Funções de Navegação
def opcoes():
    print('1 - CONSULTAR PONTOS E VOUCHERS')
    print('2 - GERAR VOUCHER')
    print('3 - VER HISTÓRICO DE CONVERSÕES')
    print('4 - VER IMPACTO AMBIENTAL')
    print('5 - Cadastrar outra conta')
    print('6 - Alterar dados cadastrais')
    print('7 - Excluir conta')
    print('8 - SAIR')


def escolher_opcao():
    try:
        escolha = int(input('Escolha uma opção: '))
    except:
        print("Digite um número válido!")

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
        case 6:
            cpf = input("Digite seu cpf: ")
            indice = buscar_cliente(lista_clientes, cpf)
            if (indice != -1):
                alterar_cliente(lista_clientes, indice)
            else:
                print("CPF não encontrado.")
        case 7:
            excluir_cliente(lista_clientes, indice)        
        case 8:
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

def mostrar_historico():
    os.system('cls')
    exibir_nome_soulpass()

    print('HISTÓRICO DE CONVERSÕES\n')
    
    if len(historico) == 0:
        print('Nenhuma conversão foi realizada.')
    else:
        for conversao in historico:
            print(f"\nPONTOS UTILIZADOS: {conversao['pontos_utilizados']}")
            print(f"VOUCHERS GERADOS: {conversao['vouchers_gerados']}")
            print(f"VALOR TOTAL: {conversao['valor_total']}")
            print('\n============================================\n')
    
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
            print("Você precisa ter no mínimo 18 anos para realizar o cadastro!")
            return
        # while(idade < 18):
        #     print("Você precisa ter no mínimo 18 anos para realizar o cadastro!")
        #     data_digitada = input("Digite a sua data de nascimento: ")
        #     data_nascimento = datetime.strptime(data_digitada, "%d/%m/%Y").date()
        #     idade = calcular_idade(data_nascimento)
    except ValueError:
        print("O CPF e data de nascimento devem ser escritos com números!!!")
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
        print("O cadastro foi finalizado! Agora você pode acessar a nossa plataforma com a sua conta!")

def alterar_cliente(lista_clientes, indice):
        #Resgatando novos valores
        print(f"O nome do cliente é: {lista_clientes[indice]['Nome']}")
        novo_nome = input("Digite o novo nome do cliente: ")
        print(f"O email do cliente é: {lista_clientes[indice]['Email']}")
        novo_email = input("Digite o novo email do cliente: ")
        print(f"A senha do cliente é: {lista_clientes[indice]['Senha']}")
        nova_senha = input("Digite a nova senha do cliente: ")
        indice_senha = validar_senha(lista_clientes, nova_senha)
        while(indice_senha != -1):
            nova_senha = input("A senha informada já existe, digite uma senha que não está em uso: ")
            indice_senha = validar_senha(lista_clientes, nova_senha)

        #Alterando os dados
        lista_clientes[indice]['Nome'] = novo_nome
        lista_clientes[indice]['Email'] = novo_email
        lista_clientes[indice]['Senha'] = nova_senha
        print("Dados alterados com sucesso!")

def excluir_cliente(lista_clientes, indice):
    lista_clientes.pop(indice)
    print("Cliente excluído!")


# Variáveis globais
pontos = float(input('Informe a quantidade de pontos: '))
quantidade_vouchers = 0
historico = []
lista_clientes = []

opcao_cadastro = 0

while (opcao_cadastro != 3):
    print("*****ENTRE NA SUA CONTA*****")
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
                        main()
                        break
                    else:
                        print(f"Usuário ou senha incorretos. Tente novamente, você ainda tem mais {2-i} tentativa(s)")
            case 2:
                cadastrar_cliente(lista_clientes)
    else:
        print("Opção inválida. Tente novamente!")
