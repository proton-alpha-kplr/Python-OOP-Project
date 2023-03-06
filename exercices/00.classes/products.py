class Product:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque

class Meuble(Product):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension):
        super().__init__(cost, price, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimension = dimension

class Canape(Meuble):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension, nom):
        super().__init__(cost, price, marque, materiaux, couleur, dimension)
        self.nom = nom


class Chaise(Meuble):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension, nom):
        super().__init__(cost, price, marque, materiaux, couleur, dimension)
        self.nom = nom


class Table(Meuble):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension, nom):
        super().__init__(cost, price, marque, materiaux, couleur, dimension)
        self.nom = nom


canape1 = Canape(1000, 2000, "OKLM", "Tissu","Blanc","200x100x80", "Canape")
canape2 = Canape(800, 1600, "SIESTA", "Tissu","Bleu","150x90x70", "Canape")

chaise1 = Canape(50, 100, "PEPOUSE", "Plastique","Rouge","50x50x70", "Canape")
chaise2 = Canape(75, 150, "PEPOUSE", "Métal","Gris","60x60x80", "Canape")

table1 = Canape(250, 500, "TEX", "Bois","Chêne","150x80x75", "Canape")
table2 = Canape(350, 700, "350", "Verre","Transparent","120x60x75", "Canape")

print(canape1.materiaux)

