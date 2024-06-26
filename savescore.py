import firebase_admin
from firebase_admin import credentials, firestore
from Player import player
import platform
import os


def clear_terminal():
    system_name = platform.system()
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Inicialização do Firebase
cred = credentials.Certificate('firebase_config.json')  # Substitua pelo caminho do seu arquivo JSON
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_ranking():
    rankings_ref = db.collection('rankings')
    rankings = rankings_ref.order_by('score', direction=firestore.Query.DESCENDING).stream()
    ranking_list = [(ranking.to_dict()['player_name'], ranking.to_dict()['score']) for ranking in rankings]
    return ranking_list

def save_score():
    x = input('Digite a forma que você gostaria de aparecer no Rank \n> ')
    rankings_ref = db.collection('rankings')
    rankings_ref.add({
        'player_name': x,
        'score': player['pontos']
    })

def print_ranking():
    ranking_list = get_ranking()
    medals = ['🥇', '🥈', '🥉']
    clear_terminal()
    print("Aqui estão nossos queridos jogadores \n\n")
    for index, (player_name, score) in enumerate(ranking_list, start=1):
        if index <= 3:
            print(f"{medals[index-1]} {index}. {player_name} - {score} pontos")
        else:
            print(f"{index}. {player_name} - {score} pontos")
    print('----------------------------------------------------------------')


