from Player import player
from Inimigo import *
import time
import sys
from Itens import *
from rich import *
from rich.console import Console 
from rich.panel import Panel
from rich.text import Text
from rich.box import *
from rich.box import ROUNDED
from rich.table import Table
from rich.emoji import Emoji
from rich.align import Align
import threading
import keyboard






def calcular_defesa_total(p):
    defesa_total = 0
    for armadura in p['armaduras_equipadas']:
        defesa_total += armadura['def']
    return defesa_total
    
#isso é um puta de um comentário ooooooooooooooooooooooooooooooooooooooooooooooooooo

def display_npc_hp_bar(current_hp, max_hp,inimigo,i_level,i_xp, bar_length=10):
    ratio = current_hp / max_hp

    white_squares = int(ratio * bar_length)
    black_squares = bar_length - white_squares

    npc_hp_bar = "❤️ " * white_squares + "🤍" * black_squares
    print(f"""------------------------------
INIMIGO 💀 : \033[91m{inimigo}\033[0m 
------------------------------
Vida: {npc_hp_bar} 
            {current_hp}/{max_hp}           
Nivel 🌟 : {i_level} | Exp 📚 : {i_xp} 
            """)
    
    return npc_hp_bar

def display_player_hp_bar(current_hp, max_hp, bar_length=10):
    ratio = current_hp / max_hp

    white_squares = int(ratio * bar_length)
    black_squares = bar_length - white_squares

    player_hp_bar = "[white]:heartpulse:[/white]" * white_squares + " :white_medium_square:" * black_squares

    #print(f"\033[36m{player['nome']}\033[0m {player_hp_bar}  ")
    

    return player_hp_bar

def xp_bar(xp_atual,xp_max,bar_lenght=10):
    ratio = xp_atual / xp_max

    white_squares = int(ratio * bar_lenght)
    black_squares = bar_lenght - white_squares

    player_xp_bar = ":large_orange_diamond:" * white_squares + " :white_medium_square:" * black_squares

    #print(f"\033[36m{player['nome']}\033[0m {player_xp_bar}  ")
    
    
    return player_xp_bar    

def mana_bar(man_atual,mana_max,bar_lenght=10):
    ratio = man_atual / mana_max

    white_squares = int(ratio * bar_lenght)
    black_squares = bar_lenght - white_squares

    player_mana_bar = ':large_blue_circle:' * white_squares + " :white_medium_square:" * black_squares

    #print(f"\033[36m{player['nome']}\033[0m {player_xp_bar}  ")
    
    
    return player_mana_bar    



def Hud_player():
    c = Console()
    t = Text()
    
    player_mana_bar = mana_bar(man_atual=player['mana'], mana_max=player['mana_max'])
    player_xp_bar = xp_bar(xp_atual=player['exp'], xp_max=player['exp_max'])
    player_hp_bar = display_player_hp_bar(current_hp=player['vida'], max_hp=player['vida_max'])
    armaduras_equipadas = [armadura['nome_colorido'] for armadura in player['armaduras_equipadas'].values()]

    tabela = Table(
        box=ROUNDED,
        show_header=False,
        show_edge=True,
        show_lines=False,
        width = 114,
        padding=(-1,3),
    )

    # limpeza nome da classe:
    nome_classe_limpa = player['classe'][0].replace("1",'').replace('2','').strip().replace('>','').strip()
    # separador de milhar:
    dinheiro_limpo = f"{player['dinheiro']:<10,.0f}".replace(',','.')
    # impressão de itens do inventário sem as aspas
    itens_inventario = ', '.join(player['inventario'])
    # print do equipamento
    armadura = (', '.join(armaduras_equipadas) if armaduras_equipadas else 'sem armadura')
    # tamanho do inventário
    tot_inv = sum(len(item) for item in player['inventario'])

    
    tabela.add_column() 
    tabela.add_row(f"{'[b]PAINEL PLAYER[/b]':^106}\n")
    tabela.add_row(f"[b]NM[/b] 👤: {player['nome'].upper()[0:17]:<20}  [b]LV:[/b][yellow]:star: {player['level']:<4}[/yellow]     [b]CLASSE[/b]: {nome_classe_limpa:<12}   [b]ARMA[/]: {player['armas']['nome_colorido']:<15}[white b]CASH[/]:[i green]💲 {dinheiro_limpo}[/]")
    tabela.add_row(f"[b]HP[/] {player_hp_bar:<10}     [red i]{player['vida']:>3} / {player['vida_max']:<3}[/]       [b]EQ[/b]: {armadura}                                    [b]DEF[/b]🔰:{player['defesa']:>3}/{player['defesa_max']:<3}")
    tabela.add_row(f"[b]MP[/] {player_mana_bar:<10}     [cyan i]{player['mana']:>3} / {player['mana_max']:<3}[/]                  ")
    tabela.add_row(f"[b]XP[/] {player_xp_bar:<10}     [#ffA500 i]{player['exp']:>3} / {player['exp_max']:<3}[/]     📦 [b]INVENTARIO[/b]: {itens_inventario if tot_inv <= 40 else itens_inventario[0:40]+'...'}")
    tabela.add_section()

    # linha equipamento e defesa antiga
    '''tabela.add_row(f"[b]HP[/] {player_hp_bar:<10}     [red i]{player['vida']:>3} / {player['vida_max']:<3}[/]     [b]EQ[/]: {armadura}                                    [b]DEF[/]🔰:{player['defesa']:>3}/{player['defesa_max']:<3}")'''

    tabela_centralizada = Align.center(tabela)

    c.print(tabela_centralizada)




