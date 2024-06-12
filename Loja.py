from Itens import * 
from Textos import Hud_player, desc_itens,txt_lj_i,txt_lj_a,txt_lj_ar,desc_armaduras
from classes import*
from time import sleep

l_itens_alexandre = ['suco_maça', 'cafezin',]
l_itens_bathemofh = []
l_itens_Bartolomeu = []


loja_Alexandre = {
    #nome do npc
    'nome' : 'Alexandre',
    'itens' : l_itens_alexandre,
}
loja_Bathemofh = {
    #nome do npc
    'nome' : 'Bathemofh',
    'itens' : l_itens_bathemofh,
}
loja_Bartolomeu = {
    #nome do npc
    'nome' : 'Bartolomeu',
    'itens' : l_itens_Bartolomeu,
}

#Updates
def update_armas():
    l_itens_bathemofh = [
    armas['adaga']['nome_colorido'],
    armas['espada_curta']['nome_colorido'],
    armas['cajado']['nome_colorido'],
    armas['varinha']['nome_colorido'],
    armas['machado']['nome_colorido']
                    ]
    loja_Bathemofh.update({
        'itens': l_itens_bathemofh})
    
def update_amaduras():
    l_itens_Bartolomeu = [
    equipamentos['capacete']['nome_colorido'],
    equipamentos['peitoral']['nome_colorido'],
    equipamentos['calca']['nome_colorido'],
    equipamentos['bota']['nome_colorido'],
                    ]
    loja_Bartolomeu.update({
        'itens': l_itens_Bartolomeu})






def loja(npc):
    gerar_raridades_itens(armas, equipamentos)
    txt_lj_i()
    print('================================================================')
    sleep(2)
    print(f"VOCÊ ENCONTROU A LOJA DO  >> \033[32m{npc['nome']} <<\033[0m ")
    print('')
    print("\033[31mVOCÊ SÓ PODE COMPRAR UM ITEM POR ENCONTRO, ESCOLHA COM SABEDORIA.\033[0m")
    print('')
    print(f"Sua bagagem é >> INVENTARIO 🎒 : {player['inventario']} | Dinheiro 💰 : {player['dinheiro']}")
    print(f'\nItens da loja são: ')
    for i,c in enumerate(npc['itens']):
        print(f'{i+1} - {c}')
    desc_itens()
    x = int(input(f"\n\033[32mVAI LEVAR OQUE HOJE ? ->  \033[0m"))-1
    if 0 <= x < len(npc['itens']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = npc['itens'][x] # Acessando o item pelo índice fornecido
        if player['dinheiro'] >= consumiveis[item_desejado]['preco'] :
            sleep(1)
            print('CONFERINDO O TROCO 💸')
            sleep(1)
            print("VOCÊ COMPROU :", item_desejado)
            sleep(2)
            # Removendo o item da lista
            npc['itens'].pop(x)
           
            player['pontos'] += consumiveis[item_desejado]['pontos']
            
            #add ao inv player
            player['inventario'].append(item_desejado)
            player['dinheiro'] -= consumiveis[item_desejado]['preco']
            player['pontos'] += consumiveis[item_desejado]['pontos']
            print(f"ITEM FOI ADICIONADO AO INVENTARIO DO PLAYER, BOA SORTE NA SUA VIAGEM. ")
            sleep(3)
            Hud_player()      
        else:
            print('RAPAZ, TU TA SEM GRANA, ESCOLHE OUTRA COISA...')
            loja(npc=loja_Alexandre)
    else:
        print("JÁ QUE VOCÊ NÃO QUER NADA, ADEUS. ")


def loja_a(npc):
    gerar_raridades_itens(armas, equipamentos)
    update_armas()
    txt_lj_a()
    print('================================================================')
    sleep(2)
    print(f"VOCÊ ENCONTROU A LOJA DO  >> \033[32m{npc['nome']} <<\033[0m ")
    print('')
    print("\033[31mVOCÊ SÓ PODE COMPRAR UM ITEM POR ENCONTRO, ESCOLHA COM SABEDORIA.\033[0m")
    print('')
    print(f"Sua bagagem é >> INVENTARIO 🎒 : {player['armas']} | Dinheiro 💰 : {player['dinheiro']}")
    print(f'\nItens da loja são: ')
    for i,c in enumerate(npc['itens']):
        print(f'{i+1} - {c}')
    desc_armas()
    x = int(input(f"\n\033[32mVAI LEVAR OQUE HOJE ? ->  \033[0m"))-1
    if 0 <= x < len(npc['itens']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = npc['itens'][x] # Acessando o item pelo índice fornecido
        if player['dinheiro'] >= armas[item_desejado]['preco'] :
            sleep(1)
            print('CONFERINDO O TROCO 💸')
            sleep(1)
            print("VOCÊ COMPROU :", item_desejado)
            sleep(2)
            # Removendo o item da lista
            npc['itens'].pop(x)
            player['pontos'] += armas[item_desejado]['pontos']
            #add ao inv player
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


def loja_e(npc):
    gerar_raridades_itens(armas, equipamentos)
    update_amaduras()
    txt_lj_ar()
    print('================================================================')
    sleep(2)
    print(f"VOCÊ ENCONTROU A LOJA DO  >> \033[32m{npc['nome']} <<\033[0m ")
    print('')
    print("\033[31mVOCÊ SÓ PODE COMPRAR UM ITEM POR ENCONTRO, ESCOLHA COM SABEDORIA.\033[0m")
    print('')
    print(f"Sua bagagem é >> INVENTARIO 🎒 : {player['armaduras_equipadas']} | Dinheiro 💰 : {player['dinheiro']}")
    print(f'\nItens da loja são: ')
    for i,c in enumerate(npc['itens']):
        print(f'{i+1} - {c}')
    desc_armaduras()
    x = int(input(f"\n\033[32mVAI LEVAR OQUE HOJE ? ->  \033[0m"))-1
    if 0 <= x < len(npc['itens']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = npc['itens'][x] # Acessando o item pelo índice fornecido
        if player['dinheiro'] >= equipamentos[item_desejado]['preco'] :
            sleep(1)
            print('CONFERINDO O TROCO 💸')
            sleep(1)
            print("VOCÊ COMPROU :", item_desejado)
            sleep(2)
            # Removendo o item da lista
            npc['itens'].pop(x)
            player['pontos'] += equipamentos[item_desejado]['pontos']
            #add ao inv player
            if equipamentos[item_desejado]['nome'] == 'capacete':
                equip_cap()
            elif equipamentos[item_desejado]['nome'] == 'peitoral':
                equip_pet()
            elif equipamentos[item_desejado]['nome'] == 'calca':
                equip_cal()
            elif equipamentos[item_desejado]['nome'] == 'bota':
                equip_bot()
            print(f"{equipamentos[item_desejado]['nome']} FOI EQUIPADA NO PLAYER, PARABÉNS PELA AQUISIÇÃO. BOA SORTE NA VIAGEM. ")
            player['dinheiro'] -= equipamentos[item_desejado]['preco']
            sleep(2)
            Hud_player()
        else:
            print('RAPAZ, TU TA SEM GRANA, ESCOLHE OUTRA COISA...')
            loja_e(npc=loja_Bartolomeu)
    else:
        print("JÁ QUE VOCÊ NÃO QUER NADA, ADEUS. ")




gerar_raridades_itens(equipamentos,armas)
print(armas['adaga']['nome_colorido'])



#escolha_classe()


#loja_a(npc=loja_Bathemofh)
#loja(npc=loja_Alexandre)
loja_e(npc=loja_Bartolomeu)
