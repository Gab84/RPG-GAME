import random

import random

# Dicionário de armas
armas = {
    'adaga': {'nome': 'adaga', 'dano': [7, 11], 'preco': 10},
    'espada_curta': {'dano': [15, 20], 'nome': 'espada_curta', 'preco': 15},
    'cajado': {'dano': [15, 23], 'nome': 'cajado', 'preco': 10},
    'varinha': {'dano': [10, 20], 'nome': 'varinha', 'preco': 10},
    'machado': {'dano': [25, 35], 'nome': 'machado', 'preco': 20},
}

# Dicionário de equipamentos
equipamentos = {
    'capacete': {'nome': 'capacete', 'def': 20},
    'peitoral': {'nome': 'peitoral', 'def': 20},
    'calca': {'nome': 'calca', 'def': 20},
    'bota': {'nome': 'bota', 'def': 20},
}

# Modificadores de raridade
modificadores_raridade = {
    'comum': {'dano': 1.0, 'def': 1.0, 'preco': 1.0},
    'incomum': {'dano': 1.2, 'def': 1.2, 'preco': 1.5},
    'raro': {'dano': 1.5, 'def': 1.5, 'preco': 2.0},
    'épico': {'dano': 2.0, 'def': 2.0, 'preco': 3.0},
    'lendário': {'dano': 3.0, 'def': 3.0, 'preco': 5.0}
}

# Probabilidades de raridade
probabilidades = {
    'comum': 60,
    'incomum': 25,
    'raro': 10,
    'épico': 4,
    'lendário': 1
}

# Cores de raridade
cores_raridade = {
    'comum': '\033[90m',  # cinza
    'incomum': '\033[92m',  # verde
    'raro': '\033[94m',  # azul
    'épico': '\033[95m',  # roxo
    'lendário': '\033[93m',  # dourado
    'reset': '\033[0m'  # resetar cor
}

# Função para gerar raridade
def gerar_raridade():
    numero_aleatorio = random.randint(1, 100)
    soma_probabilidades = 0
    for raridade, chance in probabilidades.items():
        soma_probabilidades += chance
        if numero_aleatorio <= soma_probabilidades:
            return raridade

# Função para aplicar modificadores às armas
def aplicar_modificadores_arma(arma, raridade):
    modificador = modificadores_raridade[raridade]
    dano_modificado = [int(d * modificador['dano']) for d in arma['dano']]
    preco_modificado = int(arma['preco'] * modificador['preco'])
    arma_modificada = arma.copy()
    arma_modificada['dano'] = dano_modificado
    arma_modificada['preco'] = preco_modificado
    arma_modificada['nome'] = f"{cores_raridade[raridade]}{arma_modificada['nome']}{cores_raridade['reset']}"
    return arma_modificada

# Função para gerar arma
def gerar_arma():
    raridade = gerar_raridade()
    arma_nome = random.choice(list(armas.keys()))
    arma_base = armas[arma_nome]
    arma_modificada = aplicar_modificadores_arma(arma_base, raridade)
    arma_modificada['raridade'] = raridade
    return arma_modificada

# Função para aplicar modificadores aos equipamentos
def aplicar_modificadores_equipamento(equipamento, raridade):
    modificador = modificadores_raridade[raridade]
    def_modificado = int(equipamento['def'] * modificador['def'])
    preco_modificado = int(equipamento.get('preco', 10) * modificador['preco'])  # Definindo um preço padrão caso não exista
    equipamento_modificado = equipamento.copy()
    equipamento_modificado['def'] = def_modificado
    equipamento_modificado['preco'] = preco_modificado
    equipamento_modificado['nome'] = f"{cores_raridade[raridade]}{equipamento_modificado['nome']}{cores_raridade['reset']}"
    return equipamento_modificado

# Função para gerar equipamento
def gerar_equipamento():
    raridade = gerar_raridade()
    equipamento_nome = random.choice(list(equipamentos.keys()))
    equipamento_base = equipamentos[equipamento_nome]
    equipamento_modificado = aplicar_modificadores_equipamento(equipamento_base, raridade)
    equipamento_modificado['raridade'] = raridade
    return equipamento_modificado

# Teste das funções
for i in range(5):
    arma = gerar_arma()
    print(f"{arma['nome']}: Dano {arma['dano']}, Preço {arma['preco']}, Raridade {arma['raridade']}")

for i in range(5):
    equipamento = gerar_equipamento()
    print(f"{equipamento['nome']}: Defesa {equipamento['def']}, Preço {equipamento['preco']}, Raridade {equipamento['raridade']}")





# Dicionário de equipamentos
equipamentos = {
    'capacete': {'nome': 'capacete', 'def': 20},
    'peitoral': {'nome': 'peitoral', 'def': 20},
    'calca': {'nome': 'calca', 'def': 20},
    'bota': {'nome': 'bota', 'def': 20},
}

# Modificadores de raridade
modificadores_raridade = {
    'comum': {'def': 1.0, 'preco': 1.0},
    'incomum': {'def': 1.2, 'preco': 1.5},
    'raro': {'def': 1.5, 'preco': 2.0},
    'épico': {'def': 2.0, 'preco': 3.0},
    'lendário': {'def': 3.0, 'preco': 5.0}
}

# Probabilidades de raridade
probabilidades = {
    'comum': 60,
    'incomum': 25,
    'raro': 10,
    'épico': 4,
    'lendário': 1
}

# Cores de raridade
cores_raridade = {
    'comum': '\033[90m',  # cinza
    'incomum': '\033[92m',  # verde
    'raro': '\033[94m',  # azul
    'épico': '\033[95m',  # roxo
    'lendário': '\033[93m',  # dourado
    'reset': '\033[0m'  # resetar cor
}

# Função para gerar raridade
def gerar_raridade():
    numero_aleatorio = random.randint(1, 100)
    soma_probabilidades = 0
    for raridade, chance in probabilidades.items():
        soma_probabilidades += chance
        if numero_aleatorio <= soma_probabilidades:
            return raridade

# Função para aplicar modificadores aos equipamentos
def aplicar_modificadores_equipamento(equipamento, raridade):
    modificador = modificadores_raridade[raridade]
    def_modificado = int(equipamento['def'] * modificador['def'])
    preco_modificado = int(equipamento.get('preco', 10) * modificador['preco'])  # Definindo um preço padrão caso não exista
    equipamento_modificado = equipamento.copy()
    equipamento_modificado['def'] = def_modificado
    equipamento_modificado['preco'] = preco_modificado
    return equipamento_modificado

# Função para gerar equipamento
def gerar_equipamento():
    raridade = gerar_raridade()
    equipamento_nome = random.choice(list(equipamentos.keys()))
    equipamento_base = equipamentos[equipamento_nome]
    equipamento_modificado = aplicar_modificadores_equipamento(equipamento_base, raridade)
    equipamento_modificado['raridade'] = raridade
    equipamento_modificado['nome'] = f"{cores_raridade[raridade]}{equipamento_modificado['nome']}{cores_raridade['reset']}"
    return equipamento_modificado

# Teste a função
for i in range(10):
    equipamento = gerar_equipamento()
    print(f"{equipamento['nome']}: Defesa {equipamento['def']}, Preço {equipamento['preco']}, Raridade {equipamento['raridade']}")

