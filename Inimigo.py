from random import randint
from Player import *
from rich import *



#print(level)

#definindo os atb do inimigo tbm

level = player['level']

dano_multiplier = level * 1.5
vida_multiplier = level * 2
xp_multiplier = level * 1.6

dano_Mf = dano_multiplier * 15
dano_bd = dano_multiplier * 7
dano_orc = dano_multiplier * 30
dano_Mf2 = dano_multiplier * 20
dano_bd2 = dano_multiplier * 9
dano_orc2 = dano_multiplier * 35

vida_mf = (vida_multiplier + 30) * 2
vida_bd = (vida_multiplier + 15) * 2
vida_orc = (vida_multiplier + 30) * 3

xp_mf = xp_multiplier * 40
xp_bd = xp_multiplier * 25
xp_orc = xp_multiplier * 60

dano_goblin = dano_multiplier * 6
dano_goblin2 = dano_multiplier * 8
vida_goblin = (vida_multiplier + 30) * 3
xp_goblin = xp_multiplier * 20

dano_Banche = dano_multiplier * 2.5
dano_Banche2 = dano_multiplier * 3.5
vida_Banche = (vida_multiplier + 30) * 3
xp_Banche = xp_multiplier * 34

dano_dragao = dano_multiplier * 30
dano_dragao2 = dano_multiplier * 35
vida_dragao = (vida_multiplier + 30) * 3
xp_dragao = xp_multiplier * 40

dano_MagoObscuro = dano_multiplier * 25
dano_MagoObscuro2 = dano_multiplier * 30
vida_MagoObscuro = vida_multiplier  * 20
xp_MagoObscuro = xp_multiplier * 30



Monstro_floresta = {
    'nome': 'Monstro da Floresta',
    'level': level,
    'dano': dano_Mf,
    'dano2': dano_Mf2,
    'vida': vida_mf,
    'vida_max': vida_mf,
    'exp': xp_mf,
    'vida_min': 0,
    'pontos': 60
}

Bandido = {
    'nome': 'Bandido',
    'level': level,
    'dano': dano_bd,
    'dano2': dano_bd2,
    'vida': vida_bd,
    'vida_max': vida_bd,
    'exp': xp_bd,
    'vida_min': 0,
    'pontos': 40
}

Orc_caverna = {
    'nome': 'Orc_caverna',
    'level': level,
    'dano': dano_orc,
    'dano2': dano_orc2,
    'vida': vida_orc,
    'vida_max': vida_orc,
    'exp': xp_orc,
    'vida_min': 0,
    'pontos': 80
}

Goblin = {
    'nome': 'Goblin',
    'level': level,
    'dano': dano_goblin,
    'dano2': dano_goblin2,
    'vida': vida_goblin,
    'vida_max': vida_goblin,
    'exp': xp_goblin,
    'vida_min': 0,
    'pontos': 30
}

Banche = {
    'nome': 'Banche',
    'level': level,
    'dano': dano_Banche,
    'dano2': dano_Banche2,
    'vida': vida_Banche,
    'vida_max': vida_Banche,
    'exp': xp_Banche,
    'vida_min': 0,
    'pontos': 100
}

dragao = {
    'nome': 'dragao',
    'level': level,
    'dano': dano_dragao,
    'dano2': dano_dragao2,
    'vida': vida_dragao,
    'vida_max': vida_dragao,
    'exp': xp_dragao,
    'vida_min': 0,
    'pontos': 100
}
MagoObscuro = {
    'nome': 'MagoObscuro',
    'level': level,
    'dano': dano_MagoObscuro,
    'dano2': dano_MagoObscuro2,
    'vida': vida_MagoObscuro,
    'vida_max': vida_MagoObscuro,
    'exp': xp_MagoObscuro,
    'vida_min': 0,
    'pontos': 100
}


