# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.


class Product:
        def __init__(self, cost, price, marque):
                self.cost = cost
                self.price = price
                self.marque = marque
                self.name=type(self).__name__


class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product:Product, quantity):
        """
        'product' : un objet de type produit qui rassemble les différents attributs et caractéristiques de ce dernier
        'quantity' : un entier qui représente le nombre des pièces du produit en question
        """
        # Initialisation des variables
        """
        Vous devez initialiser deux variables. 
        la variable 'sales' qui stocke le total des revenues des ventes du produit
        la variable 'expenses' qui stocke le total des dépenses pour restocker le produit
        
        """
        self.product = product
        self.quantity = quantity
        sales = 0
        expenses = 0

    #Méthode Sell
    """
    La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
    Elle met également à jour les ventes totales pour le produit.
    
    """
    def sell(self, quantity):
        #Avant de mettre à jour l'état du stocke du produit, on doit vérifier si on a déjà une quantité suffisante à vendre.
        """
        En utilisant des conditions, vérifier: 

        SI la quantité en stock est inférieure à la quantité demandée:
            Afficher "Le stock du produit [nom du produit] est insuffisant."
            Retourner Faux
        SINON:
            Réduire la quantité en stock par la quantité demandée
            Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
            Retourner Vrai
        
        """
        if(self.quantity < quantity):
            print(f"Le stock du produit {self.product.name} est insuffisant.")
            return(False)
        else:
            self.quantity -= quantity
            self.sales += (quantity * self.product.price)
            return(True)
    
    #Méthode Restock
    """
    La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
    Elle met également à jour les dépenses totales pour restocker ce produit.
    """
    def restock(self, quantity):
        """
        Ajouter la quantité reçue à la quantité en stock
        Ajouter le coût total de la nouvelle quantité reçue  à la variable 'expenses' en multipliant la quantité reçue par le coût du produit
        """
        self.quantity += quantity
        self.expenses += (quantity * self.product.cost)

    #Méthode repr
    """
    La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
    qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.

    """
    def __repr__(self):
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        caract_produit = f"Nom du produit : {self.product.name}\nMarque : {self.product.marque}\nQuantité en stock : {self.quantity}\nPrix du produit : {self.product.price} €"
        return(caract_produit)



# monproduit = Product(50,100,"PEPOUZE")
# machaise1 = InventoryProductEntry(monproduit, 50)


# print(repr(machaise1))