def Hud_inimigo(i_nome,i_vida,i_vida_m,i_level,i_xp):
    npc_hp_bar=display_npc_hp_bar(current_hp=i_vida,max_hp=i_vida_m)
    print(f"Inimigo: {i_nome} | Vida: {i_vida} {npc_hp_bar} | Nivel: {i_level} | Exp: {i_xp} |")

def Hud_inimigo_gb():
    Hud_inimigo(i_nome=Goblin['nome'],i_vida=Goblin['vida'],i_level=Goblin['level'],i_xp=Goblin['exp'])

def Hud_inimigo_orc():
    Hud_inimigo(i_nome=Orc_caverna['nome'],i_vida=Orc_caverna['vida'],i_level=Orc_caverna['level'],i_xp=Orc_caverna['exp'])

def Hud_inimigo_mf():
    Hud_inimigo(i_nome=Monstro_floresta['nome'],i_vida=Monstro_floresta['vida'],i_level=Monstro_floresta['level'],i_xp=Monstro_floresta['exp'])

def Hud_inimigo_bd():
    Hud_inimigo(i_nome=Bandido['nome'],i_vida=Bandido['vida'],i_level=Bandido['level'],i_xp=Bandido['exp'])
    
def Hud_inimigo_banche():
    Hud_inimigo(i_nome=Banche['nome'],i_vida=Banche['vida'],i_level=Banche['level'],i_xp=Banche['exp'])


def desc_Furtivo():
    print(f"BANDIDO  > \nVIDA : 40/80 |\nDANO: 7/5 |\nGOLPES : GOLPE_BASICO | GOLPE_FORTE | CURA |\nMANA : 50/100 | ")
    print("")
    print(f"GNOMO  > \nVIDA : 40/80 |\nDANO: 7/5 |\nGOLPES : GOLPE_BASICO | GOLPE_FORTE | CURA |\nMANA : 50/100 | ")
def desc_magia():
    pass
def desc_corpo_corpo():
    pass

def desc_armas_i():
    print('')
    print(f"ADAGA > DANO: 7/11  |\nESPADA_CURTA > DANO: 15/20  |\nCAJADO > DANO: 15/23  |\nVARINHA > DANO: 10/20  |\nMACHADO > DANO: 25/35  ")


def desc_armas():
    print('')
    print(f"{armas['adaga']['nome_colorido']} > DANO: {armas['adaga']['dano']} PREÇO: {armas['adaga']['preco']} |\n{armas['espada_curta']['nome_colorido']} > DANO: {armas['espada_curta']['dano']} PREÇO: {armas['espada_curta']['preco']} |\n{armas['cajado']['nome_colorido']} > DANO: {armas['cajado']['dano']} PREÇO: {armas['cajado']['preco']} |\n{armas['varinha']['nome_colorido']} > DANO: {armas['varinha']['dano']} PREÇO: {armas['varinha']['preco']} |\n{armas['machado']['nome_colorido']} > DANO: {armas['machado']['dano']} PREÇO: {armas['machado']['preco']} ")

