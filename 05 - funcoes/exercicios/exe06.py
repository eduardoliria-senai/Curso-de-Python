saldo = 1000.00

# defino a funcao de menu
def mostrar_menu():
    print("===== BANCO PYTHON ===== \n")

    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

# defino a funcao de consulta
def consultar_saldo(saldo):
    return f'Saldo atual: {saldo}'

# defino a funcao de deposito
def depositar(saldo):
    deposito = float(input("Quanto deseja depositar? "))
    print("Deposito realizado com sucesso!")
    return deposito + saldo

# defino a funcao de saque
def sacar(saldo):
    saque = float(input("Quando deseja sacar? "))

    if saque > saldo:
        print("Saldo insuficiente!") 
        return saldo

    print("Saque realizado com sucesso!")
    saldo = saldo - saque
    return saldo 

# while 
while True:
    mostrar_menu()

    opcao = int(input('Digite uma opcao acima: '))

    if opcao == 1:
        print(consultar_saldo(saldo))
    elif opcao == 2:
        saldo = depositar(saldo)
    elif opcao == 3:
        saldo = sacar(saldo)
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção invalida!")

print("Obrigado por utilizar o Banco Python!")