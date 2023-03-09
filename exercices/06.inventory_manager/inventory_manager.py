#La classe "InventoryManager" est une classe qui permet de gérer un inventaire de produits. 
class Product:
        def __init__(self, cost, price, marque): #, name):
                self.cost = cost
                self.price = price
                self.marque = marque
                self.name = type(self).__name__ #name
                #attention, si le nom du produit est le nom de sa classe, on ne peut avoir qu'un type de chaise, un type de pantalon,...


#from product_classes import Chaise, Pantalon

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
        self.sales = 0
        self.expenses = 0

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























class InventoryManager:
    # Initialisation de la classe
    def __init__(self):
        # Vous initialisez un dictionnaire 'inventory' qui stocke l'inventaire de tous les produits
        # Il prend comme clé le nom du produit, et la valeur est un objet InventoryProductEntry
        self.inventory : dict[str, InventoryProductEntry] = {}

    #Méthode product_exists
    """"
    La fonction prend un objet Product en entrée et vérifie si son nom est une clé dans le dictionnaire self.inventory. 
    Si c'est le cas, la fonction retourne True, sinon elle retourne False.
    """
    def product_exists(self,product:Product):
        """
        pour chaque 'inventory_product_entry_key' dans self.inventory faire:
            si 'inventory_product_entry_key' est égal à product.name alors:
                retourner True
        retourner False
        """
        produitexistedansinventaire = False
        for nom_produit in self.inventory:
            if nom_produit == product.name:
                produitexistedansinventaire = True

        return(produitexistedansinventaire)
       
    
    #Méthode add_product
    """
    La méthode add_product est utilisée pour ajouter un nouveau produit à l'inventaire.
    Elle prend en argument un objet Product et une quantité initiale.
    """
    def add_product(self, product:Product, quantity):
        """
        SI le produit existe déjà dans l'inventaire: 
            afficher un message pour informer l'utilisateur
        Sinon:
            Créer un nouvel objet InventoryProductEntry en utilisant le produit et la quantité fournis
            Ajouter le nouvel objet au dictionnaire 'inventory'
        """
        if self.product_exists(product):
            print("Le produit existe déjà dans l'inventaire")
        else:
            self.inventory[product.name] = InventoryProductEntry(product, quantity)




    #Méthode remove_product
    """
    La méthode remove_product est utilisée pour supprimer un produit de l'inventaire.
    Elle prend en argument un nom de produit et supprime l'entrée correspondante dans le dictionnaire 'inventory'.
    """
    def remove_product(self, product:Product):
        #Utiliser la méthode product_exists pour vérifier si le produit existe dans l'inventaire
        #Si le produit est trouvé, supprimer le de l'inventaire
        #Sinon, afficher un message d'erreur indiquant que le produit n'a pas été trouvé

        if not self.product_exists(product):
            print("Le produit n'existe pas dans l'inventaire")
        else:
            del(self.inventory[product.name])

    #Méthode sell_product
    """
    La méthode sell_product est utilisée pour vendre une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à vendre.
    """
    
    def sell_product(self, product:Product, quantity):
        #Utiliser une boucle pour parcourir les clés du dictionnaire 'inventory'
        #Pour chaque itération, on vérifie si le nom du produit fourni est équal à la clé du dictionnaire.
        #Si le produit est trouvé, appeler la méthode 'sell' de l'objet InventoryProductEntry correspondant avec la quantité à vendre
        #Sinon, afficher un message d'erreur indiquant que la vente a échoué

        if not self.product_exists(product):
            print(f"Erreur, le produit {product.name} ne fait pas partie de l'inventaire")
        else :
            for nom_produit in self.inventory:
                if nom_produit == product.name:
                    self.inventory[nom_produit].sell(quantity)            


    #Méthode restock_product
    """
    La méthode restock_product est utilisée pour restocker une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à restocker.
    """
    def restock_product(self, product:Product, quantity):
        #Vérifier si le produit existe déjà dans l'inventaire
        #Si le produit est trouvé, appeler la méthode 'restock' de l'objet InventoryProductEntry correspondant avec la quantité à restocker
        #Si le réapprovisionnement est réussi, afficher un message de confirmation
        #Sinon, on appelle la méthode add_product pour ajouter le produit en stock avec une quantité nulle et on rappelle la fonction restock_product pour le restocker
        
        if self.product_exists(product):
            self.inventory[product.name].restock(quantity)
            print(f"Le produit {product.name} a été restocké de {quantity} articles.")

        else:    
            self.add_product(product, 0)
            self.restock_product(product, quantity)
        


    #Méthode get_product
    """
    La méthode get_product retourne toutes les informations liées au produit en faisant une recherche par son nom.
    Elle prend en entrée un nom de produit.
    """
    def get_product(self, name):
        """
        pour chaque inventory_product_entry_key dans self.inventory:
            si inventory_product_entry_key == nom de produit:
                retourner self.inventaire[inventory_product_entry_key].product
        afficher un message pour indiquer que le produit n'existe pas
        """
        produitdansinventaire = False
        for nom_produit in self.inventory:
            if nom_produit == name:
                produitdansinventaire = True
                return(self.inventory[nom_produit])
        if not produitdansinventaire :
            print(f"Le produit {name} n'existe pas dans l'inventaire")



    #Méthode list_products
    """
    La méthode list_products(self) parcourt tous les produits de l'inventaire 
    et affiche les informations relatives à chacun d'entre eux (nom, quantité disponible, prix unitaire, coût unitaire, prix de vente unitaire, bénéfice unitaire). 
    """
    def list_products(self):
        """
        pour chaque clé du dictionnaire 'inventory':
            afficher la valeur correspondante à cette clé
        retourner le dictionnaire inventaire
        """
        infos = []
        for nom_produit in self.inventory:
            #infos += repr(self.inventory[nom_produit])
            #infos += "\n\n"
            infos.append(f"{nom_produit} ({self.inventory[nom_produit].product.marque}): {self.inventory[nom_produit].quantity} in stock, price:{self.inventory[nom_produit].product.price}")
            #"Chaise (Ikea): 5 in stock,  price:100"

        return(infos)