def desc_armaduras():
    print('')
    print(f"{equipamentos['capacete']['nome_colorido']} > DEFESA: {equipamentos['capacete']['def']} PREÇO: {equipamentos['capacete']['preco']} |\n{equipamentos['peitoral']['nome_colorido']} > DEFESA: {equipamentos['peitoral']['def']} PREÇO: {equipamentos['peitoral']['preco']} |\n{equipamentos['calca']['nome_colorido']} > DEFESA: {equipamentos['calca']['def']} PREÇO: {equipamentos['calca']['preco']} |\n{equipamentos['bota']['nome_colorido']} > DEFESA: {equipamentos['bota']['def']} PREÇO: {equipamentos['bota']['preco']} |")
def desc_itens():
    print('')
    print(f"suco de maça🧃 > VIDA: 20 PREÇO: 15 |\ncafezin🥤 > MANA: 20 PREÇO: 10 |")


def txt_btl():
    print(f""" ██▒   █▓ ▒█████   ▄████▄  ▓█████    ▓█████   ██████ ▄▄▄█████▓ ▄▄▄         ▓█████  ███▄ ▄███▓    ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▄▄▄       ██▓     ██░ ██  ▄▄▄      
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒████▄       ▓█   ▀ ▓██▒▀█▀ ██▒   ▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██░ ██▒▒████▄    
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄     ▒███   ▓██    ▓██░   ▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██▀▀██░▒██  ▀█▄  
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██    ▒▓█  ▄ ▒██    ▒██    ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ░▓█ ░██ ░██▄▄▄▄██ 
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ░▒████▒▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒   ░▒████▒▒██▒   ░██▒   ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒░██████▒░▓█▒░██▓ ▓█   ▓██▒
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░   ░░ ▒░ ░░ ▒░   ░  ░   ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░    ░ ░  ░░ ░▒  ░ ░    ░      ▒   ▒▒ ░    ░ ░  ░░  ░      ░   ▒░▒   ░   ▒   ▒▒ ░   ░      ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░▒░ ░  ▒   ▒▒ ░
     ░░  ░ ░ ░ ▒  ░           ░         ░   ░  ░  ░    ░        ░   ▒         ░   ░      ░       ░    ░   ░   ▒    ░        ░   ▒     ░ ░    ░  ░░ ░  ░   ▒   
      ░      ░ ░  ░ ░         ░  ░      ░  ░      ░                 ░  ░      ░  ░       ░       ░            ░  ░              ░  ░    ░  ░ ░  ░  ░      ░  ░
     ░            ░                                                                                   ░                                                       """)



def txt_lj_i():
    print("""▄▄▌         ▐▄▄▄ ▄▄▄·     ·▄▄▄▄  ▄▄▄ .    ▪  ▄▄▄▄▄▄▄▄ . ▐ ▄ .▄▄ · 
██•  ▪       ·██▐█ ▀█     ██▪ ██ ▀▄.▀·    ██ •██  ▀▄.▀·•█▌▐█▐█ ▀. 
██▪   ▄█▀▄ ▪▄ ██▄█▀▀█     ▐█· ▐█▌▐▀▀▪▄    ▐█· ▐█.▪▐▀▀▪▄▐█▐▐▌▄▀▀▀█▄
▐█▌▐▌▐█▌.▐▌▐▌▐█▌▐█ ▪▐▌    ██. ██ ▐█▄▄▌    ▐█▌ ▐█▌·▐█▄▄▌██▐█▌▐█▄▪▐█
.▀▀▀  ▀█▄▀▪ ▀▀▀• ▀  ▀     ▀▀▀▀▀•  ▀▀▀     ▀▀▀ ▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀▀ """)
    
    

def txt_lj_a():
    print(""" ▄█        ▄██████▄       ▄█    ▄████████      ████████▄     ▄████████         ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████
███       ███    ███     ███   ███    ███      ███   ▀███   ███    ███        ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███
███       ███    ███     ███   ███    ███      ███    ███   ███    █▀         ███    ███   ███    ███ ███   ███   ███   ███    ███   ███    █▀ 
███       ███    ███     ███   ███    ███      ███    ███  ▄███▄▄▄            ███    ███  ▄███▄▄▄▄██▀ ███   ███   ███   ███    ███   ███       
███       ███    ███     ███ ▀███████████      ███    ███ ▀▀███▀▀▀          ▀███████████ ▀▀███▀▀▀▀▀   ███   ███   ███ ▀███████████ ▀███████████
███       ███    ███     ███   ███    ███      ███    ███   ███    █▄         ███    ███ ▀███████████ ███   ███   ███   ███    ███          ███
███▌    ▄ ███    ███     ███   ███    ███      ███   ▄███   ███    ███        ███    ███   ███    ███ ███   ███   ███   ███    ███    ▄█    ███
█████▄▄██  ▀██████▀  █▄ ▄███   ███    █▀       ████████▀    ██████████        ███    █▀    ███    ███  ▀█   ███   █▀    ███    █▀   ▄████████▀ 
▀                    ▀▀▀▀▀▀                                                                ███    ███                                          """)

