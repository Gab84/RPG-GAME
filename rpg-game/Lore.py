from Acoes import *
from Player import player
from time import sleep
from Textos import txtlore
from savescore import *

def part1():
    txtlore(f"Em uma caverna, {player['nome']}, acorda devido a forte agitação, do som de metal, e risadas direcionadadas a {player['nome']}, ao abrir os olhos, uma voz rouca te chama.", delay=0.005)
    sleep(1)
    txtlore(f"VOZ > Ei, princesa! Acorda, você não está em um spa. Depois que esses malditos entram na merda do Ether virão mesmo uns preguiçosos. por falar nisso, sou Heclito, o Hemosiano.", delay=0.005)
    sleep(1)
    txtlore(f"Vamos, pegue alguns equipamentos. Precisamos de mais gente, mesmo que você não pareça fazer diferença nesse lugar.", delay=0.005)
    escolha_classe()
    
#escolha parte 2

def A_B01_1():
    txtlore(f"{player['nome']} prossegue seu caminho e mais a frente encontra novamente heclito, ele diz que estão indo para fora das defesas da cidade e que precisa que você venha junto.", delay=0.05)
    sleep(1)
    txtlore(f"{player['nome']} segue Heclito até os portões da cidade e lá eles percebem uma dupla de orcs, Heclito diz para você cuidar de um que ele promete finalizar o outro.", delay=0.05)
    sleep(4)
    combate_orc()

def A_B01():
    sleep(1)
    txtlore(f"Ao tentar prosseguir ver uma escritura na parede que aparentemente foi escrito por uma comunidade distante.", delay=0.005)
    x = int(input('Deseaja tentar ler ? \n1)SIM \n2)NAO \n > '))
    if x == 1:
        if player['classe'] == '2 > Mago':
            if player['mana'] == (player['mana_inicial'] +20):
                print('Você já leu.')
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
    clear_terminal()
    txtlore(f"Após a coleta de seus itens, {player['nome']} vê dois caminhos a serem seguidos.", delay=0.05)
    txtlore(f"Uma porta a direita que alguns dos soldados estão indo. Uma porta a esquerda que você percebe um velho bebado indo.", delay=0.005)
    x = int(input('Qual caminho seguir ? \n1)direita \n2)esquerda \n> '))
    if x == 1:
        sleep(1)
        clear_terminal()
        A_B01()
    

def part3():
    print('deu bom')
    


def PLAY():
    print (player)
    while True:
        print("1. Iniciar Jogo")
        print("2. Ver Ranking")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            p()
        elif choice == '2':
            ranking = get_ranking()
            print("Ranking:")
            for rank in ranking:
                print(f"{rank[0]} - {rank[1]}")
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

    
    
    
def p():
    txt_str()
    part1()
    part2()
    part3()
    

PLAY()