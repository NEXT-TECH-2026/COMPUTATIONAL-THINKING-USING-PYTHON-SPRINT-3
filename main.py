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
            mostrar_historico()
        case 4:
            mostrar_impacto()
        case 5:
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
    return indice

def validar_usuario_senha(lista_clientes, usuario, senha):
    indice = -1
    for i in range(len(lista_clientes)):
        if (usuario == lista_clientes[i]['Usuário'] or senha == lista_clientes[i]['Senha']):
            indice = i
    return indice

def cadastrar_cliente(lista_clientes):
    try:
        cpf = int(input("Digite o seu CPF para iniciar o seu cadastro: "))
        indice = buscar_cliente(lista_clientes, cpf)
        while(indice != -1):
            cpf = int(input("O CPF informado já está associado a uma conta. Para iniciar o cadastro, é necessário informar um CPF que ainda não foi cadastrado."))
            indice = buscar_cliente(lista_clientes, cpf)
        id += 1
        nome = input("Digite o seu nome: ")
        usuario = input("Digite o nome de usuario que deseja criar: ")
        senha = input("Digite a senha que deseja criar: ")
        indice = validar_usuario_senha(lista_clientes, usuario, senha)
        while(indice != -1):
            print("O nome de usuário ou a senha informada já existe!")
            usuario = input("Digite o nome de usuario que deseja criar: ")
            senha = input("Digite a senha que deseja criar: ")
            validar_usuario_senha(lista_clientes, usuario, senha)
        idade = int(input("Digite a sua idade: "))
    except ValueError:
        print("Os dados de idade e CPF devem ser escritos com números!!!")
    else:
        dados_cliente = {
            'id': id,
            'Nome': nome,
            'Usuário': usuario,
            'Senha': senha,
            'Idade': idade,
            'CPF': cpf
        }
        lista_clientes.append(dados_cliente)
        print("O cadastro foi finalizado! Agora você pode acessar a nossa plataforma com a sua conta!")

# def alterar_cliente(lista_clientes, cpf):
#     try:
#         print(f"O nome do cliente é: {lista_clientes[cpf]['Nome']}")
#         novo_nome = input("Digite o novo nome do cliente: ")
#         print(f"O usuário")
#     except ValueError:


# Variáveis globais
# pontos = float(input('Informe a quantidade de pontos: '))
quantidade_vouchers = 0
historico = []
lista_clientes = []
cpf = int(input("O CPF informado já está associado a uma conta. Para iniciar o cadastro, é necessário informar um CPF que ainda não foi cadastrado."))

# Chamada principal
main()
