
import firebase_admin
from firebase_admin import credentials, firestore
from Player import player

cred = credentials.Certificate('firebase_config.json')  # Substitua pelo caminho do seu arquivo JSON
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_ranking():
    rankings_ref = db.collection('rankings')
    rankings = rankings_ref.order_by('score', direction=firestore.Query.DESCENDING).stream()
    ranking_list = [(ranking.to_dict()['player_name'], ranking.to_dict()['score']) for ranking in rankings]
    return ranking_list


def save_score():
    rankings_ref = db.collection('rankings')
    rankings_ref.add({
        'player_name': player['nome'],
        'score': player['pontos']
    })

