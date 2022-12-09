from copy import deepcopy

from quoridor_error import QuoridorError

from graphe import construire_graphe

import networkx as nx

import copy

import turtle

from quoridor import Quoridor


def jouer_le_coup(état):
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

        

        


        graphe = construire_graphe(
            [tuple(joueur['pos']) for joueur in état['joueurs']],
            tuple(état['murs']['horizontaux']),
            tuple(état['murs']['verticaux']))

        liste_chemin_rapide_J2 = nx.shortest_path(graphe, tuple(état["joueurs"][1]["pos"]), 'B2')


        for i in liste_chemin_rapide_J2:
            if type(i) != tuple:
                liste_chemin_rapide_J2.remove(i)

        Choix_de_chemin_J2 = list(graphe.successors(tuple(état["joueurs"][1]["pos"])))

        for i in Choix_de_chemin_J2:
            if type(i) != tuple:
                Choix_de_chemin_J2.remove(i)

        for i in liste_chemin_rapide_J2:
            for j in Choix_de_chemin_J2:
                if j == i:
                    variable_x = j



        if len(Choix_de_chemin_J2) > 1:
            if état["joueurs"][1]["pos"][0] != variable_x[0]:
 
                delta = état["joueurs"][1]["pos"][0] - variable_x[0]
                if delta < 0:
                    variable_k = état["joueurs"][1]["pos"][0]
                    variable_y = état["joueurs"][1]["pos"][1]
                    variable_ky = [(variable_k+1), variable_y-1]
                if delta > 0:
                    variable_k = état["joueurs"][1]["pos"][0]
                    variable_y = état["joueurs"][1]["pos"][1]
                    variable_ky = [variable_k, variable_y-1]
                try:

                    position, orientation = placer_un_mur(état, 2, variable_ky, "MV")
                    print(position, orientation)
                    print("ligne 266")
                    return(position, orientation)
                except QuoridorError:
                     variable_k = "ne peut pas mettre un mur"





            if état["joueurs"][1]["pos"][1] != variable_x[1]:
                variable_k = état["joueurs"][1]["pos"][0]
                variable_y = état["joueurs"][1]["pos"][1]
                variable_ky = [(variable_k-1), (variable_y)]
                for i in état["murs"]["horizontaux"]:

                    if i[1] == (variable_y) and (i[0] + 2) == variable_k:
                        variable_ky = [variable_k, (variable_y+1)]



                try:

                    position, orientation = placer_un_mur(état, 2, variable_ky, "MH")
                    print(position, orientation)
                    print("ligne 266")
                    return (position, orientation)
                except QuoridorError:
                    variable_k = "ne peut pas mettre un mur"

            if variable_k == "ne peut pas mettre un mur":
                mouvement_rapide_J1 = nx.shortest_path(graphe, tuple(état["joueurs"][0]["pos"]), 'B1')

                position_mouv = list(mouvement_rapide_J1[1])

                p = int(position_mouv[0])
                w = int(position_mouv[1])
                position = [p, w]
                print(position)
                print("ligne 266")
                return (position, "D")


def placer_un_mur(état, joueur, position, orientation):

        
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
        état = copy.deepcopy(état)

        
        for i in état["murs"]["horizontaux"]:
            if position[0] == i[0]+1 and position[1]+1 == i[1]:
                raise QuoridorError("Un mur occupe déjà cette position.")

        for i in état["murs"]["verticaux"]:
            if position[0] == i[0]-1 and position[1]-1 == i[1]:
                raise QuoridorError("Un mur occupe déjà cette position.")



        if orientation == "MH":
            for i in état["murs"]["horizontaux"]:
                if i[0]-1 == position[0] and i[1] == position[1]:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MV":
            for i in état["murs"]["verticaux"]:
                if i[0] == position[0] and (i[1]+1) == position[1]:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MV":
            for i in état["murs"]["verticaux"]:
                if i == position:
                    raise QuoridorError("Un mur occupe déjà cette position.")

        if orientation == "MH":
            for i in état["murs"]["horizontaux"]:
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


        if état["joueurs"][joueur-2]["murs"] <= 0:
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





        if nx.has_path(graphe, tuple(état["joueurs"][1]["pos"]), 'B2') == False:

            raise QuoridorError("La position du mur est invalide puisqu'elle enferme le joueur")

        #if orientation == "MV":
            #état["murs"]["verticaux"] += [position]
            #état["joueurs"][joueur-1]["murs"] -=  1

        #if orientation == "MH":
            #état["murs"]["horizontaux"] += [position]
            #état["joueurs"][joueur-1]["murs"] -=  1


        
        return (position, orientation)


