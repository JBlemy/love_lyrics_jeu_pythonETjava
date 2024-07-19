import turtle

# Création d'une tortue et d'une fenêtre graphique
t = turtle.Turtle()
s = turtle.Screen()

# Configuration de la couleur de fond de la fenêtre
s.bgcolor('black')

# Configuration de la vitesse de la tortue
t.speed(0)

# Liste des couleurs à utiliser
col = ["yellow", "red", "pink", "cyan", "lightgreen", "blue"]

# Boucle pour dessiner la figure étoilée
for i in range(150):
    # Sélection de la couleur du stylo en fonction de l'itération
    t.pencolor(col[i % 6])
    
    # Dessin du premier cercle
    t.circle(190 - i / 2, 90)
    
    # Rotation de la tortue de 90 degrés à gauche
    t.lt(90)
    
    # Dessin du deuxième cercle
    t.circle(190 - i / 3, 90)
    
    # Rotation de la tortue de 60 degrés à gauche
    t.lt(60)

# Fermeture de la fenêtre graphique lors d'un clic
s.exitonclick()

