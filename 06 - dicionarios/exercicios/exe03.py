# Conversao para numeros 
idade = "15"
temperatura = "33.8"
print(int(idade) + 15) # convertendo pra int
print(float(idade)) # convertendo pra float

# Exercicio => soma e tirar a media
turma = [
    {
        "nome": 'Willian',
        "nota": "8.5"
    },
    {
        "nome": 'Fabio',
        "nota": "8.0"
    },
    {
        "nome": 'Dudu',
        "nota": "3.5"
    },
    {
        "nome": 'Pablo',
        "nota": "6.7"
    },
]

soma = 0
for t in turma:
   notas = float(t['nota'])
   soma = soma + notas

media = soma / len(turma)
print(f'A media final é de: {round(media,1)}')