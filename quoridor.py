"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy

import copy

import networkx as nx

from quoridor_error import QuoridorError

from graphe import construire_graphe


class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """

    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))

    def vérification(self, joueurs, murs):
        """Vérification d'initialisation d'une instance de la classe Quoridor.

        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        try:
            joueurs[0]
        except TypeError:
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")

        if len(joueurs) > 2:
            raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")

        if isinstance(joueurs, dict):

            if joueurs[0]["murs"] < 0 or joueurs[0]["murs"] > 10:
                raise QuoridorError("""Le nombre de murs qu'un joueur peut placer est
                plus grand que 10, ou négatif.""")

            if joueurs[1]["murs"] < 0 or joueurs[1]["murs"] > 10:
                raise QuoridorError("""Le nombre de murs qu'un joueur peut placer est
                plus grand que 10, ou négatif.""")

            if joueurs[0]["pos"] != [5, 1] and joueurs[0]["pos"] != [5, 9] and murs is None:
                raise QuoridorError("La position d'un joueur est invalide.")

            if joueurs[1]["pos"] != [5, 1] and joueurs[1]["pos"] != [5, 9] and murs is None:
                raise QuoridorError("La position d'un joueur est invalide.")

        if murs is None:
            murs = {"horizontaux": [], "verticaux": [], }

        if murs is not None:
            if not isinstance(murs, dict):
                raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")

            if isinstance(joueurs[0], dict):
                if len(murs["horizontaux"]) + len(murs["verticaux"]) + \
                        (joueurs[0]['murs']) + (joueurs[1]['murs']) != 20:
                    raise QuoridorError("QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.")

            for i in murs["horizontaux"]:
                if (1 <= i[0] <= 8) is False:
                    raise QuoridorError("La position d'un mur est invalide.")

                if (2 <= i[1] <= 9) is False:
                    raise QuoridorError("La position d'un mur est invalide.")

            for i in murs["verticaux"]:
                if (2 <= i[0] <= 9) is False:
                    raise QuoridorError("La position d'un mur est invalide.")

                if (1 <= i[1] <= 8) is False:
                    raise QuoridorError("La position d'un mur est invalide.")

        état = {"joueurs": joueurs, "murs": murs}
        self.état = état
        return self.état

    def formater_légende(self):
        """Formater la représentation graphique de la légende.

        Returns:
            str: Chaîne de caractères représentant la légende.
        """
        variable_x = self["joueurs"]
        nb_murs_joueur1 = variable_x[0]['murs']
        nb_murs_joueur2 = variable_x[1]['murs']
        nom_joueur1 = variable_x[0]['nom']
        nom_joueur2 = variable_x[1]['nom']
        différence_espace = len(nom_joueur1) - len(nom_joueur2)
        espace_ajoutee_joueur2 = 0
        espace_ajoutee_joueur1 = 0
        if différence_espace > 0:
            espace_ajoutee_joueur2 = 0
            espace_ajoutee_joueur2 = ((' ' * (différence_espace)))
            murs_joueur1 = (nb_murs_joueur1 * '|')
            murs_joueur2 = (nb_murs_joueur2 * '|')
            legende = ("Légende:\n"
                       f"   1={nom_joueur1}, murs={murs_joueur1}\n"
                       f"   2={nom_joueur2}, {espace_ajoutee_joueur2}murs={murs_joueur2}\n")
            self.legende = legende
            return self.legende
        if différence_espace < 0:
            espace_ajoutee_joueur1 = 0
            espace_ajoutee_joueur1 = ((' ' * (-1 * (différence_espace))))
            murs_joueur1 = (nb_murs_joueur1 * '|')
            murs_joueur2 = (nb_murs_joueur2 * '|')
            legende = (
                "Légende:\n"   f"   1={nom_joueur1}, {espace_ajoutee_joueur1}murs={murs_joueur1}\n"
                f"   2={nom_joueur2}, murs={murs_joueur2}\n")
            return legende

        murs_joueur1 = nb_murs_joueur1 * '|'
        murs_joueur2 = nb_murs_joueur2 * '|'
        legende = ("Légende:\n"
                   f"   1={nom_joueur1}, murs={murs_joueur1}\n"
                   f"   2={nom_joueur2}, murs={murs_joueur2}\n")

        return legende

    def formater_damier(self):
        """Formater la représentation graphique du damier.

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
        murs_verticaux = self["murs"]["verticaux"]
        murs_horizontaux = self["murs"]["horizontaux"]
        positionnement_joueur1 = self["joueurs"][0]['pos']
        positionnement_joueur2 = self["joueurs"][1]['pos']

        for i in murs_verticaux:
            variable_x = damier.find(str(i[1]))
            damier = list(damier)
            variable_y = (4 + (4 * ((i[0]) - 1)) - 2)
            damier[variable_x + variable_y] = ('|')
            damier[variable_x + variable_y - 40] = ('|')
            damier[variable_x + variable_y - 80] = ('|')
            variable_z = ''.join(damier)
            damier = variable_z
        for i in murs_horizontaux:
            variable_x = damier.find(str(i[1]))
            damier = list(damier)
            variable_y = (+40 + 4 + (4 * ((i[0]))) - 5)
            damier[variable_y + variable_x] = ('-')
            damier[variable_y + variable_x + 1] = ('-')
            damier[variable_y + variable_x + 2] = ('-')
            damier[variable_y + variable_x + 3] = ('-')
            damier[variable_y + variable_x + 4] = ('-')
            damier[variable_y + variable_x + 5] = ('-')
            damier[variable_y + variable_x + 6] = ('-')
            variable_z = ''.join(damier)
            damier = variable_z
        variable_x = damier.find(str(positionnement_joueur1[1]))
        damier = list(damier)
        variable_y = (4 + (4 * ((positionnement_joueur1[0]) - 1)))
        damier[variable_y + variable_x] = ('1')
        variable_z = ''.join(damier)
        damier = variable_z
        variable_x = damier.find(str(positionnement_joueur2[1]))
        damier = list(damier)
        variable_y = (4 + (4 * ((positionnement_joueur2[0]) - 1)))
        damier[variable_y + variable_x] = ('2')
        variable_z = ''.join(damier)
        damier = variable_z
        return damier

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """
        damier = Quoridor.formater_damier(self)
        legende = Quoridor.formater_légende(self)
        return f"{legende}{damier}"

    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)

    def est_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        if self.état["joueurs"][0]["pos"][1] == 9:
            return self.état["joueurs"][0]["nom"]

        if self.état["joueurs"][1]["pos"][1] == 1:
            return self.état["joueurs"][1]["nom"]

        return False

    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
        """
        if joueur not in (1, 2):
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')

        type_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):")
        variable_x = input("Donnez la position où appliquer ce coup (x,y):")
        # type_coup ="MV"
        # x = ("4,2")
        if type_coup not in ('D', 'MV', 'MH'):
            raise QuoridorError("La position est invalide (en dehors du damier).")

        variable_p = int(variable_x[0])
        variable_w = int(variable_x[2])
        position = [variable_p, variable_w]
        return (type_coup, position)

    def déplacer_jeton(self, joueur, position):

        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        position1 = 0
        référence = (self.état["joueurs"][joueur - 1]["pos"][0]) + (self.état["joueurs"][joueur - 1]["pos"][1])
        if joueur not in (1, 2):
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')

        if position[0] > 9 or position[0] < 1:
            raise QuoridorError('La position est invalide (en dehors du damier).')

        if position[1] > 9 or position[1] < 1:
            raise QuoridorError('La position est invalide (en dehors du damier).')

        if position[0] + position[1] != référence + 1:
            if position[0] + position[1] != référence - 1:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

        graphe = construire_graphe(
            [tuple(joueur['pos']) for joueur in self.état['joueurs']],
            tuple(self.état['murs']['horizontaux']),
            tuple(self.état['murs']['verticaux']))

        choix_de_chemin = list(graphe.successors(tuple(self.état["joueurs"][joueur - 1]["pos"])))

        for i in choix_de_chemin:
            if tuple(position) == i:
                position1 = 'trouvé'

        if position1 != 'trouvé':
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

        # for i in self.état["murs"]["horizontaux"]:
        # if position[1] == i[1]:
        # if position[0] == i[0] or position[0] == i[0] + 1:
        # raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

        # for i in self.état["murs"]["verticaux"]:
        # if position[0] == i[0]:
        # if position[1] == i[1] or position[1] == i[1] + 1:
        # raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

        self.état["joueurs"][joueur - 1]["pos"] = position
        Quoridor.jouer_le_coup(Quoridor, 2)

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

        if joueur not in (1, 2):
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")

        for i in self.état["murs"]["horizontaux"]:
            if position[0] == i[0] + 1 and position[1] + 1 == i[1]:
                raise QuoridorError("Un mur occupe déjà cette position.")

        for i in self.état["murs"]["verticaux"]:
            if position[0] == i[0] - 1 and position[1] - 1 == i[1]:
                raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MH":
            for i in self.état["murs"]["horizontaux"]:
                if i[0] - 1 == position[0] and i[1] == position[1]:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MV":
            for i in self.état["murs"]["verticaux"]:
                if i[0] == position[0] and (i[1] - 1) == position[1]:
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
            if (1 <= position[0] <= 8) is False:
                raise QuoridorError("La position d'un mur est invalide.")

            if (2 <= position[1] <= 9) is False:
                raise QuoridorError("La position d'un mur est invalide.")

        if orientation == "MV":
            if (2 <= position[0] <= 9) is False:
                raise QuoridorError("La position d'un mur est invalide.")

            if (1 <= position[1] <= 8) is False:
                raise QuoridorError("La position d'un mur est invalide.")

        if self.état["joueurs"][joueur - 1]["murs"] <= 0:
            raise QuoridorError("Le joueur a déjà placé tous ses murs.")

        if orientation == "MV":
            état["murs"]["verticaux"] += [position]
            état["joueurs"][joueur - 1]["murs"] -= 1

        if orientation == "MH":
            état["murs"]["horizontaux"] += [position]
            état["joueurs"][joueur - 1]["murs"] -= 1

        graphe = construire_graphe(
            [tuple(joueur['pos']) for joueur in état['joueurs']],
            tuple(état['murs']['horizontaux']),
            tuple(état['murs']['verticaux']))

        if not nx.has_path(graphe, tuple(état["joueurs"][0]["pos"]), 'B1'):
            raise QuoridorError("La position du mur est invalide puisqu'elle enferme le joueur")

        if not nx.has_path(graphe, tuple(état["joueurs"][1]["pos"]), 'B2'):
            raise QuoridorError("La position du mur est invalide puisqu'elle enferme le joueur")

        if orientation == "MV":
            self.état["murs"]["verticaux"] += [position]
            self.état["joueurs"][joueur - 1]["murs"] -= 1

        if orientation == "MH":
            self.état["murs"]["horizontaux"] += [position]
            self.état["joueurs"][joueur - 1]["murs"] -= 1

        if joueur == 1:
            Quoridor.jouer_le_coup(Quoridor, 2)

        joueurs = self.état["joueurs"]
        murs = self.état["murs"]
        return (joueurs, murs)

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

        if joueur not in (1, 2):
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")

        if self.état["joueurs"][0]["pos"][1] == 9:
            raise QuoridorError(" QuoridorError: La partie est déjà terminée.")

        if self.état["joueurs"][1]["pos"][1] == 1:
            raise QuoridorError(" QuoridorError: La partie est déjà terminée.")

        graphe = construire_graphe(
            [tuple(joueur['pos']) for joueur in self.état['joueurs']],
            tuple(self.état['murs']['horizontaux']),
            tuple(self.état['murs']['verticaux']))

        liste_chemin_rapide_j1 = nx.shortest_path(graphe, tuple(self.état["joueurs"][0]["pos"]), 'B1')

        for i in liste_chemin_rapide_j1:
            if not isinstance(i, tuple):
                liste_chemin_rapide_j1.remove(i)

        choix_de_chemin_j1 = list(graphe.successors(tuple(self.état["joueurs"][0]["pos"])))
        for i in choix_de_chemin_j1:
            if not isinstance(i, tuple):
                choix_de_chemin_j1.remove(i)

        for i in liste_chemin_rapide_j1:
            for j in choix_de_chemin_j1:
                if j == i:
                    variable_x = j

        if len(choix_de_chemin_j1) > 1:
            if self.état["joueurs"][0]["pos"][0] != variable_x[0]:
                delta = self.état["joueurs"][0]["pos"][0] - variable_x[0]
                if delta < 0:
                    variable_k = self.état["joueurs"][0]["pos"][0]
                    variable_y = self.état["joueurs"][0]["pos"][1]
                    variable_ky = [(variable_k + 1), variable_y]
                if delta > 0:
                    variable_k = self.état["joueurs"][0]["pos"][0]
                    variable_y = self.état["joueurs"][0]["pos"][1]
                    variable_ky = [variable_k, variable_y]
                try:
                    Quoridor.placer_un_mur(Quoridor, 2, variable_ky, "MV")
                except QuoridorError:
                    variable_k = "ne peut pas mettre un mur"

            if self.état["joueurs"][0]["pos"][1] != variable_x[1]:
                variable_k = self.état["joueurs"][0]["pos"][0]
                variable_y = self.état["joueurs"][0]["pos"][1]
                variable_ky = [(variable_k - 1), (variable_y + 1)]
                for i in self.état["murs"]["horizontaux"]:

                    if i[1] == (variable_y + 1) and (i[0] + 2) == variable_k:
                        variable_ky = [variable_k, (variable_y + 1)]

                # pos = (list(self.état["joueurs"][0]["pos"]))
                # self.état['murs']['verticaux'] += ([pos])

                try:
                    Quoridor.placer_un_mur(Quoridor, 2, variable_ky, "MH")
                except QuoridorError:
                    variable_k = "ne peut pas mettre un mur"

            if variable_k == "ne peut pas mettre un mur":
                mouvement_rapide_j2 = nx.shortest_path(graphe, tuple(self.état["joueurs"][1]["pos"]), 'B2')
                self.état["joueurs"][1]["pos"] = list(mouvement_rapide_j2[1])
                joueurs = self.état["joueurs"]
                murs = self.état["murs"]
                return (joueurs, murs)
