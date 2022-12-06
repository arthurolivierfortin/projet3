"""Module Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique du damier.
    * formater_damier - Formater la représentation graphique de la légende.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
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
        action='store_true' )
    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_légende(joueurs):
    """Formater la représentation graphique de la légende.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.

    Returns:
        str: Chaîne de caractères représentant la légende.
    """

    x = joueurs
    nb_murs_joueur1 = x[0]['murs']
    nb_murs_automate = x[1]['murs']
    nom_idul = x[0]['nom']
    nom_automate = x[1]['nom']
    différence_espace = len(nom_idul) - len(nom_automate)
    espace_ajoutee_automate = 0
    espace_ajoutee_idul = 0
    if différence_espace > 0:
        espace_ajoutee_automate = 0
        espace_ajoutee_automate = ((' '*(différence_espace)))
        murs_idul = (nb_murs_joueur1*'|')
        murs_automate = (nb_murs_automate*'|')
        legende = ("Légende:\n"   f"   1={nom_idul}, murs={murs_idul}\n"   f"   2={nom_automate}, {espace_ajoutee_automate}murs={murs_automate}\n")
        return legende
    if différence_espace < 0:
        espace_ajoutee_idul = 0
        espace_ajoutee_idul = ((' '*(-1*(différence_espace))))
        murs_idul = (nb_murs_joueur1*'|')
        murs_automate = (nb_murs_automate*'|')
        legende = ("Légende:\n"   f"   1={nom_idul}, {espace_ajoutee_idul}murs={murs_idul}\n"   f"   2={nom_automate}, murs={murs_automate}\n")
        return legende
    murs_idul = nb_murs_joueur1*'|'
    murs_automate = nb_murs_automate*'|'
    legende = ("Légende:\n"   f"   1={nom_idul}, murs={murs_idul}\n"   f"   2={nom_automate}, murs={murs_automate}\n")
    return legende


def formater_damier(joueurs, murs):
    """Formater la représentation graphique du damier.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.
        murs (dict): Dictionnaire représentant l'emplacement des murs.

    Returns:
        str: Chaîne de caractères représentant le damier.
    """

    damier_vide = (
        "   -----------------------------------\n"
        "9 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "7 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "6 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "5 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "4 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "3 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "2 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   .   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )

    damier = damier_vide
    murs_verticaux = murs["verticaux"]
    murs_horizontaux = murs["horizontaux"]
    positionnement_idul = joueurs[0]['pos']
    positionnement_automate = joueurs[1]['pos']
    for i in murs_verticaux:
        x = damier.find(str(i[1]))
        damier = list(damier)
        y = (4+(4*((i[0])-1))-2)
        damier[x+y] = ('|')
        damier[x+y-40] = ('|')
        damier[x+y-80] = ('|')
        z = ''.join(damier)
        damier = (z)
    for i in murs_horizontaux:
        x = damier.find(str(i[1]))
        damier = list(damier)
        y = (+40+4+(4*((i[0])))-5)
        damier[y+x] = ('-')
        damier[y+x+1] = ('-')
        damier[y+x+2] = ('-')
        damier[y+x+3] = ('-')
        damier[y+x+4] = ('-')
        damier[y+x+5] = ('-')
        damier[y+x+6] = ('-')
        z = ''.join(damier)
        damier = (z)
    x = damier.find(str(positionnement_idul[1]))
    damier = list(damier)
    y = (4+(4*((positionnement_idul[0])-1)))
    damier[y+x] = ('1')
    z = ''.join(damier)
    damier = (z)
    x = damier.find(str(positionnement_automate[1]))
    damier = list(damier)
    y = (4+(4*((positionnement_automate[0])-1)))
    damier[y+x] = ('2')
    z = ''.join(damier)
    damier = (z)
    return damier


def formater_jeu(état):
    from quoridor_serveur import formater_légende
    from quoridor_serveur import formater_damier


    """Formater la représentation graphique d'un jeu.

    Doit faire usage des fonctions formater_légende et formater_damier.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """

    return formater_légende(état['joueurs']) + formater_damier(état['joueurs'], état['murs'])


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


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
    Examples:
        Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):
        Donnez la position où appliquer ce coup (x,y): 2,6
    """

    type_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):")
    x = input("Donnez la position où appliquer ce coup (x,y):")
    p = int(x[0])
    w = int(x[2])
    position = [p, w]
    return(type_coup, position)
