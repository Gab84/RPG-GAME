import random
# Define as escalas de raridade, seus multiplicadores e cores
raridades = {
    'comum': {'multiplicador': 1.0, 'cor': '[white]'},         # Branco padrão
    'incomum': {'multiplicador': 1.1, 'cor': '[green]'},      # Verde
    'raro': {'multiplicador': 1.2, 'cor': '[cyan]'},         # Azul
    'épico': {'multiplicador': 1.3, 'cor': '[magenta]'},        # Magenta
    'lendário': {'multiplicador': 1.5, 'cor': '[yellow]'}      # Amarelo
}

# Função para aplicar a raridade aos atributos
def aplicar_raridade(item, raridade):
    multiplicador = raridades[raridade]['multiplicador']
    cor = raridades[raridade]['cor']
    if 'dano' in item:
        item['dano'] = [int(d * multiplicador) for d in item['dano']]
    if 'def' in item:
        item['def'] = int(item['def'] * multiplicador)
    if 'preco' in item:
        item['preco'] = int(item['preco'] * multiplicador)
    item['raridade'] = raridade
    item['nome_colorido'] = f"{cor}{item['nome']}[/]"  # Atualiza o nome com a cor

# Função para gerar uma raridade aleatória
def gerar_raridade():
    return random.choice(list(raridades.keys()))

# Função para aplicar raridade a todos os itens
def gerar_raridades_itens(armas, equipamentos):
    for arma in armas.values():
        raridade = gerar_raridade()
        aplicar_raridade(arma, raridade)
    for equipamento in equipamentos.values():
        raridade = gerar_raridade()
        aplicar_raridade(equipamento, raridade)
    
    #removido pois acho que nao precisa gerar raridade de itens, deixar eles sempre padroes.
"""    for consumivel in consumiveis.values():
        raridade = gerar_raridade()
        aplicar_raridade(consumivel, raridade)"""



# Dados dos itens

# Aplicar raridade aos itens
#gerar_raridades_itens(armas, consumiveis, equipamentos)

# Função para exibir itens com cor
def exibir_item_com_cor(item):
    cor = raridades[item['raridade']]['cor']
    nome_colorido = f"{cor}{item['nome']}[/]"
    print(f"{nome_colorido}: {item}")
