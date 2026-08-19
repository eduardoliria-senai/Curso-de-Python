# Crie uma funcao par ou impar que receber um numero 
# e retorne se o numero e par ou impar 
# pergunte ao usuario o numero.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

valor = int(input('Digite um valor: '))
print(par_ou_impar(valor))