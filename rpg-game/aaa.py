import random
import time
from classes import *

# Define as escalas de raridade, seus multiplicadores e cores
raridades = {
    'comum': {'multiplicador': 1.0, 'cor': '\033[0m'},         # Branco padrão
    'incomum': {'multiplicador': 1.1, 'cor': '\033[32m'},      # Verde
    'raro': {'multiplicador': 1.2, 'cor': '\033[34m'},         # Azul
    'épico': {'multiplicador': 1.3, 'cor': '\033[35m'},        # Magenta
    'lendário': {'multiplicador': 1.5, 'cor': '\033[33m'}      # Amarelo
}

# Função para aplicar a raridade aos atributos
def aplicar_raridade(item, raridade):
    multiplicador = raridades[raridade]['multiplicador']
    cor = raridades[raridade]['cor']
    if 'def' in item:
        item['def'] = int(item['def'] * multiplicador)
    if 'dano' in item:
        item['dano'] = [int(d * multiplicador) for d in item['dano']]
    item['raridade'] = raridade
    item['nome_colorido'] = f"{cor}{item['nome']}\033[0m"  # Atualiza o nome com a cor

# Função para gerar uma raridade aleatória
def gerar_raridade():
    return random.choice(list(raridades.keys()))

# Função para aplicar raridade a todos os itens
def gerar_raridades_itens(itens):
    for item in itens.values():
        raridade = gerar_raridade()
        aplicar_raridade(item, raridade)

# Dados do jogador
player = {
    'nome' : input('Digite o Nome do Heroi ! > '),
    'level' : 1,
    'exp' : 0,
    'exp_max' : 50,
    'vida' : 50,
    'vida_min': 0,
    'vida_max' : 100,
    'dano_base' : [1,1,0],
    'dano' : [0,0,0], # Inicializa zerado
    'golpes': ["golpe_basico (1) ",'golpe_forte (2) ','cura(3)','inventario(4)'],
    'armas' : ['desarmado'],
    'mana' : 0,
    'mana_inicial': 0,
    'mana_max' : 100,
    'cura' : 7,
    'inventario' : ['suco de maça🧃'],
    'classe' : ['guerreiro'],
    'dinheiro': 50,
    'armaduras_equipadas': {},  # Armazena as armaduras equipadas por categoria
    'defesa' : 0
}

# Dados dos equipamentos
equipamentos = {
    'capacete': {'nome': 'capacete', 'def': 20},
    'peitoral': {'nome': 'peitoral', 'def': 20},
    'calca': {'nome': 'calca', 'def': 20},
    'bota': {'nome': 'bota', 'def': 20},
}

# Dados das armas
armas = {
    'espada': {'nome': 'espada', 'dano': [10, 15], 'raridade': ''},
    'machado': {'nome': 'machado', 'dano': [15, 20], 'raridade': ''},
}

# Aplicar raridade aos equipamentos e armas inicialmente
gerar_raridades_itens(equipamentos)
gerar_raridades_itens(armas)

# Função para determinar o tipo de classe (Exemplo simplificado)

def determinar_classe_tipo(classe):
    if classe in Furtivo['classe']:
        return 'Furtivo'
    elif classe in Magias['classe']:
        return 'Magias'
    elif classe in Corpo_a_corpo['classe']:
        return 'Corpo_a_corpo'
    return None

# Dicionário de multiplicadores de dano por classe
multiplicadores_dano = {
    'guerreiro': {'espada': 1.2, 'machado': 1.1},
    'mago': {'espada': 0.8, 'machado': 0.7},
}

# Função para equipar uma arma
def equip_arma(p, arma_nome):
    nova_arma = armas[arma_nome]

    if arma_nome  in p['armas']:
        arma_atual_nome = p['armas'][0]
        arma_atual = armas[arma_atual_nome]
        print(f"Você já tem uma {arma_atual['nome']} equipada com raridade {arma_atual['raridade']}.")
        print(f"A nova arma é {nova_arma['nome']} com raridade {nova_arma['raridade']}.")

        # Pergunta ao jogador se deseja substituir a arma existente
        resposta = input("Deseja substituir a arma existente? (s/n): ")
        if resposta.lower() != 's':
            print("A arma não foi substituída.")
            return
        else:
            print(f"Você jogou fora a arma {arma_atual['nome']}.")

    # Equipar a nova arma
    p['armas'] = [arma_nome]
    
    classe_tipo = determinar_classe_tipo(p['classe'])
    
    if classe_tipo not in multiplicadores_dano:
        print("Classe do jogador inválida.")
        return
    
    multiplicador = multiplicadores_dano[classe_tipo].get(arma_nome, 1)
    
    d1 = int(nova_arma['dano'][0] * multiplicador)
    d2 = int(nova_arma['dano'][1] * multiplicador)
    
    p['dano'][0] = (d1 + p['dano_base'][0])
    p['dano'][1] = (d2 + p['dano_base'][1])
    print(f"Você pegou uma arma com raridade {nova_arma['raridade']}")
    print(f"{nova_arma['nome_colorido']} FOI COLOCADO NA SUA MÃO, AGORA VOCÊ TA POTENTE {p['dano']}")
    time.sleep(5)

