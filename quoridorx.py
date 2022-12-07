from quoridor import Quoridor
import turtle

class QuoridorX(Quoridor):
    
    def graphique(self):
        fen = turtle.Screen()
        fen.title("Quorido phase 3")
        fen.setup(width=800, height=600)
        alex = turtle.Turtle()
        #création de l'arrière plan noir
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
        clair.shape("dot")
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
        clair.forward(200)
        clair.pensize(4)

        #point dans le jeu
        
        for i in range(10**2):
            i += 1
            clair.forward(40*i)
            clair.right(90)
            
        