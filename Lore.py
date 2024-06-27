from Acoes import *
from Player import player
from time import sleep
from Textos import txtlore
from savescore import *
from Modo_infinito import evnt_aleatorio
from rich import *


def part1():
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
    print('')
    print('Capítulo 2: A Primeira Jornada....')
    print('')
    txtlore(f"Independente da classe escolhida, o ancião dá a {player['nome']} uma missão para começar sua jornada.", delay=0.05)
    txtlore(f"O destino de Eldoria depende da sua coragem e sabedoria. Vá ao norte, onde a Floresta Sussurrante esconde segredos antigos, ou ao sul, onde as Montanhas da Perdição são habitadas por monstros ferozes. Em qualquer direção, você encontrará desafios que testarão suas habilidades.", delay=0.005)
    x = int(input('Qual caminho seguir ? \n1)norte \n2)sul \n> '))
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
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    part7()
    part8()
    
    
PLAY()
