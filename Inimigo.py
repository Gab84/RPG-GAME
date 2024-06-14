from random import randint
from Player import *

def lx():
  global level
  level = randint(1,2)  #master piece
  level += player['level']
lx()

level = (player['level'] *2)

print(level)


#definindo os atb do inimigo tbm
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
  }



def reset_inimigos():
  lx()

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