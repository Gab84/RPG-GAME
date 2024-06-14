# texto para modificar

'''print(f"""------------------------------
JOGADOR 👤 : {player['nome']} 
------------------------------
Vida: {player_hp_bar} | Mana: {player_mana_bar} 
            {player['vida']}/{player['vida_max']}                       {player['mana']}/{player['mana_max']}                
------------------------------
Armaduras 🛡️ : {', '.join(armaduras_equipadas) if armaduras_equipadas else 'Nenhuma'} | INVENTÁRIO 🎒 : {player['inventario']} | Dinheiro 💰 : {player['dinheiro']}

Arma ⚔️ : {armap}

Nível 🌟 : {player['level']} | Exp 📚 : {player['exp']}/{player['exp_max']} {player_xp_bar} 

Classe 🏋️‍♀️ : {player['classe']}

Defesa Total 🛡️ : {defesa_total}

AÇÕES -->  {player['golpes'][0]}🗡️  : DANO : {player['dano'][0]} ❤️  | {player['golpes'][1]}🗡️  : DANO : {player['dano'][1]} ❤️  | {player['golpes'][2]} 🩹 : CURA: {player['cura']} ❤️  | {player['golpes'][3]}🎒 : ABRIR INVENTÁRIO
------------------------------""")'''
from rich.console import Console 
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED, DOUBLE, ASCII, SIMPLE
from Player import player
from Inimigo import *
import time
import sys
from Itens import *
from Textos import *
from classes import *


c = Console()
t = Text()


equip_adaga_i()
player_mana_bar = mana_bar(man_atual=player['mana'], mana_max=player['mana_max'])
player_xp_bar = xp_bar(xp_atual=player['exp'], xp_max=player['exp_max'])
player_hp_bar = display_player_hp_bar(current_hp=player['vida'], max_hp=player['vida_max'])    
armaduras_equipadas = [armadura['nome_colorido'] for armadura in player['armaduras_equipadas'].values()]
defesa_total = player['defesa']
armap = player['armas']['nome_colorido']


t = f"""JOGADOR 👤 : {player['nome']} 

Vida: {player_hp_bar} | Mana: {player_mana_bar} 
            {player['vida']}/{player['vida_max']}                       {player['mana']}/{player['mana_max']}                

Armaduras 🛡️ : {', '.join(armaduras_equipadas) if armaduras_equipadas else 'Nenhuma'} | INVENTÁRIO 🎒 :
{player['inventario']} | Dinheiro 💰 : {player['dinheiro']}

Arma ⚔️ : {armap}

Nível 🌟 : {player['level']} | Exp 📚 : {player['exp']}/{player['exp_max']} {player_xp_bar}

Classe 🏋️‍♀️ : {player['classe']}

Defesa Total 🛡️ : {defesa_total}

AÇÕES -->  {player['golpes'][0]}🗡️  : DANO : {player['dano'][0]} ❤️  | {player['golpes'][1]}🗡️  : DANO :{player['dano'][1]} ❤️  | {player['golpes'][2]} 🩹 : CURA: {player['cura']} ❤️  | {player['golpes'][3]}🎒 : ABRIR INVENTÁRIO"""



p = Panel(
    t,
    style='white b',
    title="HUD PLAYER 2.0",
    border_style='white',
    title_align="center",
    subtitle="Exemplo de subtítulo",
    expand=False,
    box=ROUNDED
)

c.print(p)