# monproduitchaise1 = Product(50,100,"PEPOUZE")
# moninventaire = InventoryManager()
# moninventaire.add_product(monproduitchaise1, 50)
# print(moninventaire.list_products())



# """
# # moninventaireduprod = InventoryProductEntry(monproduitchaise1, 100)

# # print(repr(moninventaireduprod))

# # moninventaireduprod.sell(20)

# # print(repr(moninventaireduprod))
# """

# monproduitchaise2 = Product(200,500,"MASUPERCHAISE", "machaise2")

# monproduitchaise3 = Product(5,10,"MACHAISEPOURRIE", "machaise3")


# moninventaire.add_product(monproduitchaise2, 100)
# moninventaire.add_product(monproduitchaise3, 2)



# moninventaire.remove_product(monproduitchaise2)

# moninventaire.list_products()

# moninventaire.remove_product(monproduitchaise2)

# moninventaire.add_product(monproduitchaise2, 100)

# moninventaire.add_product(monproduitchaise2, 100)

# moninventaire.list_products()

# moninventaire.sell_product(monproduitchaise2, 55)

# moninventaire.list_products()

# moninventaire.sell_product(monproduitchaise2, 50)

# moninventaire.restock_product(monproduitchaise2, 50)

# moninventaire.sell_product(monproduitchaise2, 50)

# # print(moninventaire.inventory.keys(), moninventaire.inventory.values())

# moninventaire.list_products()


# machaise = Chaise("materiau2", "couleur2", "dimension2", 50, 100, "Ikea")
# monpantalon = Pantalon("M", "noir", "jeans", 150, 200,"Zara")

# print(machaise.name)
# print(monpantalon.name)
