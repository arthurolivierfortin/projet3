"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quoridor import Quoridor
from utilitaire import analyser_commande, formater_les_parties
from quoridor_serveur import formater_jeu, récupérer_le_coup, formater_les_parties
import quoridor_serveur_vs_bot as Q_SvB
import time
import quoridorx
# Mettre ici votre secret récupéré depuis le site de PAX
secret = "07088f23-df64-4ff3-a352-08cb9a19158d"

if __name__ == "__main__":
    args = analyser_commande()
        

    if args.automatique:
        # Implémenter la boucle pour jouer contre le bot du serveur
        id_partie, état = débuter_partie(args.idul, secret)
        while True:
            # Afficher la partie
            print(Q_SvB.formater_jeu(état))
            # Demander au joueur de choisir son prochain coup
            position, type_coup = Q_SvB.jouer_le_coup(état)
            
            # Envoyez le coup au serveur
            id_partie, état = jouer_coup(
                id_partie,
                type_coup,
                position,
                args.idul,
                secret,
            )
            time.sleep(1)


    if args.parties:
        parties = lister_parties(args.idul, secret)
        print(formater_les_parties(parties))

    
    if args.local:
        # Implémenter la boucle pour jouer contre votre bot en local
        joueurs = [{"nom": args.idul, "murs": 10, "pos": [5, 1]}, {"nom": 'automate', "murs": 10, "pos": [5, 9]}]
        murs = {"horizontaux": [],
        "verticaux": [],}
        def jouer(joueurs, murs):
            état = Quoridor.vérification(Quoridor, joueurs, murs)
            affichage = Quoridor.__str__(état)
            print(affichage)
            type_coup, position = Quoridor.récupérer_le_coup(Quoridor, 1)
            if type_coup == 'D':
                Quoridor.déplacer_jeton(Quoridor, 1, position)
            if type_coup == 'MH' or type_coup == 'MV':
                joueurs, murs = Quoridor.placer_un_mur(Quoridor, 1, position, type_coup)
            Quoridor.est_terminée(Quoridor)
            #joueurs, murs = Quoridor.jouer_le_coup(Quoridor, 2)
    
    if args.graphique:
        joueurs = [{"nom": args.idul, "murs": 10, "pos": [5, 1]}, {"nom": 'automate', "murs": 10, "pos": [5, 9]}]
        murs = {"horizontaux": [],
        "verticaux": [],}
        def jouer(joueurs, murs):
            état = Quoridor.vérification(Quoridor, joueurs, murs)
            #quoridorx.QuoridorX.graphique()
            #quoridorx.QuoridorX.positionnement_joueur(état)
            quoridorx.QuoridorX.légende_murs_départ(état)
            type_coup, position = Quoridor.récupérer_le_coup(Quoridor, 1)
            if type_coup == 'D':
                Quoridor.déplacer_jeton(Quoridor, 1, position)
            if type_coup == 'MH' or type_coup == 'MV':
                joueurs, murs = Quoridor.placer_un_mur(Quoridor, 1, position, type_coup)
            Quoridor.est_terminée(Quoridor)
            #joueurs, murs = Quoridor.jouer_le_coup(Quoridor, 2)

            jouer(joueurs, murs)
        jouer(joueurs, murs)
    else:
        # Implémenter la boucle pour jouer contre le bot du serveur
        id_partie, état = débuter_partie(args.idul, secret)
        while True:
            # Afficher la partie
            print(formater_jeu(état))
            # Demander au joueur de choisir son prochain coup
            type_coup, position = récupérer_le_coup()
            # Envoyez le coup au serveur
            id_partie, état = jouer_coup(
                id_partie,
                type_coup,
                position,
                args.idul,
                secret,
            )
