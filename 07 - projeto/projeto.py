# Importar o modulo csv
import csv

# armazenar a planilha em uma variavel
planilha = "07 - projeto\produtos.csv"

# criar funcao para LER a planilha 
def carregar_produtos():
    # criar o array vazio
    produtos = []

    with open(planilha, 'r', encoding="utf-8-sig") as arquivo:
        # Pegando a planilha e tranformando em um dicionario
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha['preco'] = float(linha['preco'])
            linha['quantidade'] = int(linha['quantidade'])

            # Adiciona essas linhas 
            produtos.append(linha)

    return produtos

print(carregar_produtos())