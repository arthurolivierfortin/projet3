from quoridor import Quoridor
import turtle

class QuoridorX(Quoridor):
    
    def graphique():
        fen = turtle.Screen()
        fen.title("Quorido phase 3")
        fen.setup(width=800, height=600)
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
    
    def positionnement_joueur(état):
        print(état)
        
        #joueur
        J1 = turtle.Turtle()
        J1.penup()
        J1.shape('turtle')
        J1.color("blue")
        J2 = turtle.Turtle()
        J2.penup()
        J2.shape('turtle')
        J2.color("red")
        #positionnement initial
        
        J1.right(90)
        J1.forward(170)
        J1.left(180)
        
        J2.left(90)
        J2.forward(170)
        J2.right(180)
    
    def légende_murs_départ(état):
        Joe = turtle.Turtle()
        Joe.penup()
        Joe.shape('circle')
        Joe.shapesize(0.5)
        Joe.color('black')

        #positionnement
        Joe.right(90)
        Joe.forward(250)
        Joe.right(90)
        Joe.forward(300)
        Joe.right(90)
        Joe.pendown()
        Joe.color('white')
        Joe.forward(20)
        Joe.right(135)
        Joe.forward(10)
        Joe.left(90)
        Joe.forward(10)
        Joe.right(135)
        Joe.forward(20)
        Joe.penup()
        Joe.color('black')
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        Joe.forward(10)
        Joe.right(180)
        Joe.pendown()
        Joe.color('white')
        Joe.forward(10)
        Joe.left(90)
        Joe.forward(10)
        Joe.left(90)
        Joe.forward(10)
        Joe.right(180)
        Joe.forward(10)
        Joe.penup()
        Joe.color('black')
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        Joe.pendown()
        Joe.color('white')
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
        Joe.color('white')
        Joe.stamp()
        Joe.forward(5)
        Joe.stamp()
        Joe.color('black')
        Joe.right(180)
        Joe.forward(7.5)
        Joe.left(90)
        Joe.forward(10)


