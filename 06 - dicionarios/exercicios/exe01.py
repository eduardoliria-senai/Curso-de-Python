produtos = [
    {
        "nome": "Notebook",
        "preco": 4500
    },
    {
        "nome": "Celular",
        "preco": 1800.50
    },
    {
        "nome": "Mouse",
        "preco": 45
    },
    {
        "nome": "Monitor",
        "preco": 670
    },
    {
        "nome": "Teclado",
        "preco": 67
    },
]

# somar todos os valores dos produtos. 
soma = 0
for p in produtos:
    precos = p['preco']
    soma += precos

print(f'A soma total dos produtos foi de R$ {soma}')