# Criar um dicionario 
pessoa = {
    "nome": "Fabio",
    "altura": 1.70,
    "peso": 85,
    "anoNascimento": 1982,
    "times": ['Botafogo','Brasil','Flamengo'] # podemos colocar um array
}

# acessar um valor no dicionario 
print(pessoa['altura']) 

# comprimento (quantas propriedades)
print(len(pessoa))

# Podemos guardar um valor dentro de uma variavel
nome = pessoa['nome']
print(nome)

# Alterar valor no dicionario 
pessoa['peso'] = 81
print(pessoa)

# Criar um valor novo no dicionario 
pessoa['corCabelo'] = "Inexistente"
print(pessoa)

# Criando um array de dicionarios
turma = [
    {
        "nome": "Ana Wictorya",
        "idade": 19,
        "corCabelo": "preto"
    },
    {
        "nome": "Camila",
        "idade": 19,
        "corCabelo": "castanho escuro"
    },
    {
        "nome": "Bernardo",
        "idade": 14,
        "corCabelo": "preto"
    },
]

# mostrar o nome da camila dentro do print
print(turma[1]['nome'])

# mostrar todos os nomes das chaves (propriedade)
for i in pessoa:
    print(i)

# mostrar todos os valores do dicionario 
for i in pessoa.values():
    print(i)

# mostra valores de um array de dicionarios 
for t in turma:
    # pegando todos os nomes
    print(t['nome'])