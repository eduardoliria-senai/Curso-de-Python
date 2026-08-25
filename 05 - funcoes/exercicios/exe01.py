# Pedir ao usario dois numeros e com esse numeros 
# calcular a soma, subtracao, divisao, multplicacao
# e tambem pedir ao usuario um nome para sauda-lo
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
nome = input('Qual seu nome? ')

# crio as funcoes 
def somar(numero1, numero2):
    return numero1 + numero2

def sub(numero1, numero2):
    return numero1 - numero2

def div(numero1, numero2):
    return numero1 / numero2

def multi(numero1, numero2):
    return numero1 * numero2

def saudacao(nome):
    return f'Ola seja bem-vindo(a) {nome}'

# Guardando os retornos das funcoes nas variaveis
soma = somar(valor1, valor2)
subtracao = sub(valor1, valor2)
divisao = div(valor1, valor2)
multiplicacao = multi(valor1,valor2)
saudar = saudacao(nome)

# mostrar as mensagens
print(f'A soma dos valores foi de: {soma}')
print(f'A subtracao dos valores foi de: {subtracao}')
print(f'A divisao dos valores foi de: {divisao}')
print(f'A multiplicacao dos valores foi de: {multiplicacao}')
print(saudar)