# Função para equipar uma armadura
def equip_armadura(p, armadura_nome):
    armadura = equipamentos[armadura_nome]
    
    # Verifica se uma armadura da mesma categoria já está equipada
    if armadura_nome in p['armaduras_equipadas']:
        armadura_atual = p['armaduras_equipadas'][armadura_nome]
        print(f"Você já tem um {armadura_atual['nome']} equipado com raridade {armadura_atual['raridade']}.")
        print(f"A nova armadura é {armadura['nome']} com raridade {armadura['raridade']}.")
        
        # Pergunta ao jogador se deseja substituir a armadura existente
        resposta = input("Deseja substituir a armadura existente? (s/n): ")
        if resposta.lower() != 's':
            print("A armadura não foi substituída.")
            return
        else:
            # Remove a defesa da armadura antiga da defesa total do jogador
            p['defesa'] -= armadura_atual['def']
            print(f"Você substituiu a armadura {armadura_atual['nome']} por {armadura['nome']}.")
    
    # Equipar a nova armadura
    p['armaduras_equipadas'][armadura_nome] = armadura
    p['defesa'] += armadura['def']
    
    print(f"Você equipou uma armadura com raridade {armadura['raridade']}.")
    print(f"{armadura['nome_colorido']} está equipada, agora você está mais protegido.")
    time.sleep(5)

# Função para exibir o HUD do jogador
def Hud_player():
    player_mana_bar = mana_bar(man_atual=player['mana'], mana_max=player['mana_max'])
    player_xp_bar = xp_bar(xp_atual=player['exp'], xp_max=player['exp_max'])
    player_hp_bar = display_player_hp_bar(current_hp=player['vida'], max_hp=player['vida_max'])
    
    armaduras_equipadas = [armadura['nome_colorido'] for armadura in player['armaduras_equipadas'].values()]
    defesa_total = player['defesa']
    
    print(f"""------------------------------
JOGADOR 👤 : {player['nome']} 
------------------------------
Vida: {player_hp_bar} | Mana: {player_mana_bar} 
            {player['vida']}/{player['vida_max']}                       {player['mana']}/{player['mana_max']}                
------------------------------
Armaduras 🛡️ : {', '.join(armaduras_equipadas) if armaduras_equipadas else 'Nenhuma'} | INVENTÁRIO 🎒 : {player['inventario']} | Dinheiro 💰 : {player['dinheiro']}

Nível 🌟 : {player['level']} | Exp 📚 : {player['exp']}/{player['exp_max']} {player_xp_bar} 

Classe 🏋️‍♀️ : {player['classe']}

Defesa Total 🛡️ : {defesa_total}

AÇÕES -->  {player['golpes'][0]}🗡️  : DANO : {player['dano'][0]} ❤️  | {player['golpes'][1]}🗡️  : DANO : {player['dano'][1]} ❤️  | {player['golpes'][2]} 🩹 : CURA: {player['cura']} ❤️  | {player['golpes'][3]}🎒 : ABRIR INVENTÁRIO
------------------------------""")

# Função exemplo para barras (simplificação)
def mana_bar(man_atual, mana_max):
    return f"{'█' * (man_atual * 10 // mana_max)}{' ' * (10 - man_atual * 10 // mana_max)}"

def xp_bar(xp_atual, xp_max):
    return f"{'█' * (xp_atual * 10 // xp_max)}{' ' * (10 - xp_atual * 10 // xp_max)}"

def display_player_hp_bar(current_hp, max_hp):
    return f"{'█' * (current_hp * 10 // max_hp)}{' ' * (10 - current_hp * 10 // max_hp)}"

# Exemplo de uso
equip_armadura(player, 'capacete')
equip_armadura(player, 'peitoral')

equip_arma(player, 'machado')
equip_arma(player, 'espada')
# Exibir o HUD do jogador
Hud_player()
