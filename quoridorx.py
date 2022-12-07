from quoridor import Quoridor
import turtle

class QuoridorX(Quoridor):
    
    def graphique(self):
        fen = turtle.Screen()
        fen.title("Quorido phase 3")
        fen.setup(width=800, height=600)
        alex = turtle.Turtle()
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
        alex.forward(900)
        alex.end_fill()