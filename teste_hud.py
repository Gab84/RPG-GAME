from rich.console import Console 
from rich.panel import Panel
from rich.text import Text
from rich.box import *
from Player import player
from Inimigo import *
from rich.box import ROUNDED
from rich.table import Table
from rich.emoji import Emoji
from rich.align import Align
from Textos import *
from classes import * 
from Raridadesf import *
#from Acoes import combate_MagoObscuro

equip_adaga_i()
gerar_raridades_itens(equipamentos, armas)
equip_bot()
equip_cap()
equip_pet()
equip_cal()

print(player)


Hud_player()
tamanho = 0
for c in player['armaduras_equipadas']:
    for letra in c:
        tamanho += len(letra)
print(tamanho)


#combate_MagoObscuro()
