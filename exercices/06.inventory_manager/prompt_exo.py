import sys
sys.path.extend(['.','..'])
from inventory_product_entry import *
from inventory_manager import *
from product_classes import *
from class_hierarchy import generate_class_hierarchy
from arbre_json_data import *
import json
from unidecode import unidecode
import treelib
#import generator

import readline
import os
import utils

# Define the prompt_for_instance function a
# that takes a class name as a string as input
def prompt_for_instance(cls):
    # Get the class object from the class name string
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)


# on cree une classe Tree qui herite de treelib.Tree
# et rajoute deux fonctionnalités supplémentaires
# get_penultimate_nodes -> recupère les avant derniers noeuds
# get_children_nodes -> recupère les noeud terminaux
class TreeExt(treelib.Tree):
    def __init__(self):
        super().__init__()
    
    def get_penultimate_nodes(self):
        penultimate_nodes = set()
        for node in self.all_nodes():
            if not self.children(node.identifier):
                parent_node = self.parent(node.identifier)
                if parent_node is not None and not self.children(node.identifier):
                    penultimate_nodes.add(parent_node.identifier)
        return penultimate_nodes
    
    # Define a function to get the immediate children nodes of a specified node
    def get_children_nodes(self, node_name):
        children_nodes = []
        node = self.get_node(node_name)
        if node is not None:
            children = self.children(node.identifier)
            children_nodes = [child.identifier for child in children]
        return children_nodes

def sep():
    print("====================")


def main():

    inventory_manager = InventoryManager()
    # write code to read json file as dict

    # Charger des données JSON à partir du fichier dans un dictionnaire python
    json_dict = json_dict_from_file()

    readline.set_completer_delims(' \t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, list):
        matching_entry = [entry for entry in list if entry.startswith(text)]
        if len(matching_entry) == 1:
            entry_name = matching_entry[0]
            remaining_text = entry_name[len(text):]
            if remaining_text:          
                readline.insert_text(remaining_text)
                readline.redisplay()
                
    def set_autocomplete(list):
        readline.set_completer(lambda text, state: auto_complete(text,list))

    while True:
        print("""
			What would you like to do? :
			A. Add a product to stock
			R. Restock a product quantity
			S. Sell a product quantity
			D. Remove a product from stock
			L. List the products in stock
			B. Show the current balance
			Q. Quit
		""")

        
        choice = input("Enter your choice: ")
        choice = choice.upper()
        

        if choice == "A":
            
            #utils.print_list
            
            # write code to get class tree hierachy
            print(type(json_dict))
            class_tree = create_tree_from_dict(json_dict)
            print(type(class_tree))
            # convert the tree object to TreeExt to get the new functionalities 
            # described above in TreeExt class

            #class_tree = TreeExt()
            #print(type(class_tree))
            #print(class_tree)
            
            # ecrire le code pour récupérer les avant dernier noeuds de classe
            # (dernier niveau de catégories de produits)
            product_classes = class_tree.get_penultimate_nodes()
        
            sep()

            # write code to print list of product_classes
            #
            set_autocomplete(product_classes)
            category = input("Enter the category of the product: ")
            
            # Get the immediate children nodes of node 'B'
            children_nodes = class_tree.get_children_nodes(category)
            # write code to print list of children_nodes
            #
            set_autocomplete(children_nodes)
            
            product_name = input("Enter your product choice: ")   


            # write code to create a instance of classe product_name
            product_entry = prompt_for_instance(globals()[product_name])


            quantity = int(input("Enter quantity: "))
            # write code to add product_entry and quantity in Inventory Manager

            inventory_manager.add_product(product_entry, quantity)
            print(f"{product_entry.name} has been added to stock with a quantity of {quantity}.")

        # elif choice == "R":
        #     name = input("Enter the name of the product: ")
        #     quantity = int(input("Enter the quantity to restock: "))
        #     # write code to get product by name
        #     # 
        #     # write code to restock product
        #     # 



        # elif choice == "S":
        #     name = input("Enter the name of the product: ")
        #     quantity = int(input("Enter the quantity to sell: "))
        #     # write code to get product by name
        #         # 
        #     # write code to sell product
        #         # 

        # elif choice == "D":
        #     name = input("Enter the name of the product: ")
        #     # write code to get product
        #         # 
        #         #
        #         #
        #     #if product:
        #         # write code to remove product
        #         # 
        #         #
        #         #
        #         #print(f"{name} has been removed from stock.")
        #     #else:
        #         #print(f"{name} is not in stock.")

        # elif choice == "L":
        #     inventory_manager.list_products()

        # elif choice == "B":
        #     # write code to print current balance
        #         # 
        #     # supprimer la ligne suivante apres avoir ecrit cotre code
        #     pass
        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
