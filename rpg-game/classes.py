from Player import player
from Personagens import *
from Textos import desc_Furtivo,Hud_player,desc_armas,txtlore
from Itens import armas,consumiveis,equipamentos
from time import sleep
import os
import platform
from Raridadesf import *

def clear_terminal():
    system_name = platform.system()
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


Furtivo = {
    'classe' : ['1 > Bandido', '2 > Gnomo'],

    '1 > Bandido':{
        'nome' : player['nome'],
        'level' : player['level'],
        'exp' : player['exp'],
        'exp_max' : player['exp_max'],
        'vida' : 90,
        'vida_min': 0,
        'vida_max' : 90,
        'dano_base': [5,7,0],
        'dano' : [5, 7, 0],
        'golpes': ["golpe_basico (1)", 'golpe_forte (2)', 'cura(3)', 'inventario(4)'],
        'armas' : [],
        'mana' : 50,
        'mana_inicial':50,
        'mana_max' : 100,
        'cura' : 10,
        'inventario' : ["suco_maça"],
        
    },

    '2 > Gnomo': {

        'nome' : player['nome'],
        'level' : player['level'],
        'exp' : player['exp'],
        'exp_max' : player['exp_max'],
        'vida' : 80,
        'vida_min': 0,
        'vida_max' : 80,
        'dano_base': [5,7,0],
        'dano' : [5, 7, 0],
        'golpes': ["golpe_basico (1)", 'golpe_forte (2)', 'cura(3)','inventario(4)'],
        'armas' : [],
        'mana' : 50,
        'mana_inicial':50,
        'mana_max' : 100,
        'cura' : 10,
        'inventario' : ["suco_maça"],        

    }
}

Magias = {
    'classe' : ['1 > Bruxo', '2 > Mago'],

    '1 > Bruxo':{
        'nome' : player['nome'],
        'level' : player['level'],
        'exp' : player['exp'],
        'exp_max' : player['exp_max'],
        'vida' : 100,
        'vida_min': 0,
        'vida_max' : 100,
        'dano_base': [5,7,0],
        'dano' : [5, 7, 0],
        'golpes': ["golpe_magico (1)", 'feitiço_forte (2)', 'cura(3)','inventario(4)'],
        'armas' : [],
        'mana' : 100,
        'mana_inicial':100,
        'mana_max' : 200,
        'cura' : 10,
        'inventario' : ["cafezin","cafezin"],
        
    },

    '2 > Mago': {

        'nome' : player['nome'],
        'level' : player['level'],
        'exp' : player['exp'],
        'exp_max' : player['exp_max'],
        'vida' : 100,
        'vida_min': 0,
        'vida_max' : 100,
        'dano_base': [5,7,0],
        'dano' : [5, 7, 0],
        'golpes': ["golpe_magico (1)", 'feitiço_forte (2)', 'cura(3)','inventario(4)'],
        'armas' : [],
        'mana' : 100,
        'mana_inicial':100,
        'mana_max' : 200,
        'cura' : 10,
        'inventario' : ["cafezin","cafezin"],        

    }
}

Corpo_a_corpo = {
    'classe' : ['1 > Guerreiro', '2 > Barbaro'],

    '1 > Guerreiro':{
        'nome' : player['nome'],
        'level' : player['level'],
        'exp' : player['exp'],
        'exp_max' : player['exp_max'],
        'vida' : 120,
        'vida_min': 0,
        'vida_max' : 120,
        'dano_base': [12, 4, 0],
        'dano' : [12, 4, 0],
        'golpes': ["soco (1)", 'chute (2)', 'cura(3)','inventario(4)'],
        'armas' : [],
        'mana' : 0,
        'mana_inicial':0,
        'mana_max' : 50,
        'cura' : 50,
        'inventario' : ["suco_maça"],
        
    },

    '2 > Barbaro': {

        'nome' : player['nome'],
        'level' : player['level'],
        'exp' : player['exp'],
        'exp_max' : player['exp_max'],
        'vida' : 125,
        'vida_min': 0,
        'vida_max' : 125,
        'dano_base': [5,7,0],
        'dano' : [5, 7, 0],
        'golpes': ["soco (1)", 'chute (2)', 'cura(3)','inventario(4)'],
        'armas' : [],
        'mana' : 0,
        'mana_inicial':0,
        'mana_max' : 50,
        'cura' : 50,
        'inventario' : ["suco_maça"],        

    }
}

multiplicadores_dano = {
    'Furtivo': {
        'adaga': 2,
        'espada_curta': 1.2,
        'cajado': 0.6,
        'varinha': 0.8,
        'machado': 1.0,
    },
    'Magias': {
        'adaga': 0.3,
        'espada_curta': 0.5,
        'cajado': 4000,
        'varinha': 1.5,
        'machado': 0.5,
    },
    'Corpo_a_corpo': {
        'adaga': 0.9,
        'espada_curta': 1.5,
        'cajado': 0.7,
        'varinha': 0.7,
        'machado': 2,
    }
}



