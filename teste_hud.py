from rich.console import Console 
from rich.panel import Panel
from rich.text import Text
from rich.box import *
from Player import player
from Inimigo import *
import time
import sys
from Itens import *
from Textos import *
from classes import *
from rich.box import ROUNDED
from rich.table import Table
from rich.emoji import Emoji
from rich.align import Align



def player_hud():
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
        width = 113,
        padding=(-1,3),
    )

    # limpeza nome da classe:
    nome_classe_limpa = player['classe'][0].replace("1",'').replace('2','').strip().replace('>','').strip()
    # separador de milhar:
    dinheiro_limpo = f'{player['dinheiro']:<10,.0f}'.replace(',','.')
    # impressão de itens do inventário sem as aspas
    itens_inventario = ', '.join(player['inventario'])

    tabela.add_column() 
    tabela.add_row(f'{'[b]PAINEL PLAYER[/b]':^106}\n')
    tabela.add_row(f"[b]NM[/b] 👤: [white  ]{player['nome'].upper()[0:20]:<20}[/]  [b]LV[/b]{f'[yellow]:star: {player['level']:<4}[/yellow]'}     [b]CLASSE[/b]: {nome_classe_limpa:<12}[b]ARMA[/]: {player['armas']['nome_colorido']:>15}      [white b]CASH[/]: [i]💲{dinheiro_limpo}[/]")
    tabela.add_row(f"[b]HP[/] {player_hp_bar:<10}     [red i]{player['vida']:>3} / {player['vida_max']:<3}[/]      [b]EQ[/]: {', '.join(armaduras_equipadas) if armaduras_equipadas else 'sem armadura...':<50}         [b]DEF[/]🔰: {player['defesa']:>3}/{player['defesa_max']:<3}")
    tabela.add_row(f"[b]MP[/] {player_mana_bar:<10}     [cyan i]{player['mana']:>3} / {player['mana_max']:<3}[/]                  ")
    tabela.add_row(f"[b]XP[/] {player_xp_bar:<10}     [#ffA500 i]{player['exp']:>3} / {player['exp_max']:<3}[/]      📦 [b]INVENTARIO[/b]: {itens_inventario[0:40]}...")
    tabela.add_section()

    tabela_centralizada = Align.center(tabela)

    c.print(tabela_centralizada)