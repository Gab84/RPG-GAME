from Player import *


Atributos = {
    'Forca' : 1,
    'Constituicao' : 1,
    'Mente': 1,
}


def distribuir_pt():
    for x in range(2):
        print('Você tem 2 pontos de atributos para distribuir')
        v = int(input('1 > Força 💪​ (Força upa o Dano dos seus golpes) | 2 > Constituição 🧡​ (Aumenta sua vida maxima e cura parte da sua vida)| 3 > Mente 📖​ (Aumenta sua mana maxima e recupera parte da sua mana.)') )
        if v == 1:
            print(f"{player['nome']} Upou 1 ponto em força .")
            player['dano'][0] += Atributos['Forca']
            player['dano'][1] += Atributos['Forca']
            print(f"O seu dano aumentou > {player['dano']}")
        if v == 2:
            print(f"{player['nome']} Upou 1 ponto em Constituição .")
            player['vida_max'] += Atributos['Constituicao']
            player['vida'] += 20
            print(f"Sua vida Maxima aumentou > {player['vida_max']}")
        if v == 3:
            print(f"{player['nome']} Upou 1 ponto em Mente .")
            player['mana_max'] += Atributos['Mente']
            player['mana'] += 20
            print(f"Sua mana Maxima aumentou > {player['mana_max']}")
    return