def reset_inimigos():
  global level
  level = player['level']
  
  Banche.update({
      'nome': Banche['nome'],
      'level': Banche['level'],
      'vida': Banche['vida'],
      'vida_min': 0,
      'vida_max': Banche['vida_max'],
      'dano': Banche['dano'],
      'dano2':  Banche['dano2'],
      
      'exp' : Banche['exp'],

  })

  Goblin.update({
      'nome': Goblin['nome'],
      'level': Goblin['level'],
      'vida': Goblin['vida'],
      'vida_min': 0,
      'vida_max': Goblin['vida_max'],
      'dano': Goblin['dano'],
      'dano2':  Goblin['dano2'],
      
      'exp' : Goblin['exp'],

  })
  Monstro_floresta.update({
      'nome': Monstro_floresta['nome'],
      'level': Monstro_floresta['level'],
      'vida': Monstro_floresta['vida'],
      'vida_min': 0,
      'vida_max': Monstro_floresta['vida_max'],
      'dano': Monstro_floresta['dano'],
      'dano2':  Monstro_floresta['dano2'],
      
      'exp' : Monstro_floresta['exp'],

  })
  Orc_caverna.update({
      'nome': Orc_caverna['nome'],
      'level': Orc_caverna['level'],
      'vida': Orc_caverna['vida'],
      'vida_min': 0,
      'vida_max': Orc_caverna['vida_max'],
      'dano': Orc_caverna['dano'],
      'dano2':  Orc_caverna['dano2'],
      
      'exp' : Orc_caverna['exp'],

  })
  Bandido.update({
      'nome': Bandido['nome'],
      'level': Bandido['level'],
      'vida': Bandido['vida'],
      'vida_min': 0,
      'vida_max': Bandido['vida_max'],
      'dano': Bandido['dano'],
      'dano2':  Bandido['dano2'],
      
      'exp' : Bandido['exp'],

  })
  dragao.update({
      'nome': dragao['nome'],
      'level': dragao['level'],
      'vida': dragao['vida'],
      'vida_min': 0,
      'vida_max': dragao['vida_max'],
      'dano': dragao['dano'],
      'dano2':  dragao['dano2'],
      
      'exp' : dragao['exp'],

  })
  MagoObscuro.update({
      'nome': MagoObscuro['nome'],
      'level': MagoObscuro['level'],
      'vida': MagoObscuro['vida'],
      'vida_min': 0,
      'vida_max': MagoObscuro['vida_max'],
      'dano': MagoObscuro['dano'],
      'dano2':  MagoObscuro['dano2'],
      
      'exp' : MagoObscuro['exp'],

  })
  
  


print(dragao)
  


#VERSÃO ANTIGA DOS INIMIGOS CASO ALGO TENHA FICADO ERRADO

"""
def lx():
  global level
  level = randint(1,2)  #master piece
  level += player['level']

level = (player['level'] *2)

for x in range(10):
  player['level'] +=1
  
level = 0
def nv_inimigo():
  global level
  x = player['level']
  y = x * 2
  level = y
  return level
  

nv_inimigo() 


nv_inimigo() 
print(level)



dano_Mf = 7*level
dano_bd = 3*level
dano_orc = 11*level
dano_Mf2 = 9*level
dano_bd2 = 4*level
dano_orc2 = 15*level
vida_mf = 40*level
vida_bd = 20*level
vida_orc = 40*level
xp_mf = 8*level
xp_bd = 7*level
xp_orc = 13*level

dano_goblin = 2*level
dano_goblin2 = 3*level
vida_goblin = 5*level
xp_goblin = 3*level

dano_Banche = 15*level
dano_Banche2 = 20*level
vida_Banche = 20*level
xp_Banche = 9*level
    


Monstro_floresta = {
      'nome': 'Monstro da Floresta',
      'level': level,
      'dano': dano_Mf,
      'dano2': dano_Mf2,
      'vida': vida_mf,
      'vida_max' : vida_mf,
      'exp' : xp_mf,
      'vida_min' : 0,
      'pontos' : 60
  }

Bandido = {
      'nome': 'Bandido',
      'level': level,
      'dano': dano_bd,
      'dano2': dano_bd2,
      'vida': vida_bd,
      'vida_max' : vida_bd,
      'exp' : xp_bd,
      'vida_min' : 0,
      'pontos' : 40
  }

Orc_caverna = {
      'nome': 'Orc_caverna',
      'level': level,
      'dano': dano_orc,
      'dano2': dano_orc2,
      'vida': vida_orc,
      'vida_max' : vida_orc,
      'exp' : xp_orc,
      'vida_min' : 0,
      'pontos' : 80
  }

Goblin = {
      'nome': 'Goblin',
      'level': level,
      'dano': dano_goblin,
      'dano2': dano_goblin2,
      'vida': vida_goblin,
      'vida_max' : vida_goblin,
      'exp' : xp_goblin,
      'vida_min' : 0,
      'pontos' : 30
  }

Banche = {
      'nome': 'Banche',
      'level': level,
      'dano': dano_Banche,
      'dano2': dano_Banche2,
      'vida': vida_Banche,
      'vida_max' : vida_Banche,
      'exp' : xp_Banche,
      'vida_min' : 0,
      'pontos' : 100
  }"""