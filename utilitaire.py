"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""

import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut «idul» représentant l'idul du joueur
                   et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'idul',
        type=str,
        default=None,
        help='IDUL du joueur')
    parser.add_argument(
        '-p',
        '--parties',
        help='Lister les parties existantes',
        action='store_true')
    parser.add_argument(
        '-l',
        '--local',
        help='jouer en local',
        action='store_true' )
    parser.add_argument(
        '-a',
        '--automatique',
        help='Activer le mode automatique.',
        action='store_true' )
    parser.add_argument(
        '-x',
        '--graphique',
        help='Activer le mode graphique.',
        action='store_true' )
    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    liste = ''
    for i in range(len(parties)):
        if (parties[i]['gagnant']) is None:
            liste += (f"{i} : {parties[i]['date']}, {parties[i]['joueurs']}\n")
        else:
            liste += (f"{i} : {parties[i]['date']}, {parties[i]['joueurs']}, gagnant {parties[i]['gagnant']}\n")
    return liste
