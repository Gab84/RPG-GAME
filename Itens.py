from Player import player

armas = {
    'adaga':{
        'nome':'adaga',
        'dano':[12,15],
        'preco' : 10,
        'raridade': [],
        'pontos' : 10,
        'nome_colorido': ''
    },
    
    'espada_curta':{
        'dano':[15,20],
        'nome':'espada_curta',
        'preco' : 15,
        'raridade': [],
        'pontos' : 10,
        'nome_colorido': ''

    },
    'cajado':{
        'dano':[10,23],
        'nome': 'cajado',
        'preco' : 10,
        'raridade': [],
        'pontos' : 10,
        'nome_colorido': ''
    },
    'varinha':{
        'dano':[10,20],
        'nome': 'varinha',
        'preco' : 10,
        'raridade': [],
        'pontos' : 10,
        'nome_colorido': ''
    },
    'machado':{
        'dano':[15,20],
        'nome' : 'machado',
        'preco' : 20,
        'raridade': [],
        'pontos' : 10,
        'nome_colorido': ''
    },
    
    
}

consumiveis = {

    'suco_maça' : {
        'nome' : 'suco_maça',
        'cura' : 30,
        'preco' : 15,
        'raridade': [],
        'pontos' : 20
    },
    'cafezin' : {
        'nome' : 'cafezin',
        'cura' : 30,
        'preco' : 10,
        'raridade': [],
        'pontos' : 25
    },

}

equipamentos = {
    'capacete' : {
        'nome' : 'capacete',
        'def' : 3,
        'raridade': [],
        'preco': 10,
        'pontos' : 15,
        'nome_colorido': ''
    },
    'peitoral' : {
        'nome' : 'peitoral',
        'def' : 5,
        'raridade': [],
        'preco': 20,
        'pontos' : 30,
        'nome_colorido': ''
    },
    'calca' : {
        'nome' : 'calca',
        'def' : 4,
        'raridade': [],
        'preco': 15,
        'pontos' : 22,
        'nome_colorido': ''
    },
    'bota' : {
        'nome' : 'bota',
        'def' : 2,
        'raridade': [],
        'preco': 5,
        'pontos' : 13,
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