# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree
import os


# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
def json_dict_from_file():
    """
    Cette fonction ouvre et charge les données JSON du fichier
    dans un dictionnaire Python.

    Returns:
        dict: le dictionnaire Python contenant les données JSON du fichier
    """
    # Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    
    # il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)
    #print(json_dict)
    return json_dict



# Fonction pour créer un arbre à partir d'un dictionnaire Python

def create_tree_from_dict(json_dict):
    # Créer un nouvel arbre
    mytree = Tree()
    # Créer le noeud racine de l'arbre
    mytree.create_node(tag="Racine", identifier="racine")
    
    # Parcourir récursivement le dictionnaire Python pour créer les noeuds de l'arbre (fonction ci dessous)
    recursive_tree_from_json(mytree, json_dict, "racine")

    # Retourner l'arbre
    mytree.show()

# Fonction récursive pour parcourir un dictionnaire Python et créer des noeuds dans un arbre
def recursive_tree_from_json(tree, json_dict, parent_node_id):
    for key, value in json_dict.items():
        if (key == "subclasses"):
            recursive_tree_from_json(tree, value, parent_node_id)
        elif (isinstance(value, dict) ):  #enlever les valeur nulles
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            recursive_tree_from_json(tree, value, new_node_id)
        #elif not (isinstance(value, dict)):
        #    pass

    # Pour chaque clé (class_name) et valeur (class_attrs) dans le dictionnaire :
    #     Créer un nouveau noeud pour la clé courante du dictionnaire (nom de la classe)
    #     Ajouter le nouveau noeud en tant que fils du noeud parent

    #     Si "subclasses" est dans les attributs de la classe en cours (soit : valeur(class_attrs))
    #         Appeler récursivement la fonction pour créer les sous-noeuds de ce dictionnaire

# Fonction principale
def main():
    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    # Créer l'arbre à partir du dictionnaire Python
    # Afficher l'arbre de classes
    create_tree_from_dict(json_dict_from_file())



# Code principal
if __name__ == '__main__':
    # Appeler la fonction principale
    main()
