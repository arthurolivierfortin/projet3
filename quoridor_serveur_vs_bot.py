"""Module Quoridor"""
from copy import deepcopy

from quoridor_error import QuoridorError

from graphe import construire_graphe

import networkx as nx

import copy
"""Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique du damier.
    * formater_damier - Formater la représentation graphique de la légende.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
import argparse





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


def récupérer_le_coup(état):
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
    Examples:
        Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):
        Donnez la position où appliquer ce coup (x,y): 2,6
    """
    print(état)


def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.

        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """

        if joueur != 1 and joueur != 2:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")

        if self.état["joueurs"][0]["pos"][1] == 9:
            raise QuoridorError(" QuoridorError: La partie est déjà terminée.")

        if self.état["joueurs"][1]["pos"][1] == 1:
            raise QuoridorError(" QuoridorError: La partie est déjà terminée.")


        graphe = construire_graphe(
            [tuple(joueur['pos']) for joueur in self.état['joueurs']],
            tuple(self.état['murs']['horizontaux']),
            tuple(self.état['murs']['verticaux']))

        liste_chemin_rapide_J1 = nx.shortest_path(graphe, tuple(self.état["joueurs"][0]["pos"]), 'B1')

        for i in liste_chemin_rapide_J1:
            if type(i) != tuple:
                liste_chemin_rapide_J1.remove(i)

        Choix_de_chemin_J1 = list(graphe.successors(tuple(self.état["joueurs"][0]["pos"])))
        for i in Choix_de_chemin_J1:
            if type(i) != tuple:
                Choix_de_chemin_J1.remove(i)

        for i in liste_chemin_rapide_J1:
            for j in Choix_de_chemin_J1:
                if j == i:
                    x = j



        if len(Choix_de_chemin_J1) > 1:
            if self.état["joueurs"][0]["pos"][0] != x[0]:
 
                delta = self.état["joueurs"][0]["pos"][0] - x[0]
                if delta < 0:
                    variable_k = self.état["joueurs"][0]["pos"][0]
                    variable_y = self.état["joueurs"][0]["pos"][1]
                    variable_ky = [(variable_k+1), variable_y]
                if delta > 0:
                    variable_k = self.état["joueurs"][0]["pos"][0]
                    variable_y = self.état["joueurs"][0]["pos"][1]
                    variable_ky = [variable_k, variable_y]
                try:
                    Quoridor.placer_un_mur(Quoridor, 2, variable_ky, "MV")
                except QuoridorError:
                     variable_k = "ne peut pas mettre un mur"





            if self.état["joueurs"][0]["pos"][1] != x[1]:
                variable_k = self.état["joueurs"][0]["pos"][0]
                variable_y = self.état["joueurs"][0]["pos"][1]
                variable_ky = [(variable_k-1), (variable_y+1)]
                for i in self.état["murs"]["horizontaux"]:

                    if i[1] == (variable_y + 1) and (i[0] + 2) == variable_k:

                        variable_ky = [variable_k, (variable_y+1)]

                #pos = (list(self.état["joueurs"][0]["pos"]))
                #self.état['murs']['verticaux'] += ([pos])


                try:
                    Quoridor.placer_un_mur(Quoridor, 2, variable_ky, "MH")
                except QuoridorError:
                    variable_k = "ne peut pas mettre un mur"

            if variable_k == "ne peut pas mettre un mur":
                mouvement_rapide_J2 = nx.shortest_path(graphe, tuple(self.état["joueurs"][1]["pos"]), 'B2')
                self.état["joueurs"][1]["pos"] = list(mouvement_rapide_J2[1])
                joueurs = self.état["joueurs"]
                murs = self.état["murs"]
                return (joueurs, murs)


def placer_un_mur(self, joueur, position, orientation):

        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        état = copy.deepcopy(self.état)

        if joueur != 1 and joueur != 2:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")


        for i in self.état["murs"]["horizontaux"]:
            if position[0] == i[0]+1 and position[1]+1 == i[1]:
                raise QuoridorError("Un mur occupe déjà cette position.")

        for i in self.état["murs"]["verticaux"]:
            if position[0] == i[0]-1 and position[1]-1 == i[1]:
                raise QuoridorError("Un mur occupe déjà cette position.")



        if orientation == "MH":
            for i in self.état["murs"]["horizontaux"]:
                if i[0]-1 == position[0] and i[1] == position[1]:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MV":
            for i in self.état["murs"]["verticaux"]:
                if i[0] == position[0] and (i[1]-1) == position[1]:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MV":
            for i in self.état["murs"]["verticaux"]:
                if i == position:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MH":
            for i in self.état["murs"]["horizontaux"]:
                if i == position:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MH":
            if (1 <= position[0] <= 8) == False:
                raise QuoridorError("La position d'un mur est invalide.")

            elif (2 <= position[1] <= 9) == False:
                raise QuoridorError("La position d'un mur est invalide.")

        if orientation == "MV":
            if (2 <= position[0] <= 9) == False:
                raise QuoridorError("La position d'un mur est invalide.")

            elif (1 <= position[1] <= 8) == False:
                raise QuoridorError("La position d'un mur est invalide.")


        if self.état["joueurs"][joueur-1]["murs"] <= 0:
            raise QuoridorError("Le joueur a déjà placé tous ses murs.")


        if orientation == "MV":
            état["murs"]["verticaux"] += [position]
            état["joueurs"][joueur-1]["murs"] -=  1

        if orientation == "MH":
            état["murs"]["horizontaux"] += [position]
            état["joueurs"][joueur-1]["murs"] -=  1


        graphe = construire_graphe(
            [tuple(joueur['pos']) for joueur in état['joueurs']],
            tuple(état['murs']['horizontaux']),
            tuple(état['murs']['verticaux']))




        if nx.has_path(graphe, tuple(état["joueurs"][0]["pos"]), 'B1') == False:

            raise QuoridorError("La position du mur est invalide puisqu'elle enferme le joueur")

        if nx.has_path(graphe, tuple(état["joueurs"][1]["pos"]), 'B2') == False:

            raise QuoridorError("La position du mur est invalide puisqu'elle enferme le joueur")

        if orientation == "MV":
            self.état["murs"]["verticaux"] += [position]
            self.état["joueurs"][joueur-1]["murs"] -=  1

        if orientation == "MH":
            self.état["murs"]["horizontaux"] += [position]
            self.état["joueurs"][joueur-1]["murs"] -=  1



        if joueur == 1:
            Quoridor.jouer_le_coup(Quoridor, 2)

        joueurs = self.état["joueurs"]
        murs = self.état["murs"]
        return (joueurs, murs)

    