"""Hud_inimigo_gb()
Hud_inimigo_orc()
Hud_inimigo_gb()
Hud_inimigo_gb()"""

#xp_bar(xp_atual=player['exp'],xp_max=player['exp_max'])

#Hud_player()

def txt_lj_ar():
    print(""" █████          ███████          █████   █████████      ██████████   ██████████      █████████   ███████████   ██████   ██████   █████████   ██████████   █████  █████ ███████████     █████████    █████████ 
░░███         ███░░░░░███       ░░███   ███░░░░░███    ░░███░░░░███ ░░███░░░░░█     ███░░░░░███ ░░███░░░░░███ ░░██████ ██████   ███░░░░░███ ░░███░░░░███ ░░███  ░░███ ░░███░░░░░███   ███░░░░░███  ███░░░░░███
 ░███        ███     ░░███       ░███  ░███    ░███     ░███   ░░███ ░███  █ ░     ░███    ░███  ░███    ░███  ░███░█████░███  ░███    ░███  ░███   ░░███ ░███   ░███  ░███    ░███  ░███    ░███ ░███    ░░░ 
 ░███       ░███      ░███       ░███  ░███████████     ░███    ░███ ░██████       ░███████████  ░██████████   ░███░░███ ░███  ░███████████  ░███    ░███ ░███   ░███  ░██████████   ░███████████ ░░█████████ 
 ░███       ░███      ░███       ░███  ░███░░░░░███     ░███    ░███ ░███░░█       ░███░░░░░███  ░███░░░░░███  ░███ ░░░  ░███  ░███░░░░░███  ░███    ░███ ░███   ░███  ░███░░░░░███  ░███░░░░░███  ░░░░░░░░███
 ░███      █░░███     ███  ███   ░███  ░███    ░███     ░███    ███  ░███ ░   █    ░███    ░███  ░███    ░███  ░███      ░███  ░███    ░███  ░███    ███  ░███   ░███  ░███    ░███  ░███    ░███  ███    ░███
 ███████████ ░░░███████░  ░░████████   █████   █████    ██████████   ██████████    █████   █████ █████   █████ █████     █████ █████   █████ ██████████   ░░████████   █████   █████ █████   █████░░█████████ 
░░░░░░░░░░░    ░░░░░░░     ░░░░░░░░   ░░░░░   ░░░░░    ░░░░░░░░░░   ░░░░░░░░░░    ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░     ░░░░░░░░   ░░░░░   ░░░░░ ░░░░░   ░░░░░  ░░░░░░░░░  """)

def txt_str():
    print(""" 

▄▀▀▀▀▄  ▄▀▀█▄   ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄ 
█ █   ▐ ▐ ▄▀ ▀▄ █ █    ▌ █   █   █ ▐ ▄▀ ▀▄ █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █    █  ▐ █      █
   ▀▄     █▄▄▄█ ▐ █      ▐  █▀▀█▀    █▄▄▄█ ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐   █     █      █
▀▄   █   ▄▀   █   █       ▄▀    █   ▄▀   █   █    █    █    ▌    █   █     █      ▀▄    ▄▀
 █▀▀▀   █   ▄▀   ▄▀▄▄▄▄▀ █     █   █   ▄▀  ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █    ▄▀         ▀▀▀▀  
 ▐      ▐   ▐   █     ▐  ▐     ▐   ▐   ▐   █    █     █    ▐   █    ▐   █                 
                ▐                          ▐    ▐     ▐        ▐        ▐                 
                
                                                                                                    Versão de TESTES 
                                                                                                    
          """)




def txtlore(text, delay=0.1):
    def print_text():
        for char in text:
            if keyboard.is_pressed('tab'):
                sys.stdout.write(text[printed_chars:])
                sys.stdout.flush()
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    printed_chars = 0
    text_thread = threading.Thread(target=print_text)
    text_thread.start()
    text_thread.join()
    

#txtlore("TEXTO", delay=0.05)