from quoridor import Quoridor
import turtle

class QuoridorX(Quoridor):
    
    def graphique(self):
        fen = turtle.Screen()
        fen.title("Quorido phase 3")
        fen.setup(width=800, height=600)
        alex = turtle.Turtle()
