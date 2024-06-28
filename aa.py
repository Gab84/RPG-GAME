from Acoes import *
from Player import player
from time import sleep
from Textos import txtlore
from savescore import *
from Modo_infinito import evnt_aleatorio
from rich import *


def chanc():
    global chanx
    x = randint(1,60)
    chanx = x
    return chanx


def cenario1_corpocorpo_sul():
    print("Capítulo 4: O Santuário da Árvore Sagrada...")
    txtlore(f"Você chega ao Santuário da Árvore Sagrada, um lugar de grande poder espiritual. Aqui, você deve enfrentar um guardião místico para provar seu valor e obter uma bênção poderosa.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Colar Divino' in player['artefatos']:
        print("Com a ajuda do Colar Divino, você enfraquece o guardião místico e o derrota, obtendo mais pontos e uma bênção sagrada.")
        player['pontos'] += 50
        player['artefatos'].append('Bênção da Árvore Sagrada')
    else:
        print("Sem o Colar Divino, você enfrenta o guardião místico com bravura, mas é uma batalha difícil. }")
        player['pontos'] += 30
        combate_mf()
        chanc()
        if chanx <40:
            print("Após a vitória contra o inimigo, você toma a força do artefato")
            player['artefatos'].append('Colar Divino')
            cenario2_corpocorpo_sul()
        else:
            print("Após a vitória contra o inimigo, você toma a força do artefato, mas ele está quebrado")
            cenario2_corpocorpo_sul()

def cenario2_corpocorpo_sul():
    print("Capítulo 5: A Caverna dos Espíritos...")
    txtlore(f"Nas profundezas da caverna, você deve enfrentar espíritos antigos que guardam um tesouro lendário.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Bênção da Árvore Sagrada' in player['artefatos']:
        print("Usando a Bênção da Árvore Sagrada, você purifica os espíritos e obtém o tesouro lendário.")
        player['pontos'] += 100
        player['artefatos'].append('Escudo Espiritual')
    else:
        print("Sem a Bênção da Árvore Sagrada, a luta é difícil, mas sua coragem e habilidades permitem que você derrote os espíritos.")
        player['pontos'] += 70
        combate_Banche()
        combate_Banche()
        chanc()
        if chanx <40:
            print("Após a vitória contra o inimigo, você toma a força do artefato")
            player['artefatos'].append('Bênção da Árvore Sagrada')
            cenario3_corpocorpo_sul()
        else:
            print("Após a vitória contra o inimigo, você toma a força do artefato, mas ele está quebrado")
            cenario3_corpocorpo_sul()
        
    cenario3_corpocorpo_sul()

def cenario3_corpocorpo_sul():
    print("Capítulo 6: O Encontro com o Druida Corrompido...")
    txtlore(f"Em uma clareira sombria, você encontra um druida corrompido que ameaça a floresta com sua magia negra. Para salvar a floresta, você deve derrotá-lo.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Escudo Espiritual' in player['artefatos']:
        print("Com a proteção do Escudo Espiritual, você reflete os feitiços do druida corrompido e o derrota.")
        player['pontos'] += 150
        player['artefatos'].append('Varinha do Druida')
    else:
        print("Sem o Escudo Espiritual, você enfrenta o druida corrompido com sua força, vencendo após uma batalha intensa.")
        player['pontos'] += 100
        combate_mf()
        chanc()
        print("Após a vitória contra o inimigo, você toma a força do artefato")
        player['artefatos'].append('Escudo Espiritual')
        cenario4_corpocorpo_sul()
        

    cenario4_corpocorpo_sul()
    
def cenario4_corpocorpo_sul():
    print("Capítulo 7: A Batalha Final...")
    txtlore(f"Com todos os artefatos em mãos, você lidera um exército para defender a floresta de uma invasão inimiga. A batalha final está prestes a começar.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_bd()
    combate_bd()
    combate_bd()
    combate_bd()
    if 'Varinha do Druida' in player['artefatos']:
        print("Usando a Varinha do Druida, você conjura poderosos feitiços para fortalecer seu exército e derrotar os invasores, garantindo a vitória.")
        player['pontos'] += 200
    else:
        print("Sem a Varinha do Druida, a batalha é difícil, mas sua liderança e habilidades garantem a vitória para a floresta.")
        player['pontos'] += 150
    fim()

def cenario1_magia_sul():
    print("Capítulo 4: O Círculo de Pedras...")
    txtlore(f"Você chega ao Círculo de Pedras, um lugar de grande poder arcano. Aqui, você deve enfrentar um elemental que guarda segredos arcanos.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Colar Divino' in player['artefatos']:
        print("Com a ajuda do Colar Divino, você desvenda os segredos arcanos e derrota o elemental, obtendo mais pontos e um artefato mágico.")
        player['pontos'] += 50
        player['artefatos'].append('Cristal Elemental')
    else:
        print("Sem o Colar Divino, você enfrenta o elemental com sua magia, vencendo após uma batalha intensa.")
        player['pontos'] += 30
    combate_mf()
    cenario2_magia_sul()
    
def cenario2_magia_sul():
    print("Capítulo 5: A Biblioteca Perdida...")
    txtlore(f"Nas profundezas de uma biblioteca antiga, você deve enfrentar guardiões mágicos para obter um poderoso grimório.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_orc()
    if 'Cristal Elemental' in player['artefatos']:
        print("Usando o poder do Cristal Elemental, você neutraliza os guardiões e obtém o grimório.")
        player['pontos'] += 100
        player['artefatos'].append('Grimório da Floresta')
    else:
        print("Sem o Cristal Elemental, a luta é difícil, mas suas habilidades mágicas permitem que você derrote os guardiões.")
        player['pontos'] += 70
    cenario3_magia_sul()
    
def cenario3_magia_sul():
    print("Capítulo 6: O Encontro com o Dragão Verde...")
    txtlore(f"Em uma caverna verdejante, você encontra um dragão verde, guardião de segredos antigos. Para obter seu conhecimento, você deve provar sua sabedoria e poder.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Grimório da Floresta' in player['artefatos']:
        print("Usando os feitiços do Grimório da Floresta, você impressiona o dragão verde e obtém seu conhecimento.")
        player['pontos'] += 150
        player['artefatos'].append('Cristal do Dragão Verde')
    else:
        print("Sem o Grimório da Floresta, você enfrenta o dragão verde com seus poderes, vencendo com sabedoria.")
        player['pontos'] += 100
    cenario4_magia_sul()
    
def cenario4_magia_sul():
    print("Capítulo 7: A Batalha Final...")
    txtlore(f"Com todos os artefatos em mãos, você lidera um exército para defender a floresta de uma invasão inimiga. A batalha final está prestes a começar.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_bd()
    combate_bd()
    combate_bd()
    combate_bd()
    if 'Cristal do Dragão Verde' in player['artefatos']:
        print("Usando o Cristal do Dragão Verde, você conjura poderosos feitiços para fortalecer seu exército e derrotar os invasores, garantindo a vitória.")
        player['pontos'] += 200
    else:
        print("Sem o Cristal do Dragão Verde, a batalha é difícil, mas sua liderança e habilidades mágicas garantem a vitória para a floresta.")
        player['pontos'] += 150
    fim()
    
def cenario1_furtivo_sul():
    print("Capítulo 4: A Clareira dos Ladrões...")
    txtlore(f"Você chega à Clareira dos Ladrões, um lugar de traição e intrigas. Aqui, você deve provar sua habilidade ao enfrentar um chefe de ladrões que guarda riquezas.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Colar Divino' in player['artefatos']:
        print("Com a ajuda do Colar Divino, você derrota o chefe dos ladrões e obtém mais pontos e um artefato mágico.")
        player['pontos'] += 50
        player['artefatos'].append('Adaga Enfeitiçada')
    else:
        print("Sem o Colar Divino, você enfrenta o chefe dos ladrões com suas habilidades, vencendo após uma luta intensa.")
        player['pontos'] += 30
    combate_bd()
    cenario2_furtivo_sul()

def cenario2_furtivo_sul():
    print("Capítulo 5: A Caverna dos Espectros...")
    txtlore(f"Nas profundezas da caverna, você deve enfrentar espectros guardiões para obter um artefato sombrio.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_Banche()
    if 'Adaga Enfeitiçada' in player['artefatos']:
        print("Usando o poder da Adaga Enfeitiçada, você neutraliza os espectros e obtém o artefato sombrio.")
        player['pontos'] += 100
        player['artefatos'].append('Amuleto das Sombras')
    else:
        print("Sem a Adaga Enfeitiçada, a luta é difícil, mas suas habilidades permitem que você derrote os espectros.")
        player['pontos'] += 70
    cenario3_furtivo_sul()
    
def cenario3_furtivo_sul():
    print("Capítulo 6: O Encontro com o Mestre Assassino...")
    txtlore(f"Em uma fortaleza oculta, você encontra o Mestre Assassino, guardião de técnicas secretas. Para obter seu conhecimento, você deve provar sua furtividade e habilidade.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Amuleto das Sombras' in player['artefatos']:
        print("Usando as habilidades do Amuleto das Sombras, você impressiona o Mestre Assassino e obtém seu conhecimento.")
        player['pontos'] += 150
        player['artefatos'].append('Capa das Sombras')
    else:
        print("Sem o Amuleto das Sombras, você enfrenta o Mestre Assassino com suas habilidades, vencendo com precisão.")
        player['pontos'] += 100
    cenario4_furtivo_sul()
    
def cenario4_furtivo_sul():
    print("Capítulo 7: A Batalha Final...")
    txtlore(f"Com todos os artefatos em mãos, você lidera um exército para defender sua vila de uma invasão inimiga. A batalha final está prestes a começar.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_goblin()
    combate_goblin()
    combate_goblin()
    if 'Capa das Sombras' in player['artefatos']:
        print("Usando a Capa das Sombras, você realiza ataques furtivos para enfraquecer os inimigos e garantir a vitória.")
        player['pontos'] += 200
    else:
        print("Sem a Capa das Sombras, a batalha é difícil, mas sua liderança e habilidades garantem a vitória para sua vila.")
        player['pontos'] += 150
    fim()







def cenario1_furtivo():
    print("Capítulo 4: O Covil dos Ladrões...")
    txtlore(f"Você chega ao Covil dos Ladrões, um lugar de traição e intrigas. Aqui, você deve provar sua habilidade ao enfrentar um chefe de ladrões que guarda riquezas.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_bd()
    if 'Pedra Do Esmos' in player['artefatos']:
        print("Com a ajuda da Pedra Do Esmos, você derrota o chefe dos ladrões e obtém mais pontos e um artefato mágico.")
        player['pontos'] += 50
        player['artefatos'].append('Máscara Sombria')
        cenario2_furtivo()
    else:
        print("Sem a Pedra Do Esmos, você enfrenta o chefe dos ladrões com suas habilidades, vencendo após uma luta intensa.")
        player['pontos'] += 30
        cenario2_furtivo()
    

def cenario2_furtivo():
    print("Capítulo 5: As Catacumbas dos Espectros...")
    txtlore(f"Nas profundezas das catacumbas, você deve enfrentar espectros guardiões para obter um artefato sombrio.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_Banche()
    if 'Máscara Sombria' in player['artefatos']:
        print("Usando o poder da Máscara Sombria, você neutraliza os espectros e obtém o artefato sombrio.")
        player['pontos'] += 100
        player['artefatos'].append('Amuleto das Sombras')
        cenario3_furtivo()
    else:
        print("Sem a Máscara Sombria, a luta é difícil, mas suas habilidades permitem que você derrote os espectros.")
        player['pontos'] += 70
        cenario3_furtivo()

def cenario3_furtivo():
    print("Capítulo 6: O Encontro com o Mestre Assassino...")
    txtlore(f"Em uma fortaleza oculta, você encontra o Mestre Assassino, guardião de técnicas secretas. Para obter seu conhecimento, você deve provar sua furtividade e habilidade.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Amuleto das Sombras' in player['artefatos']:
        print("Usando as habilidades do Amuleto das Sombras, você impressiona o Mestre Assassino e obtém seu conhecimento.")
        player['pontos'] += 150
        player['artefatos'].append('Adaga da Sombra')
        cenario4_furtivo()
    else:
        print("Sem o Amuleto das Sombras, você enfrenta o Mestre Assassino com suas habilidades, vencendo com precisão.")
        player['pontos'] += 100
        cenario4_furtivo()

def cenario4_furtivo():
    print("Capítulo 7: A Batalha Final...")
    txtlore(f"Com todos os artefatos em mãos, você lidera um exército para defender sua vila de uma invasão inimiga. A batalha final está prestes a começar.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_goblin()
    combate_goblin()
    combate_goblin()
    combate_goblin()
    if 'Adaga da Sombra' in player['artefatos']:
        print("Usando a Adaga da Sombra, você realiza ataques furtivos para enfraquecer os inimigos e garantir a vitória.")
        player['pontos'] += 200
    else:
        print("Sem a Adaga da Sombra, a batalha é difícil, mas sua liderança e habilidades garantem a vitória para sua vila.")
        player['pontos'] += 150
    fim()


def cenario1_magico():
    print("Capítulo 4: O Vale dos Magos...")
    txtlore(f"Você chega ao Vale dos Magos, um lugar de grande poder arcano. Aqui, você deve provar seu valor ao enfrentar um mago ancião que guarda segredos arcanos.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_mf() # colocar inimigos diferentes aqui tbm
    if 'Pedra Do Esmos' in player['artefatos']:
        print("Com a ajuda da Pedra Do Esmos, você desvenda os segredos arcanos e derrota o mago ancião, obtendo mais pontos e um artefato mágico.")
        player['pontos'] += 50
        player['artefatos'].append('Amuleto Arcano')
        cenario2_magico()
    else:
        print("Sem a Pedra Do Esmos, você enfrenta o mago ancião com sua magia, vencendo após uma batalha intensa.")
        player['pontos'] += 30
        cenario2_magico()
    

def cenario2_magico():
    print("Capítulo 5: A Torre do Feiticeiro...")
    txtlore(f"Nas profundezas da torre de um feiticeiro, você deve enfrentar o poderoso feiticeiro para obter um poderoso grimório.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_mf()
    if 'Amuleto Arcano' in player['artefatos']:
        print("Usando o poder do Amuleto Arcano, você neutraliza o feiticeiro e obtém o grimório.")
        player['pontos'] += 100
        player['artefatos'].append('Grimório das Sombras')
        cenario3_magico()
    else:
        print("Sem o Amuleto Arcano, a luta é difícil, mas suas habilidades mágicas permitem que você derrote o feiticeiro.")
        player['pontos'] += 70
        cenario3_magico()

def cenario3_magico():
    print("Capítulo 6: O Encontro com o Dragão Ancião...")
    txtlore(f"Em uma caverna mística, você encontra um dragão ancião, guardião de segredos antigos. Para obter seu conhecimento, você deve provar sua sabedoria e poder.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Grimório das Sombras' in player['artefatos']:
        print("Usando os feitiços do Grimório das Sombras, você impressiona o dragão ancião e obtém seu conhecimento.")
        player['pontos'] += 150
        player['artefatos'].append('Cristal de Dragão')
        cenario4_magico()
    else:
        combate_mf() #colocar a porra do dragão
        print("Sem o Grimório das Sombras, você enfrenta o dragão ancião com seus poderes, vencendo com sabedoria.")
        player['pontos'] += 100
        cenario4_magico()

def cenario4_magico():
    print("Capítulo 7: A Batalha Final...")
    txtlore(f"Com todos os artefatos em mãos, você lidera um exército para defender sua vila de uma invasão inimiga. A batalha final está prestes a começar.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_goblin()
    combate_goblin()
    combate_goblin()
    combate_goblin()
    if 'Cristal de Dragão' in player['artefatos']:
        print("Usando o Cristal de Dragão, você conjura poderosos feitiços para fortalecer seu exército e derrotar os invasores, garantindo a vitória.")
        player['pontos'] += 200
    else:
        print("Sem o Cristal de Dragão, a batalha é difícil, mas sua liderança e habilidades mágicas garantem a vitória para sua vila.")
        player['pontos'] += 150
        
    fim()


def cenario1_CorpoAcorpo():
    clear_terminal()
    print("Capítulo 4: O Vale dos orcs...")
    if 'Pedra Do Esmos' in player['artefatos']:
        txtlore(f"Após a coleta do artefato, você segue avante na sua jornada", delay=0.05)
    else:
        txtlore(f"Você segue avante na sua jornada", delay=0.05)
    p = input('Pressione enter para avançar ')
    txtlore(f"Você chega ao Vale dos orcs, um lugar lendário conhecido por suas enormes criaturas e riquezas escondidas. No entanto, para avançar, você deve enfrentar um orc guardião que protege a entrada do vale.", delay=0.05)
    p = input('Aperte enter para avançar')
    if 'Pedra Do Esmos' in player['artefatos']:
        print('')
        print("Com a ajuda da Pedra Do Esmos, você encanta  o orc e ele diz que vai te deixar seguir, mas apenas ao ganhar dele em uma luta, mas ele promete te entragar o artefato que ele guarda e uma recopensa extra.")
        p = input('Pressione enter para avançar ')
        combate_orc()
        player['pontos'] += 50
        player['artefatos'].append('Anel dos Gigantes')
        gerar_raridades_itens(armas,equipamentos)
        equip_pet()
        
        cenario2_CorpoAcorpo()
        
    else:
        print("Sem a Pedra Do Esmos, você enfrenta o gigante com bravura, mas é uma batalha difícil.")
        player['pontos'] += 30
        combate_orc()
        cenario2_CorpoAcorpo()

def cenario2_CorpoAcorpo():
    clear_terminal()
    print("Capítulo 5: As Ruínas do Dragão...")
    print('')
    print('Descendo o vale, você encontra ruínas antigas.')
    print('')
    txtlore(f"Nas profundezas das ruínas antigas, um dragão lendário dorme, guardando um tesouro incalculável. Para obter o tesouro, você deve provar seu valor enfrentando o dragão.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_orc() #combate_dragao() criar o dragão mas até lá vai ser o orc dnv
    if 'Anel dos Gigantes' in player['artefatos']:
        print("Usando o poder do Anel dos Gigantes, você luta com o dragão e consegue subjugar a besta, obtendo seu tesouro e mais pontos.")
        player['pontos'] += 100
        player['artefatos'].append('Escama do Dragão')
        cenario3_CorpoAcorpo()
    else:
        print("Sem o Anel dos Gigantes, a luta é feroz, mas sua coragem e habilidades permitem que você derrote o dragão.")
        player['pontos'] += 70
        cenario3_CorpoAcorpo()

def cenario3_CorpoAcorpo():
    print("Capítulo 6: O Encontro com o Mago Negro...")
    txtlore(f"Em uma torre sombria, você encontra o Mago Negro, um poderoso feiticeiro que ameaça destruir sua vila. Para salvar seu povo, você deve derrotá-lo.", delay=0.05)
    p = input('Aperte enter para avançar')
    txtlore(f"O mago invoca dois protetores feitos de arvores que partem sem exitar para cima de ti.", delay=0.05)
    combate_mf()
    combate_mf()
    if 'Escama do Dragão' in player['artefatos']:
        print("Com a Escama do Dragão, você elimina os defensores do Mago Negro e o derrota, salvando sua vila.")
        player['pontos'] += 150
        player['artefatos'].append('Cetro do Mago')
        cenario4_CorpoAcorpo()
    else:
        print("Sem a Escama do Dragão, você luta bravamente contra os defensores do Mago Negro, utilizando sua força e habilidades para derrotá-los.")
        player['pontos'] += 100
        cenario4_CorpoAcorpo()

def cenario4_CorpoAcorpo():
    print("Capítulo 7: A Batalha Final...")
    txtlore(f"Com todos os artefatos em mãos, você lidera um exército para defender sua vila de uma invasão inimiga. A batalha final está prestes a começar.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_goblin()
    combate_goblin()
    combate_goblin()
    combate_goblin()
    if 'Cetro do Mago' in player['artefatos']:
        print("Usando o Cetro do Mago, você conjura poderosos feitiços para fortalecer seu exército e derrotar os invasores, garantindo a vitória.")
        player['pontos'] += 200
    else:
        print("Sem o Cetro do Mago, a batalha é difícil, mas sua liderança e habilidades garantem a vitória para sua vila.")
        player['pontos'] += 150
    
    fim()




def fim():
    sleep(2)
    clear_terminal()
    print('')
    print('Epílogo : Suas Escolhas....')
    print('')
    txtlore(f"Independentemente de suas escolhas, sua jornada moldou seu destino. Cada decisão levou você a um caminho único, cheio de desafios e recompensas. A história de Eldoria agora é contada em todo o reino, e você é sempre lembrado como o aventureiro que seguiu seu coração e enfrentou o desconhecido com coragem e honra.", delay=0.05)
    p = input('pressione enter pra avançar')
    print('')
    txtlore(f"A história que você viveu é apenas uma entre muitas possíveis, e o mundo de Eldoria está sempre pronto para mais aventuras. Que novos caminhos você escolherá na próxima vez?", delay=0.005)
    sleep(2)
    print('')
    X = int(input('DESEJA FAZER OQUE ? 1) FINALIZAR O GAME. 2) MODO INFINITO (EXPERIMENTAL) '))
    if X == 1:
        save_score()
        ranking = get_ranking()
        print('FOI MUITO BOM TER SUA COMPANHIA ATÉ ESSE MOMENTO, OBRIGADO POR TESTAR O JOGO !')
        print("Ranking:")
        for rank in ranking:
            print(f"{rank[0]} - {rank[1]}")
        sleep(5)
        parar()
    if X == 2:
        evnt_aleatorio()


def sul():
    print('você escolheu ir para o sul')
    sleep(2)
    clear_terminal()
    print('')
    print('Capítulo 3: Montanhas da Perdição....')
    print('')
    txtlore(f"As Montanhas da Perdição são perigosas e traiçoeiras. O vento frio corta sua pele e a neve dificulta a visão. No caminho, você encontra uma guerreira ferido que pede sua ajuda. Ele revela ser um guardião de um tesouro escondido nas montanhas. Em agradecimento, ele o leva até o tesouro, mas você deve resolver um enigma para obter o tesouro.", delay=0.05)
    txtlore(f" O Enigma das Montanhas", delay=0.005)
    
    if player['classe'] == '1 > Guerreiro' or player['classe'] == '2 > Barbaro' :
        x = input('Eu protejo, mas também destruo. Sou áspero, mas posso ser polido. O que sou eu? \n> ').lower()
        if x =='pedra':
            print('Você obtém o artefato e também encontra uma arma junto. Apos se equipar percebe um bandido avançando em sua direção e você não pensa duas vezes em tentar proteger o artefato.')
            player['artefatos'].append('Pedra Do Esmos')
            player['pontos'] += 30
            gerar_raridades_itens(armas,equipamentos)
            if player['classe'] == '1 > Guerreiro':
                equip_espada_curta()
            if player['classe'] == '2 > Barbaro':
                equip_machado()
            combate_bd()
            cenario1_CorpoAcorpo()
        else:
            print('Você errou a resposta e a guerreira se torna um ser espiritual e parte para o ataque. prepare-se para a batalha.')
            combate_Banche()
            chanc()
            if chanx <  40:
                print('Após a derrota do inimigo, você toma a força o artefato e segue seu caminho.')
                player['artefatos'].append('Pedra Do Esmos')
                cenario1_corpocorpo_sul()
            else:
                print('Após a derrota do inimigo, você toma a força o artefato mas ele estava quebrado. Você segue seu caminho.')
                cenario1_corpocorpo_sul()
            
    elif player['classe'] == '1 > Bruxo' or player['classe'] == '2 > Mago' :
        
        x = input('Eu sou invisível, mas posso ser visto. Eu sou intangível, mas posso ser sentido. O que sou eu? \n> ').lower()
        if x =='vento':
            print('Você obtém o artefato e também encontra uma arma junto. Apos se equipar percebe um bandido avançando em sua direção e você não pensa duas vezes em tentar proteger o artefato.')
            player['artefatos'].append('Pedra Do Esmos')
            player['pontos'] += 30
            gerar_raridades_itens(armas,equipamentos)
            if player['classe'] == '1 > Bruxo':
                equip_cajado()
            if player['classe'] == '2 > Mago':
                equip_varinha()
            combate_bd()

            cenario1_magico()
        else:
            print('Você errou a resposta e a guerreira se torna um ser espiritual e parte para o ataque. prepare-se para a batalha.')
            combate_Banche()
            chanc()
            if chanx <  40:
                print('Após a derrota do inimigo, você toma a força o artefato e segue seu caminho.')
                player['artefatos'].append('Pedra Do Esmos')
                cenario1_magia_sul()
            else:
                print('Após a derrota do inimigo, você toma a força o artefato mas ele estava quebrado. Você segue seu caminho.')
                cenario1_magia_sul()
                
    #Furtivo    
    elif player['classe'] == '1 > Bandido' or player['classe'] == '2 > Gnomo' :
        
        x = input('Eu posso atravessar o céu e a terra, mas sou tão pequeno que quase ninguém me nota. O que sou eu? \n> ').lower()
        if x =='flecha':
            print('Você obtém o artefato e também encontra uma arma junto. Apos se equipar percebe um bandido avançando em sua direção e você não pensa duas vezes em tentar proteger o artefato.')
            player['artefatos'].append('Pedra Do Esmos')
            player['pontos'] += 30
            gerar_raridades_itens(armas,equipamentos)
            if player['classe'] == '1 > Bandido':
                equip_adaga()
            if player['classe'] == '2 > Gnomo':
                equip_adaga()
            combate_bd()
            cenario1_furtivo()
        else:
            print('Você errou a resposta e a guerreira se torna um ser espiritual e parte para o ataque. prepare-se para a batalha.')
            combate_Banche()
            chanc()
            if chanx <  40:
                print('Após a derrota do inimigo, você toma a força o artefato e segue seu caminho.')
                player['artefatos'].append('Pedra Do Esmos')
                cenario1_furtivo_sul()
            else:
                print('Após a derrota do inimigo, você toma a força o artefato mas ele estava quebrado. Você segue seu caminho.')
                cenario1_furtivo_sul()

    

def norte():
    print('você escolheu ir para o norte')
    sleep(2)
    clear_terminal()
    print('')
    print('Capítulo 3: A Floresta Sussurrante....')
    print('')
    txtlore(f"A Floresta Sussurrante é misteriosa e cheia de vida. As árvores antigas parecem sussurrar segredos e histórias de tempos passados. Você encontra um pergaminho antigo que revela a localização de um artefato mágico escondido nas profundezas da floresta. Para obter o artefato, você deve resolver um enigma apresentado por uma criatura mágica.", delay=0.05)
    p = input('Aperte enter para avançar')
    txtlore(f"O Enigma da Floresta", delay=0.005)
    #Corpo a Corpo
    if player['classe'] == '1 > Guerreiro' or player['classe'] == '2 > Barbaro' :
        x = input('Eu sou forte como uma rocha, mas cresço com a água. O que sou eu? \n> ').lower()
        if x =='carvalho':
            print('Você obtém o artefato e também encontra uma armadura junto. Apos se equipar percebe um bandido avançando em sua direção e você não pensa duas vezes em tentar proteger o artefato.')
            player['artefatos'].append('Colar Divino')
            player['pontos'] += 30
            gerar_raridades_itens(armas,equipamentos)
            equip_cap()
            combate_bd()
            cenario1_CorpoAcorpo()
        else:
            print('Você errou a resposta e a criatura da floresta avança em você. prepare-se para a batalha.')
            combate_mf()
            chanc()
            if chanx <  40:
                print('Após a derrota do inimigo, você toma a força o artefato e segue seu caminho.')
                player['artefatos'].append('Colar Divino')
            else:
                print('Após a derrota do inimigo, você toma a força o artefato mas ele estava quebrado. Você segue seu caminho.')
                cenario1_CorpoAcorpo()
    #Magias  
    elif player['classe'] == '1 > Bruxo' or player['classe'] == '2 > Mago' :
        
        x = input('Eu posso ser quebrado sem ser tocado. O que sou eu? \n> ').lower()
        if x =='segredo':
            print('Você obtém o artefato e também encontra uma armadura junto. Apos se equipar percebe um bandido avançando em sua direção e você não pensa duas vezes em tentar proteger o artefato.')
            player['artefatos'].append('Colar Divino')
            player['pontos'] += 30
            gerar_raridades_itens(armas,equipamentos)
            equip_cap()
            combate_bd()
            cenario1_magico()
        else:
            print('Você errou a resposta e a criatura da floresta avança em você. prepare-se para a batalha.')
            combate_mf()
            chanc()
            if chanx <  40:
                print('Após a derrota do inimigo, você toma a força o artefato e segue seu caminho.')
                player['artefatos'].append('Colar Divino')
                cenario1_magico()
            else:
                print('Após a derrota do inimigo, você toma a força o artefato mas ele está quebrado. Você segue seu caminho.')
                cenario1_magico()
        
    elif player['classe'] == '1 > Bandido' or player['classe'] == '2 > Gnomo' :
        
        x = input('Eu sou leve como uma pena, mas nem o homem mais forte pode me segurar por muito tempo. O que sou eu? \n> ').lower()
        if x =='fôlego':
            print('Você obtém o artefato e também encontra uma armadura junto. Apos se equipar percebe um bandido avançando em sua direção e você não pensa duas vezes em tentar proteger o artefato.')
            player['artefatos'].append('Colar Divino')
            player['pontos'] += 30
            gerar_raridades_itens(armas,equipamentos)
            equip_cap()
            combate_bd()
            cenario1_furtivo()
        else:
            print('Você errou a resposta e a criatura da floresta avança em você. prepare-se para a batalha.')
            combate_mf()
            chanc()
            if chanx <  40:
                print('Após a derrota do inimigo, você toma a força o artefato e segue seu caminho.')
                player['artefatos'].append('Colar Divino')
                cenario1_furtivo()
            else:
                print('Após a derrota do inimigo, você toma a força o artefato mas ele está quebrado. Você segue seu caminho.')
                cenario1_furtivo()
def cap2():
    sleep(3)
    p = input('Aperte enter para avançar')
    clear_terminal()
    print('')
    print('Capítulo 2: A Primeira Jornada....')
    print('')
    if player['classe'] == '1 > Guerreiro' or player['classe'] == '2 > Barbaro' :
        txtlore(f"Você sente a familiaridade do peso da arma em sua mão. A força e a coragem são suas aliadas. O ancião olha para você com orgulho e diz : -{player['nome']}, você é a força de nossa vila. Escolha seu caminho: vá para o norte, onde a Floresta Sussurrante esconde segredos antigos, ou para o sul, onde as Montanhas da Perdição são habitadas por monstros ferozes.", delay=0.05)
        
    elif player['classe'] == '1 > Bruxo' or player['classe'] == '2 > Mago' :
        txtlore(f"O cajado em sua mão pulsa com energia arcana. O conhecimento e a magia são suas aliadas. O ancião sorri sabiamente e diz : -{player['nome']}, você é a sabedoria de nossa vila. Escolha seu caminho: vá para o norte, onde a Floresta Sussurrante esconde segredos antigos, ou para o sul, onde as Montanhas da Perdição são habitadas por monstros ferozes.", delay=0.05)
        
    elif player['classe'] == '1 > Bandido' or player['classe'] == '2 > Gnomo' :
        txtlore(f"a arma em suas mãos é leve e mortal. A precisão e a agilidade são suas aliadas. O ancião acena com respeito e diz : - {player['nome']}, você é a precisão de nossa vila. Escolha seu caminho: vá para o norte, onde a Floresta Sussurrante esconde segredos antigos, ou para o sul, onde as Montanhas da Perdição são habitadas por monstros ferozes.", delay=0.05)
        
    txtlore(f"O destino de Eldoria depende da sua coragem e sabedoria. ", delay=0.005)
    x = int(input('Qual caminho seguir ? \n1)norte \n2)sul \n> '))
    if x == 1:
        sleep(1)
        clear_terminal()
        norte()
    elif x == 2:
        sleep(1)
        sul()


def cap1():
    print('>>> Você pode pressionar Shift caso queira pular o texto. <<<')
    print('')
    print('Capítulo 1: O Chamado da Aventura....')
    print('')
    txtlore(f"Você acorda em sua pequena cabana na vila de Eldoria. O sol está nascendo e o cheiro de pão fresco invade seus sentidos. Hoje é um dia especial; você completa 18 anos e finalmente pode se aventurar além dos limites da vila.", delay=0.005)
    sleep(1)
    txtlore(f"Você se levanta, veste sua armadura de couro e pega sua espada herdada de seu pai, um antigo guerreiro. No centro da vila, o ancião espera por você.", delay=0.005)
    sleep(1)
    txtlore(f"O ancião diz: -Parabéns, jovem aventureiro! Hoje você começa sua jornada. Primeiro, deve escolher sua classe e arma.", delay=0.005)
    p = input('Aperte enter para avançar')
    escolha_classe()





        
def PLAY():
    
    while True:
        print('Bem vindo ao SACRAMENTO. escolha uma das opções abaixo para prosseguirmos.')
        print('-------------------------------------------------------------------')
        print("1. Iniciar Jogo")
        print("2. Ver Ranking")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            p()
        elif choice == '2':
            print_ranking()
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

    
    
    
def p():
    txt_str()
    cap1()
    cap2()
    
    
PLAY()
