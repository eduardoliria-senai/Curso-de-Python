# 96) Crie um programa que tenha uma função Media(), que vai receber as 3 notas de 
# um aluno e retornar a sua média para o programa principal
def media_nota(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = media_nota(nota1, nota2, nota3) # 6
print(media)

# 100) Melhore o exercício 96, criando além da função Media() uma outra função 
# chamada Situacao(), que vai retornar para o programa principal se o aluno está 
# APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como 
# parâmetro o resultado retornado pela função Media().
def situacao(media):
    if media >= 7:
        return 'APROVADO'
    elif media >= 5 and media <= 6.9:
        return 'RECUPERACAO'
    else:
        return 'REPROVADO'

resultado = situacao(media)
print(resultado)