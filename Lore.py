from Acoes import *
from Player import player
from time import sleep
from Textos import txtlore
from savescore import *
from Modo_infinito import evnt_aleatorio



def part1():
    txtlore(f"Em uma caverna, {player['nome']}, acorda devido a forte agitação, do som de metal, e risadas direcionadadas a {player['nome']}, ao abrir os olhos, uma voz rouca te chama.", delay=0.005)
    sleep(1)
    txtlore(f"VOZ > Ei, princesa! Acorda, você não está em um spa. Depois que esses malditos entram na merda do Ether virão mesmo uns preguiçosos. por falar nisso, sou Heclito, o Hemosiano.", delay=0.005)
    sleep(1)
    txtlore(f"Vamos, pegue alguns equipamentos. Precisamos de mais gente, mesmo que você não pareça fazer diferença nesse lugar.", delay=0.005)
    p = input('Aperte enter para avançar')
    escolha_classe()
    
#escolha parte 2

def A_B01_1():
    txtlore(f"{player['nome']} prossegue seu caminho e mais a frente encontra novamente heclito, ele diz que estão indo para fora das defesas da cidade e que precisa que você venha junto.", delay=0.05)
    sleep(1)
    txtlore(f"{player['nome']} segue Heclito até os portões da cidade e lá eles percebem uma dupla de orcs, Heclito diz para você cuidar de um que ele promete finalizar o outro.", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_orc()

def A_B01():
    sleep(1)
    txtlore(f"Ao tentar prosseguir ver uma escritura na parede que aparentemente foi escrito por uma comunidade distante.", delay=0.005)
    x = int(input('Deseaja tentar ler ? \n1)SIM \n2)NAO \n > '))
    if x == 1:
        if player['classe'] == '2 > Mago':
            if player['mana'] == (player['mana_inicial'] +20):
                print('Você já leu e não precisa ler novamente, escolha outro caminho.')
                sleep(3)
                clear_terminal()
                sleep(1)
                A_B01()
            else:
                sleep(1)
                print('Você conseguiu ler e adquiriu informações importantes')
                sleep(3)
                clear_terminal()
                player['mana'] += 20
                player['pontos'] += 20
                sleep(1)
                A_B01()
                
        else:
            print('Você se esforça, mas não consegue entender a ligua que aquilo está escrito. ')
            sleep(3)
            clear_terminal()
            A_B01()
    elif x == 2:
        print('você segue adiante e encontar uma uma cidade absurdamente surreal e um rapaz ao canto te chama para o lado dele.')
        sleep(2)
        b = int(input('Deseaja se aproximar ? ? \n1)SIM \n2)NAO \n > '))
        clear_terminal()
        if b == 1 :
            print(f"Ele se apresenta, seu nome é Alexandre, ele rapidamente diz: eu tenho oque você vai precisar. se aproxime.")
            p = input('Aperte enter para avançar')
            sleep(2)
            loja(npc=loja_Alexandre)
            sleep(2)
            print('Após visitar a loja.')
            A_B01_1()
        elif b == 2:
            sleep(1)
            A_B01_1()

def part2():
    sleep(3)
    p = input('Aperte enter para avançar')
    clear_terminal()
    txtlore(f"Após a coleta de seus itens, {player['nome']} vê dois caminhos a serem seguidos.", delay=0.05)
    txtlore(f"Uma porta a direita que alguns dos soldados estão indo. Uma porta a esquerda que você percebe um velho bebado indo.", delay=0.005)
    x = int(input('Qual caminho seguir ? \n1)direita \n2)esquerda \n> '))
    if x == 1:
        sleep(1)
        clear_terminal()
        A_B01()
    else:
        print('Desculpe, esse caminho ainda não está concluido. escolha o outro :)')
        part2()
    

def part3():
    txtlore(f"Depois de sua vitoria, Heclito chama diz : 'Você me parece realmente alguem digno de minha confiança, mas ainda precisa aprender muito sobre combate, vamos. irei te levar até nossa area de treino.'.", delay=0.05)
    txtlore(f"Após chegarem, heclito apresenta os fundamentos da guerra para {player['nome']}.", delay=0.05)
    txtlore(f"Depois de um longo dia de treino, você se sente mais experiente e confiante para os novos desafios. ", delay=0.05)
    p = input('Aperte enter para avançar')
    distribuir_pt()
    txtlore(f"Heclito diz que espera que seja a ultima vez que te encontre aqui, soldados confiados por ele não precisam treinar, eles são bons por natureza e suas habilidades irão melhorar com experiencias em lutas ", delay=0.05)
    txtlore(f"Algo passa por você, algo semelhante a um fantasma de uma mulher. mas logo seu foco é interrompido por heclito dizendo que há 2 bandidos correndo pela cidade. ", delay=0.05)
    txtlore(f"Você sem exitar corre atrás deles até um beco. chegando lá percebe que era apenas você que eles queriam, mas não era relacioado aos seus pertencer então os dois te cercam e partem pra cima de você ", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_bd()
    combate_bd()


def part4():
    clear_terminal()
    txtlore(f"Os bandidos são derrotados e você leva ambos até a prisão.", delay=0.05)
    txtlore(f"Heclito leva você pra fora da cidade e tals ", delay=0.05)
    txtlore(f"Explorando os campus você encontra um vendendor diferente, e acha suspeito estar tão longe da cidade. mas mesmo assim se aproxima ", delay=0.05)
    p = input('Aperte enter para avançar')
    loja_a(npc=loja_Bathemofh)
  
def part5():
    clear_terminal()
    txtlore(f"após isso percebe 3 Globins se aproximando ", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_goblin()
    combate_goblin()
    combate_goblin()

def part6():
    txtlore(f"Após issp você vai pra uma floresta e encontra um monstro estranho ", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_mf()

def part7():
    clear_terminal()
    txtlore(f"No meio da floresta você encontra outro vendendor. ", delay=0.05)
    p = input('Aperte enter para avançar')
    loja_e(npc=loja_Bartolomeu)
    txtlore(f"Você vê novamente o fantasma e decide seguir ele dessa vez. ", delay=0.05)
    p = input('Aperte enter para avançar')
    combate_Banche()


def part8():
    txtlore(f"PARABÉNS, VOCÊ CHEGOU ATÉ O FINAL DO GAME, VOCÊ PODE AUMENTAR SUA PONTUAÇÃO LUTANDO CONTRA OUTROS INIMIGOS SEGUINDO O MODO INFINITO DO GAME OU PODE SAIR AGORA E SALVAR SUA PONTUAÇÃO NO NOSSO RANKING PRA MOSTRAR PRA TODOS O SEU PODER . ", delay=0.05)
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
        
def PLAY():
    
    while True:
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
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    part7()
    part8()
    
    
PLAY()
