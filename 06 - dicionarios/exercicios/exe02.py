# para transformar uma palavra toda em maiusculo
nome = 'fabio'
print(nome.upper())

# Exercicio 
alunos = [
    {
        "nome":"fabio",
        "idade": 45
    },
    {
        "nome":"eduardo de oliveira",
        "idade": 25
    },
    {
        "nome":"bernardo",
        "idade": 14
    },
    {
        "nome":"pablo",
        "idade": 15
    },
    {
        "nome":"miguel",
        "idade": 15
    },
]

for aluno in alunos:
    nomes = aluno['nome']
    print(nomes.upper())