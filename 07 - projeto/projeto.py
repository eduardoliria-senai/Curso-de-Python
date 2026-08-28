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

# funcao para mostrar produtos 
def mostrar_produtos(produtos):

    # titulo
    print("\n ===== PRODUTOS =====")

    for produto in produtos:
        print(
            f'{produto['produto']} | '
            f'{produto['categoria']} | '
            f'R$ {produto['preco']:.2} | '
            f'Estoque {produto['quantidade']} | '
            f'{produto['fornecedor']}'
        )

# Funcao para calcular a media
def calcular_media(produtos): 
    soma = 0

    for produto in produtos:
        soma += produto['preco']

    media = soma / len(produtos)

    print(f"\n A media de preços é de: R$ {media:.2f}")

# funcao para filtrar valores acima de algum valor
def produtos_acima(produtos):

    valor = float(input("\nMostrar produtos acima de R$: "))
    encontrados = 0

    for produto in produtos:

        if produto['preco'] > valor:
            print(
                f'{produto['produto']} - '
                f'R$ {produto['preco']:.2f} '
            )

            encontrados += 1

    if encontrados == 0:
        print("Nenhum produto encontrado.")

    print(f"Quantidade de produtos encontrados foi de: {encontrados}")

# funcao para filtrar valores abaixo de algum valor
def produtos_abaixo(produtos):
    valor = float(input('\nMostrar produtos abaixo de R$'))
    encontrados = 0

    for produto in produtos:
        if produto['preco'] < valor:
            print(
                f'{produto['produto']} - '
                f'R$ {produto['preco']:.2f} '
            )
            encontrados += 1

    if encontrados == 0:
        print('Nenhum produto encontrado')

    print(f"Quantidade de produtos encontrados foi de: {encontrados}")
        

# filtrar por CATEGORIA 
def filtrar_categoria(produtos):
    # mostrar todas as categorias
    print('\n === Todas as categorias ==== \n')
    for produto in produtos:
        print(f'Categoria: {produto['categoria']}')

    categoria = input("Digite a categoria: ")
    encontrados = 0

    print(f'\n ==== CATEGORIA: {categoria} ====')

    for produto in produtos:
        if produto['categoria'].lower() == categoria.lower():
            print(
                f'{produto['produto']} - '
                f'{produto['preco']:.2f}'
            )

            encontrados = encontrados + 1

    if encontrados == 0:
        print('Nenhum produto encontrado')

# filtra por fornecedor
def filtra_fornecedor(produtos):
    # mostrar todas as fornecedores
    print('\n === Todas os Fornecedores ==== \n')
    encontrados = 0
    for produto in produtos:
        print(f'Fornecedor: {produto['fornecedor']}')

    fornecedor = input('Digite o fornecedor: ')

    for produto in produtos:
        if produto['fornecedor'].lower() == fornecedor.lower():
            print(
                f'{produto['produto']} - '
                f'{produto['preco']:.2f}'
            )

            encontrados = encontrados + 1

    if encontrados == 0: 
        print('Nenhum produto encontrado!')


# funcao para pegar o produto mais caro
def produto_mais_caro(produtos):
    mais_caro = produtos[0]

    for produto in produtos:
        if produto['preco'] > mais_caro['preco']:
            mais_caro = produto

    print("\n==== PRODUTO MAIS CARO É ====\n")

    print(f'Produto: {mais_caro['produto']}')
    print(f'Preco: {mais_caro['preco']:.2f}')
    print(f'Categoria: {mais_caro['categoria']}')

# funcoa pegar o produto mais barato
def produto_mais_barato(produtos):
    mais_barato = produtos[0]

    for produto in produtos:
        if produto['preco'] < mais_barato['preco']:
            mais_barato = produto

    print("\n==== PRODUTO MAIS BARATO É ====\n")
    
    print(f'Produto: {mais_barato['produto']}')
    print(f'Preco: {mais_barato['preco']:.2f}')
    print(f'Categoria: {mais_barato['categoria']}')

# Calcular o estoque
# def calcular_estoque(produtos):


def menu():
    print('\n ==== Escolha as opcoes abaixo ====')
    print('1 - Mostrar Produtos')
    print('2 - Calcular a media')
    print('3 - Produtos acima...')
    print('4 - Produtos abaixo...')
    print('5 - Produto mais barato')
    print('6 - Produto mais caro')
    print('7 - Filtrar por Categoria')
    print('8 - Filtrar por Fornecedor')
    print('9 - Calcular estoque')
    print('10 - Encerrar')

produtos = carregar_produtos()

while True:
    # puxar a funcao de menu
    menu()
    opcao = int(input('Digite uma opcao: '))

    if opcao == 1:
        mostrar_produtos(produtos)
    elif opcao == 2:
        calcular_media(produtos)
    elif opcao == 3:
        produtos_acima(produtos)
    elif opcao == 4:
        produtos_abaixo(produtos)
    elif opcao == 5:
        produto_mais_barato(produtos)
    elif opcao == 6:
        produto_mais_caro(produtos)
    elif opcao == 7:
        filtrar_categoria(produtos)
    elif opcao == 8:
        filtra_fornecedor(produtos)
    elif opcao == 9:
        break