def escolha_classe():
    txtlore("AGORA ESCOLHA SUA CLASSE ", delay=0.05)
    print(f"ESCOLHA SUA CATEGORIA, {player['nome']}.")
    txtlore("CATEGORIAS DISPONÍVEIS", delay=0.05)
    txtlore("1 > FURTIVO \n2 > MAGIAS \n3 > CORPO A CORPO", delay=0.05)
    sleep(1)
    categoria = input('QUAL CAMINHO DESEJA SEGUIR > ')
    clear_terminal()
    
    if categoria == '1':
        categorias = Furtivo
        bandido_gnomo()
        desc_Furtivo()
    elif categoria == '2':
        categorias = Magias
        bruxo_mago()
    elif categoria == '3':
        categorias = Corpo_a_corpo
        guerreiro_barbaro()
    else:
        print("Categoria não encontrada")
        return
    txtlore("AGORA ESCOLHA SUA CLASSE ", delay=0.05)
    txtlore(f"CLASSES DISPONÍVEIS > {categorias['classe']}  ", delay=0.05)
    x = input('QUAL VOCAÇÃO DESEJA SEGUIR ? > ')
    
    # Encontrar a classe correspondente
    classe_selecionada = None
    for c in categorias['classe']:
        if c.startswith(x + ' >'):
            classe_selecionada = c
            break
    
    if classe_selecionada:
        print('VOCÊ ESTÁ TREINANDO ! 💪 ')
        sleep(3)
        print(f'VOCÊ ESTÁ APTO PARA SER UM {classe_selecionada[4:]}')
        # Atualizar o player com os valores da classe selecionada
        player.update({
        'vida': categorias[classe_selecionada]['vida'],
        'vida_min': categorias[classe_selecionada]['vida_min'],
        'vida_max': categorias[classe_selecionada]['vida_max'],
        'dano': categorias[classe_selecionada]['dano'],
        'dano_base':categorias[classe_selecionada]['dano_base'],
        'golpes': categorias[classe_selecionada]['golpes'],
        'armas': categorias[classe_selecionada]['armas'],
        'mana': categorias[classe_selecionada]['mana'],
        'mana_inicial': categorias[classe_selecionada]['mana_inicial'],
        'mana_max': categorias[classe_selecionada]['mana_max'],
        'cura': categorias[classe_selecionada]['cura'],
        'classe': classe_selecionada,
        'inventario': categorias[classe_selecionada]['inventario'],
        })
        
        print(f"SEUS STATUS FORAM ATUALIZADOS")
        sleep(5)
        clear_terminal()
        Hud_player()
        escolha_arma()
    else:
        print('PARA DE GRAÇA E ESCOLHE UMA QUE EXISTE VEI ')
        print('')
        escolha_classe()

def determinar_classe_tipo(classe):
    if classe in Furtivo['classe']:
        return 'Furtivo'
    elif classe in Magias['classe']:
        return 'Magias'
    elif classe in Corpo_a_corpo['classe']:
        return 'Corpo_a_corpo'
    return None

def equip_arma(p, arma_nome):
    gerar_raridades_itens(armas, consumiveis, equipamentos)
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


    
    

# Funções específicas para equipar armas
def equip_adaga():    
    equip_arma(player, 'adaga')

def equip_espada_curta():    
    equip_arma(player, 'espada_curta')

def equip_cajado():    
    equip_arma(player, 'cajado')

def equip_varinha():    
    equip_arma(player, 'varinha')

def equip_machado():    
    equip_arma(player, 'machado')

#Funções especificas para equipar armaduras

def equip_cap():
    equip_armadura(player, 'capacete')
def equip_pet():
    equip_armadura(player, 'peitoral')
def equip_cal():
    equip_armadura(player, 'calca')
def equip_bot():
    equip_armadura(player, 'bota')




def escolha_arma():
    print('')
    print("ESCOLHE UMA ARMA PRA VOCÊ NÃO SAIR DE MÃOS VAZIAS ")
    print('')
    desc_armas()
    print('')
    x = int(input('1) ADAGA | 2) ESPADA_CURTA | 3) CAJADO | 4) VARINHA | 5) MACHADO |'))
    if x == 1:
        equip_adaga()
        Hud_player()
    elif x ==2:
        equip_espada_curta()
        Hud_player()
    elif x == 3:
        equip_cajado()
        Hud_player()
    elif x == 4:
        equip_varinha()
        Hud_player()
    elif x == 5:
        equip_machado()
        Hud_player()
    else:
        print('NÃO TEM MAIS NENHUMA POR AQUI, PEGA QUALQUER UMA QUE VOCÊ ESTÁ VENDO.')
        escolha_arma()
        
#escolha_classe()