from cliente import Cliente
from conta import Conta

print('Vamos cadastrar sua conta no nosso Banco!')
nome_cliente = input('Digite seu nome: ')
cpf_cliente = input('Digite seu cpf: ')
idade_cliente = float(input('Digite sua idade: '))
cliente1 = Cliente(nome_cliente, cpf_cliente, idade_cliente)

print('Seus dados')
print(cliente1)

'''
conta_do_alan = Conta(cliente1, 00.00, 1000)

print('Cliente:',conta_do_alan.cliente.nome, '\nSaldo:',conta_do_alan.consulta_saldo())

quero_depositar = float(input('Digite seu depósito: '))
conta_do_alan.depositar(quero_depositar)

print('Saldo atual: ', conta_do_alan.consulta_saldo())

quero_sacar = float(input('Digite a quantidade que quer sacar: '))
conta_do_alan.sacar(quero_sacar)

print(conta_do_alan.consulta_saldo())
'''

conta_do_alan = Conta(cliente1, 00.00, 1000)

num = 0
while (num != 5):
    print("\n[MENU]")
    print('1 - Consultar Nome e Saldo')
    print('2 - Consultar Cadastro')
    print('3 - Fazer depósito na conta')
    print('4 - Fazer um saque')
    print('5 - Sair do programa')
    num = int(input('Digite a opção desejada: '))

    if num == 1:
        print('Cliente:',conta_do_alan.cliente.nome, '\nSaldo:',conta_do_alan.consulta_saldo())
    
    elif num == 2:
        print(cliente1)

    elif num == 3:
        print('Saldo atual: ', conta_do_alan.consulta_saldo())
        quero_depositar = float(input('Digite seu depósito: '))
        conta_do_alan.depositar(quero_depositar)
        print('Saldo atual: ', conta_do_alan.consulta_saldo())
    
    elif num == 4:
        print(conta_do_alan.consulta_saldo())
        quero_sacar = float(input('Digite a quantidade que quer sacar: '))
        conta_do_alan.sacar(quero_sacar)
        print(conta_do_alan.consulta_saldo())

    elif num == 5:
        print('Programada finalizado...')
