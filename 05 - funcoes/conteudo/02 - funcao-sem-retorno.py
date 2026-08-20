# Sem funcao
# print("=====================")
# print("OLA MUNDO")
# print("=====================")
# print("Eu me chamo Eduardo")
# print("=====================")

# # COM funcao 
# def separador():
#     print("=====================")
    
# print("OLA MUNDO")
# separador()
# print("Eu me chamo Eduardo")
# separador()

# EXEMPLO 
def menu():
    print('1 - Falar com atendente')
    print('2 - Trocar a musica')
    print('3 - Mudar de plano')
    print('4 - Para sair')

def melhoria(opcao):
    if opcao == 1:
        print('Falando com atendente...')
        return True
    elif opcao == 2: 
        print("Trocando de musica...")
        return True
    elif opcao == 3:
        print('Mudando de planos...')
        return True
    elif opcao == 4:
         print("Saindo...")
         return False
    else:
       print("Opcao invalida")

    
while True:
    menu()
    opcao = int(input('Digite uma opcao acima: '))
    
    variavel = melhoria(opcao) # False
    
    if variavel == False:
        break
    
    
    
    