class QuoridorXA(Quoridor):
        def __init__(self, état):
            self.fen = turtle.Screen()
            self.fen.title("Quoridor phase 3")
            self.fen.setup(width=800, height=600)
            self.J1 = turtle.Turtle()
            self.J2 = turtle.Turtle()
            self.M1 = turtle.Turtle()
            self.M1.shape("square")
            self.M1.penup()
            self.M2 = turtle.Turtle()
            self.M2.penup()
            self.état = état
        
        
        def graphique():
            #fen = turtle.Screen()
            #fen.title("Quorido phase 3")
            #fen.setup(width=800, height=600)
            alex = turtle.Turtle()
            #création de l'arrière plan noir
            alex.penup()
            alex.speed("fast")
            alex.fillcolor("black")
            alex.begin_fill()
            alex.forward(400)
            alex.left(90)
            alex.forward(300)
            alex.left(90)
            alex.forward(800)
            alex.left(90)
            alex.forward(600)
            alex.left(90)
            alex.forward(800)
            alex.left(90)
            alex.forward(300)
            alex.end_fill()

            #périmètre du jeu
            clair = turtle.Turtle()
            clair.speed("fast")
            clair.shape("circle")
            clair.pencolor("white")
            clair.penup()
            clair.forward(200)
            clair.left(90)
            clair.pendown()
            clair.forward(200)
            clair.left(90)
            clair.forward(400)
            clair.left(90)
            clair.forward(400)
            clair.left(90)
            clair.forward(400)
            clair.left(90)
            clair.forward(200)
            clair.left(90)
            clair.penup()
            clair.forward(200)
            clair.right(90)
            clair.shapesize(0.1)
            

            #point dans le jeu
            clair.stamp()
            nombre_stamp = 1
            while nombre_stamp < 9:
                for i in range(nombre_stamp):
                    clair.forward(40)
                    clair.stamp()
                clair.right(90)
                for i in range(nombre_stamp):
                    clair.forward(40)
                    clair.stamp()
                clair.right(90)
            
                nombre_stamp +=1
            for i in range(8):
                    clair.forward(40)
                    clair.stamp()

            #chiffre de la grille
            #positionnement de Charles
            charles = turtle.Turtle()
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(200)
            charles.right(90)
            charles.forward(220)
            charles.right(90)
            charles.forward(30)
            #chiffre
            #1 
            charles.speed("fastest")       
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.color("black")
            charles.penup()
            charles.forward(20)
            #2
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.forward(1)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.forward(40)
            #3
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.forward(1)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.forward(1)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.left(90)
            charles.forward(20)
            #4
            
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(104)
            charles.penup()
            charles.color("black")
            charles.forward(10)
            charles.right(90)
            charles.pendown()
            charles.color("white")
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.left(90)       
            charles.forward(20)
            
            #5
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(166)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.left(90)
            charles.forward(40)
            charles.left(90)
            charles.forward(5)
            charles.right(90)
            #6
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.right(90)
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(76)
            charles.penup()
            charles.color("black")
            charles.forward(10)
            charles.left(90)
            charles.forward(40)
            #7
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.right(90)
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(76)
            charles.penup()
            charles.color("black")
            charles.forward(15)
            charles.left(90)
            charles.forward(40)
            #8
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.right(90)
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(76)
            charles.penup()
            charles.color("black")
            charles.forward(20)
            charles.left(90)
            charles.forward(40)
            #9
            charles.right(90)
            charles.forward(4.96)
            charles.left(116.47)
            charles.color("white")
            charles.pendown()
            charles.forward(22.34)
            charles.left(180)
            charles.forward(22.34)
            charles.penup()
            charles.color("black")
            charles.right(116.47)
            charles.forward(9.92)
            charles.right(116.47)
            charles.color("white")
            charles.pendown()
            charles.forward(22.34)
            charles.left(180)
            charles.forward(22.34)
            charles.penup()
            charles.color("black")
            charles.right(63.53)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.forward(60)

            
            
            
            
            
            #horizontal
            charles.right(90)
            charles.forward(66)
            charles.left(90)
            #chiffre
            #1 
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(37)
            charles.left(90)
            #2
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(33)
            charles.left(90)
            #3
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.left(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(38)
            charles.left(90)
            #4
            
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(104)
            charles.penup()
            charles.color("black")
            charles.forward(10)
            charles.right(90)
            charles.pendown()
            charles.color("white")
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.left(90)
            charles.penup()
            charles.color("black")
            charles.forward(10)      
            charles.forward(37)
            charles.left(90)
            
            #5
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(166)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(45)
            charles.left(90)
            #6
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.right(90)
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(76)
            charles.penup()
            charles.color("black")
            charles.forward(10)
            charles.forward(45)
            charles.left(90)
            #7
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.right(90)
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(76)
            charles.penup()
            charles.color("black")
            charles.forward(15)
            charles.forward(42)
            charles.left(90)
            #8
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.right(90)
            charles.forward(10)
            charles.right(90)
            charles.right(14)
            charles.color("white")
            charles.pendown()
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.right(152)
            charles.forward(20.5)
            charles.right(180)
            charles.forward(20.5)
            charles.left(76)
            charles.penup()
            charles.color("black")
            charles.forward(20)
            charles.forward(30)
            charles.left(90)
            #9
            charles.right(90)
            charles.forward(4.96)
            charles.left(116.47)
            charles.color("white")
            charles.pendown()
            charles.forward(22.34)
            charles.left(180)
            charles.forward(22.34)
            charles.penup()
            charles.color("black")
            charles.right(116.47)
            charles.forward(9.92)
            charles.right(116.47)
            charles.color("white")
            charles.pendown()
            charles.forward(22.34)
            charles.left(180)
            charles.forward(22.34)
            charles.penup()
            charles.color("black")
            charles.right(63.53)
            charles.forward(5)
            charles.right(90)
            charles.color("white")
            charles.pendown()
            charles.forward(20)
            charles.right(180)
            charles.forward(20)
            charles.penup()
            charles.color("black")
            charles.left(90)
            charles.forward(5)
            charles.forward(50)
        
        def légende_murs_départ():
            Joe = turtle.Turtle()
            Joe.penup()
            Joe.shape('circle')
            Joe.shapesize(0.1)
            Joe.color('black')
            Joe.speed('fastest')
            Joe.pensize(1)

            #positionnement joueur1
            Joe.right(90)
            Joe.forward(250)
            Joe.right(90)
            Joe.forward(300)
            Joe.right(90)

            #Mur
            #M
            Joe.pendown()
            Joe.color('blue')
            Joe.forward(20)
            Joe.right(135)
            Joe.forward(7)
            Joe.left(90)
            Joe.forward(7)
            Joe.right(135)
            Joe.forward(21)
            Joe.penup()
            Joe.color('black')
            Joe.left(90)
            Joe.forward(5)
            Joe.left(90)
            Joe.forward(10)
            Joe.right(180)
            #u
            Joe.pendown()
            Joe.color('blue')
            Joe.forward(9)
            Joe.left(90)
            Joe.forward(7)
            Joe.left(90)
            Joe.forward(9)
            Joe.right(180)
            Joe.forward(10)
            Joe.penup()
            Joe.color('black')
            Joe.left(90)
            Joe.forward(5)
            Joe.left(90)
            #r
            Joe.pendown()
            Joe.color('blue')
            Joe.forward(10)
            Joe.right(90)
            Joe.forward(7)
            Joe.penup()
            Joe.color('black')
            Joe.right(90)
            Joe.forward(10)
            Joe.left(90)
            Joe.forward(5)
            Joe.left(90)
            Joe.forward(2.5)
            Joe.color('blue')
            Joe.stamp()
            Joe.forward(5)
            Joe.stamp()
            Joe.color('black')
            Joe.right(180)
            Joe.forward(7.5)
            Joe.left(90)
            Joe.forward(10)
            Joe.left(90)
            
            #Murs
            for i in range(10):
                Joe.pendown()
                Joe.color('blue')
                Joe.forward(20)
                Joe.right(180)
                Joe.forward(20)
                Joe.penup
                Joe.color('black')
                Joe.left(90)
                Joe.forward(10)
                Joe.left(90)

            #positionnement joueur2
            Joe.left(90)
            Joe.forward(149.071)
            Joe.left(90)
            Joe.forward(25)
            Joe.left(180)

    #Mur
            #M
            Joe.pendown()
            Joe.color('red')
            Joe.forward(20)
            Joe.right(135)
            Joe.forward(7)
            Joe.left(90)
            Joe.forward(7)
            Joe.right(135)
            Joe.forward(21)
            Joe.penup()
            Joe.color('black')
            Joe.left(90)
            Joe.forward(5)
            Joe.left(90)
            Joe.forward(10)
            Joe.right(180)
            #u
            Joe.pendown()
            Joe.color('red')
            Joe.forward(9)
            Joe.left(90)
            Joe.forward(7)
            Joe.left(90)
            Joe.forward(9)
            Joe.right(180)
            Joe.forward(10)
            Joe.penup()
            Joe.color('black')
            Joe.left(90)
            Joe.forward(5)
            Joe.left(90)
            #r
            Joe.pendown()
            Joe.color('red')
            Joe.forward(10)
            Joe.right(90)
            Joe.forward(7)
            Joe.penup()
            Joe.color('black')
            Joe.right(90)
            Joe.forward(10)
            Joe.left(90)
            Joe.forward(5)
            Joe.left(90)
            Joe.forward(2.5)
            Joe.color('red')
            Joe.stamp()
            Joe.forward(5)
            Joe.stamp()
            Joe.color('black')
            Joe.right(180)
            Joe.forward(7.5)
            Joe.left(90)
            Joe.forward(10)
            Joe.left(90)
            
            #Murs
            for i in range(10):
                Joe.pendown()
                Joe.color('red')
                Joe.forward(20)
                Joe.right(180)
                Joe.forward(20)
                Joe.penup
                Joe.color('black')
                Joe.left(90)
                Joe.forward(10)
                Joe.left(90)

    

        def positionnement_joueur(self):
    
            #positionnement m1 et m2
            M1 = turtle.Turtle()
            self.M1 = M1
            M2 = turtle.Turtle()
            self.M2 = M2
            self.M1.penup()
            self.M2.penup()
            self.M1.forward(250)
            self.M1.right(180)
            self.M2.forward(250)
            self.M2.right(180)
            #joueur
            J1 = turtle.Turtle()
            self.J1 = J1
            self.J1.penup()
            self.J1.shape('turtle')
            self.J1.color("blue")
            J2 = turtle.Turtle()
            self.J2 = J2
            self.J2.penup()
            self.J2.shape('turtle')
            self.J2.color("red")
            #positionnement initial
            
            self.J1.right(90)
            self.J1.forward(170)
            self.J1.left(180)
            
            self.J2.left(90)
            self.J2.forward(170)
            self.J2.right(180)
            
        def déplacement_joueur(self, position, état):
            
            delta_x = état["joueurs"][0]["pos"][0] - position[0]
            delta_y = état["joueurs"][0]["pos"][1] - position[1]

            if delta_y != 0:
                if delta_y == -1:
                    self.J1.forward(40)
                if delta_y == 1:
                    self.J1.right(180)
                    self.J1.forward(40)
                    self.J1.right(90)

            if delta_x != 0:
                if delta_x == -1:
                    self.J1.right(90)
                    self.J1.forward(40)
                    self.J1.left(90)
                    
                if delta_x == 1:
                    self.J1.left(90)
                    self.J1.forward(40)
                    self.J1.right(90)
            
            état = copy.deepcopy(état)
            self.état = état

        def placement_mur(self, position, orientation, état, joueur):
            print(état)
            print("état ligne 846")
            
            if orientation == 'MV':
                self.M1.penup()
                print('???')
                self.M1.forward(250)
                if joueur == 1:
                    self.M1.color('blue')
                if joueur == 2:
                    self.M1.color('red')
                self.M1.speed('normal')
                
                ### ne pas toucher
                if 1 <= position[0] < 5:
                    print("****")
                    déplacement = (5 - int(position[0]))*40
                    self.M1.forward(déplacement+20)
                    self.M1.right(90)
                
                    
                ### ne pas toucher 
                if 9 >= position[0] > 5:
                    print("mmmm")
                    déplacement = (5 - int(position[0]))*-40
                    self.M1.right(180)
                    self.M1.forward(déplacement-20)
                    self.M1.left(90)

                ### ne pas toucher 
                if 1 <= position[1] < 5:
                    print("&&&&")
                    self.M1.right(180)
                    déplacement = (5 - int(position[1]))*40
                    self.M1.forward(déplacement+20)
                    self.M1.left(180)
                ### ne pas toucher
                if 9 >= position[1] > 5:
                    print("jjjjj")
                    déplacement = (5 - int(position[1]))*-40
                    self.M1.forward(déplacement-20)

                
                self.M1.pendown()
                self.M1.forward(80)
                self.M1.penup()
                self.M1.goto((250,0))
                self.M1.color('white')
                self.M1.left(90)
                if joueur == 1:
                    état['murs']['verticaux'] += [position]

            
        



            if orientation == 'MH':
                
                self.M1.penup()
                self.M1.forward(250)
                if joueur == 1:
                    self.M1.color('blue')
                if joueur == 2:
                    self.M1.color('red')
                self.M1.speed('normal')
                
                ### ne pas toucher
                if 1 <= position[0] < 5:
                    print('****')
                    déplacement = (5 - int(position[0]))*40
                    self.M1.forward(déplacement+20)
                    self.M1.right(90)
                
                    
                if 9 >= position[0] > 5:
                    print("mmmm")
                    déplacement = (5 - int(position[0]))*-40
                    self.M1.right(180)
                    self.M1.forward(déplacement-20)
                    self.M1.left(90)
                
                #### ne pas toucher
                if 1 <= position[1] < 5:
                    print('????')
                    self.M1.right(180)
                    déplacement = (5 - int(position[1]))*40
                    self.M1.forward(déplacement+20)
                    self.M1.right(180)
                

                if 9 >= position[1] > 5:
                    print("jjjjj")
                    déplacement = (5 - int(position[1]))*-40
                    self.M1.forward(déplacement-20)
                
                
                self.M1.right(90)
                self.M1.pendown()
                self.M1.forward(80)
                self.M1.penup()
                self.M1.goto((250,0))
                self.M1.color('white')
                self.M1.left(180)
                if joueur == 1:
                    état['murs']['horizontaux'] += [position]
                
            
            print(état)
            print("état ligne 947")
            état = copy.deepcopy(état)
            self.état = état
        
        def analyser_mouv_bot(self, état):
            print(self.état)
            print('ligne(951)')
            print(état)
            print('ligne(953)')

            if self.état["joueurs"][1]["pos"] != état["joueurs"][1]["pos"]:
                position_J2 = état["joueurs"][1]["pos"]
                QuoridorXA.déplacement_joueur2(QuoridorXA, position_J2, self.état)

            if self.état["murs"]["verticaux"] != état["murs"]["verticaux"]:
                position_MV = état["murs"]["verticaux"][len(état["murs"]["verticaux"])-1]
                QuoridorXA.placement_mur(QuoridorXA, position_MV, "MV", état, 2)

            if self.état["murs"]["horizontaux"] != état["murs"]["horizontaux"]:
                position_MH = état["murs"]["horizontaux"][len(état["murs"]["horizontaux"])-1]
                QuoridorXA.placement_mur(QuoridorXA, position_MH, "MH", état, 2)

        def déplacement_joueur2(self, position, état):
            delta_x = état["joueurs"][1]["pos"][0] - position[0]
            delta_y = état["joueurs"][1]["pos"][1] - position[1]

            if delta_y != 0:
                if delta_y == 1:
                    self.J2.forward(40)
                if delta_y == -1:
                    self.J2.right(180)
                    self.J2.forward(40)
                    self.J2.right(90)

            if delta_x != 0:
                if delta_x == 1:
                    self.J2.right(90)
                    self.J2.forward(40)
                    self.J2.left(90)
                    
                if delta_x == -1:
                    self.J2.left(90)
                    self.J2.forward(40)
                    self.J2.right(90)

   