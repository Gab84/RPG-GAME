from random import randint
from Player import *
from rich import *

level = player['level']

#classe de inimigos

dificuldades = {
  'facil':7,
  'medio':15,
  'dificil':22,
  'level': player['level'],
  'acres':0.1,
  }


def calculo_dano(inimigo):
  global dificuldades
  base = (dificuldades['level']*dificuldades['acres'])+inimigo['dificuldade']-0.1
  return base


def vida(inimigo):
  global dificuldades
  vida_n = (dificuldades['level']*dificuldades['acres'])+inimigo['dificuldade']-0.1
  return vida_n



# calculo de dano base

vida_multiplier = level * 2
xp_multiplier = level * 1.6

vida_mf = (vida_multiplier + 30) * 2
vida_bd = (vida_multiplier + 15) * 2
vida_orc = (vida_multiplier + 30) * 3

xp_mf = xp_multiplier * 40
xp_bd = xp_multiplier * 25
xp_orc = xp_multiplier * 60

vida_goblin = (vida_multiplier + 30) * 3
xp_goblin = xp_multiplier * 20

vida_Banche = (vida_multiplier + 30) * 3
xp_Banche = xp_multiplier * 34

vida_dragao = (vida_multiplier + 30) * 3
xp_dragao = xp_multiplier * 40

vida_MagoObscuro = vida_multiplier  * 20
xp_MagoObscuro = xp_multiplier * 30



# <<<<<<<<<<<<<<<<<<<< Monstros Faceis >>>>>>>>>>>>>>>>>>>>>>>>>

Bandido = {
    'nome': 'Bandido',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['facil'],
    'mult 1':1.2,
    'mult 2':1.5, 
    'base': 0,
    'dano':0,
    'dano2': 0,
    'vida': vida_bd,
    'vida_max': vida_bd,
    'exp': xp_bd,
    'vida_min': 0,
    'pontos': 40,
}

Goblin = {
    'nome': 'Goblin',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['facil'],
    'mult 1':1.6,
    'mult 2':2.0, 
    'base': 0,
    'dano': 0,
    'dano2': 0,
    'vida': vida_goblin,
    'vida_max': vida_goblin,
    'exp': xp_goblin,
    'vida_min': 0,
    'pontos': 30
}

Orc_caverna = {
    'nome': 'Orc_caverna',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['facil'],
    'mult 1':2.0,
    'mult 2':3.0,
    'base': 0,
    'dano': 0,
    'dano2': 0,
    'vida': vida_orc,
    'vida_max': vida_orc,
    'exp': xp_orc,
    'vida_min': 0,
    'pontos': 80
}

# <<<<<<<<<<<<<<<<<<<< Monstros Medios >>>>>>>>>>>>>>>>>>>>>>>>>

Monstro_floresta = {
    'nome': 'Monstro da Floresta',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['medio'],
    'mult 1':2.2,
    'mult 2':2.8,
    'base': 0,
    'dano': 0,
    'dano2': 0,
    'vida': vida_mf,
    'vida_max': vida_mf,
    'exp': xp_mf,
    'vida_min': 0,
    'pontos': 60,
}

Banche = {
    'nome': 'Banche',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['medio'],
    'mult 1':2.9,
    'mult 2':3.5,
    'base': 0,
    'dano': 0,
    'dano2': 0,
    'vida': vida_Banche,
    'vida_max': vida_Banche,
    'exp': xp_Banche,
    'vida_min': 0,
    'pontos': 100
}

# <<<<<<<<<<<<<<<<<<<< Monstros Dificeis >>>>>>>>>>>>>>>>>>>>>>>>>

MagoObscuro = {
    'nome': 'MagoObscuro',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['dificil'],
    'mult 1':2.5,
    'mult 2':2.8,
    'base': 0,
    'dano': 0,
    'dano2': 0,
    'vida': vida_MagoObscuro,
    'vida_max': vida_MagoObscuro,
    'exp': xp_MagoObscuro,
    'vida_min': 0,
    'pontos': 100
}

dragao = {
    'nome': 'dragao',
    'level': dificuldades['level'],
    'dificuldade': dificuldades['dificil'],
    'mult 1':2.9,
    'mult 2':3.2,
    'base': 0,
    'dano': 0,
    'dano2': 0,
    'vida': vida_dragao,
    'vida_max': vida_dragao,
    'exp': xp_dragao,
    'vida_min': 0,
    'pontos': 100
}


# atualização valor dano base

Bandido['base']=(calculo_dano(Bandido))
Goblin['base']=(calculo_dano(Goblin))
Orc_caverna['base']=(calculo_dano(Orc_caverna))
Monstro_floresta['base']=(calculo_dano(Monstro_floresta))
Banche['base']=(calculo_dano(Banche))
MagoObscuro['base']=(calculo_dano(MagoObscuro))
dragao['base']=(calculo_dano(dragao))


# atualização valor dano 1

Bandido['dano']=(Bandido['base']*Bandido['mult 1'])
Goblin['dano']=(Goblin['base']*Goblin['mult 1'])
Orc_caverna['dano']=(Orc_caverna['base']*Orc_caverna['mult 1'])
Monstro_floresta['dano']=(Monstro_floresta['base']*Monstro_floresta['mult 1'])
Banche['dano']=(Banche['base']*Banche['mult 1'])
MagoObscuro['dano']=(MagoObscuro['base']*MagoObscuro['mult 1'])
dragao['dano']=(dragao['base']*dragao['mult 1'])

# atualização valor dano 2

Bandido['dano2']=(Bandido['base']*Bandido['mult 2'])
Goblin['dano2']=(Goblin['base']*Goblin['mult 2'])
Orc_caverna['dano2']=(Orc_caverna['base']*Orc_caverna['mult 2'])
Monstro_floresta['dano2']=(Monstro_floresta['base']*Monstro_floresta['mult 2'])
Banche['dano2']=(Banche['base']*Banche['mult 2'])
MagoObscuro['dano2']=(MagoObscuro['base']*MagoObscuro['mult 2'])
dragao['dano2']=(dragao['base']*dragao['mult 2'])




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
  
  

print(Bandido)
print(Goblin)
print(Orc_caverna)
print(Monstro_floresta)
print(Banche)
print(MagoObscuro)
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