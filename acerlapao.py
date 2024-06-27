dano_MagoObscuro = dano_multiplier * 2.5
dano_MagoObscuro2 = dano_multiplier * 3.5
vida_MagoObscuro = vida_multiplier
xp_MagoObscuro = xp_multiplier * 0.4


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



def combate_MagoObscuro():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         p_atq_1=player['golpes'][0],
         p_atq_2=player['golpes'][1],
         inimigo='MagoObscuro',
         i_vida=MagoObscuro['vida'],
         i_dano=MagoObscuro['dano'],
         i_dano2=MagoObscuro['dano2'],
         i_xp= MagoObscuro['exp'],
         i_level=MagoObscuro['level'],
         p_vida_m=player['vida_max'],
         i_vida_m=MagoObscuro['vida_max'],
         i_pt=(MagoObscuro['pontos']*MagoObscuro['level'])
         )
