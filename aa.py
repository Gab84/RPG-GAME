from Itens import * 
from Textos import Hud_player, desc_itens,txt_lj_i,txt_lj_a,txt_lj_ar,desc_armaduras
from classes import*
from time import sleep

l_itens_bathemofh = [
    armas['adaga']['nome_colorido'],
    armas['espada_curta']['nome_colorido'],
    armas['cajado']['nome_colorido'],
    armas['varinha']['nome_colorido'],
    armas['machado']['nome_colorido']
]


loja_Bathemofh = {
    #nome do npc
    'nome' : 'Bathemofh',
    'itens' : l_itens_bathemofh,
    'preco' : ['adaga : 10','espada_curta : 15','cajado : 10','varinha : 10','machado : 20',]
}



def xhama():
    l_itens_bathemofh = [
    armas['adaga']['nome_colorido'],
    armas['espada_curta']['nome_colorido'],
    armas['cajado']['nome_colorido'],
    armas['varinha']['nome_colorido'],
    armas['machado']['nome_colorido']
                    ]
    loja_Bathemofh.update({
        'itens': l_itens_bathemofh})



def loja_a(npc):
    gerar_raridades_itens(armas, equipamentos)
    xhama()
    txt_lj_a()
    print('================================================================')
    sleep(2)
    print(f"VOCÊ ENCONTROU A LOJA DO  >> \033[32m{npc['nome']} <<\033[0m ")
    print('')
    print("\033[31mVOCÊ SÓ PODE COMPRAR UM ITEM POR ENCONTRO, ESCOLHA COM SABEDORIA.\033[0m")
    print('')
    print(f"Sua bagagem é >> INVENTARIO 🎒 : {player['armas']} | Dinheiro 💰 : {player['dinheiro']}")
    print(f'\nItens da loja são: ')
    print(f'Debug: npc["itens"] = {npc["itens"]}')
    for i, c in enumerate(npc['itens']):
        print(f'{i+1} - {c}')
    desc_armas()
    x = int(input(f"\n\033[32mVAI LEVAR OQUE HOJE ? ->  \033[0m"))-1
    if 0 <= x < len(npc['itens']):
        item_desejado = npc['itens'][x]
        if player['dinheiro'] >= armas[item_desejado]['preco']:
            sleep(1)
            print('CONFERINDO O TROCO 💸')
            sleep(1)
            print("VOCÊ COMPROU :", item_desejado)
            sleep(2)
            npc['itens'].pop(x)
            player['pontos'] += armas[item_desejado]['pontos']
            if armas[item_desejado]['nome'] == 'adaga':
                equip_adaga()
            elif armas[item_desejado]['nome'] == 'espada_curta':
                equip_espada_curta()
            elif armas[item_desejado]['nome'] == 'cajado':
                equip_cajado()
            elif armas[item_desejado]['nome'] == 'varinha':
                equip_varinha()
            elif armas[item_desejado]['nome'] == 'machado':
                equip_machado()
            print(f"{armas[item_desejado]['nome']} FOI ADICIONADA A MÃO DO PLAYER, PARABÉNS PELA AQUISIÇÃO. BOA SORTE NA VIAGEM. ")
            player['dinheiro'] -= armas[item_desejado]['preco']
            sleep(2)
            Hud_player()
        else:
            print('RAPAZ, TU TA SEM GRANA, ESCOLHE OUTRA COISA...')
            loja_a(npc=loja_Bathemofh)
    else:
        print("JÁ QUE VOCÊ NÃO QUER NADA, ADEUS. ")



loja_a(npc=loja_Bathemofh)