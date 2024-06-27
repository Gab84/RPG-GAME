from Player import player
from rich import *
armas = {
    'adaga':{
        'nome':'adaga',
        'dano':[12,15],
        'preco' : (10*player['level']),
        'raridade': [],
        'pontos' : (10*player['level']),
        'nome_colorido': ''
    },
    
    'espada_curta':{
        'dano':[15,20],
        'nome':'espada_curta',
        'preco' : (15*player['level']),
        'raridade': [],
        'pontos' : (10*player['level']),
        'nome_colorido': ''

    },
    'cajado':{
        'dano':[10,23],
        'nome': 'cajado',
        'preco' : (10*player['level']),
        'raridade': [],
        'pontos' : (10*player['level']),
        'nome_colorido': ''
    },
    'varinha':{
        'dano':[10,20],
        'nome': 'varinha',
        'preco' : (10*player['level']),
        'raridade': [],
        'pontos' : (10*player['level']),
        'nome_colorido': ''
    },
    'machado':{
        'dano':[15,20],
        'nome' : 'machado',
        'preco' : (20*player['level']),
        'raridade': [],
        'pontos' : (10*player['level']),
        'nome_colorido': ''
    },
    
    
}

consumiveis = {

    'suco_maça' : {
        'nome' : 'suco_maça',
        'cura' : (30+player['level']+5),
        'preco' : (15*player['level']),
        'raridade': [],
        'pontos' : (25*player['level'])
    },
    'cafezin' : {
        'nome' : 'cafezin',
        'cura' : (30+player['level']+5),
        'preco' : (10*player['level']),
        'raridade': [],
        'pontos' : (25*player['level'])
    },

}

equipamentos = {
    'capacete' : {
        'nome' : 'capacete',
        'def' : (6+player['level']),
        'raridade': [],
        'preco': (10*player['level']),
        'pontos' : (15*player['level']),
        'nome_colorido': ''
    },
    'peitoral' : {
        'nome' : 'peitoral',
        'def' : (5+player['level']),
        'raridade': [],
        'preco': (20*player['level']),
        'pontos' : (30*player['level']),
        'nome_colorido': ''
    },
    'calca' : {
        'nome' : 'calca',
        'def' : (4+player['level']),
        'raridade': [],
        'preco': (15*player['level']),
        'pontos' : (22*player['level']),
        'nome_colorido': ''
    },
    'bota' : {
        'nome' : 'bota',
        'def' : (2+player['level']),
        'raridade': [],
        'preco': (5*player['level']),
        'pontos' : (13*player['level']),
        'nome_colorido': ''
    },

    
}

def equip_(item,p_inv):
    print(p_inv)
    
    p_inv.append(item)

    print(f"{item} foi adicionado ao do player. ")
    print(p_inv)

def equip_cura():    
    equip_(item=consumiveis['suco_maça']['nome'],p_inv=player['inventario'])
def equip_mana():    
    equip_(item=consumiveis['cafezin']['nome'],p_inv=player['inventario'])


def usar_suco_maça():
    print("Usando Suco de maça🧃 . Cura 20 pontos de vida.")
    if player['vida'] > player['vida_max']:
        player['vida'] = player['vida_max']
    else:
        player['vida'] += 20

def usar_cafezin():
    print("Usando Cafezin🥤 . Recupera 20 pontos de mana.")
    if player['mana'] > player['mana_max']:
        player['mana'] = player['mana_max']
    else:
        player['mana'] += 20



funcoes_consumiveis = {
    'suco_maça': usar_suco_maça,
    'cafezin': usar_cafezin,
}





#print(armas['adaga']['nome'])