# Auteur : Olivier Brunet - 15/02/2019
# OpenClassRoom - MOOC - Découvrez les librairies Python pour la Data Science
# Partie 2 - Activité - Simulez le problème de Monty Hall avec Numpy

from enum import Enum
import numpy as np


class Strategie(Enum):
    "Définition d'une sous-classe de Enum, qui contiendra les stratégies possibles."
    CHANGER = 1
    GARDER = 2


def play_several_games(strategie, nb_tours):
    """Fonction simulant 'nb_tours' parties du jeu Monty Hall. 
    Renvoie un tableau de résultats constitués de booléens.
    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours  
    Returns:
        tableau_resultats: tableau de booléens -> True: victoire à une partie, sinon False
    """
 
    # génération un tableau, 1 elt = les 3 portes, nb d'élts = 'nb_tours' parties 
    portes = np.array([[0, 1, 2]] * nb_tours)

    # génère aléatoirement les bonnes portes pour 'nb_tours' parties
    bonnes_portes = np.random.randint(0, 3, nb_tours).reshape(nb_tours, 1)  
    # reshape permet d'avoir un tableau vertical pour manipuler les éléments par la suite
    
    # génère aléatoirement les 1ers choix du joueur pour 'nb_tours' parties
    premiers_choix = np.random.randint(0, 3, nb_tours).reshape(nb_tours, 1) 

    # on retire les 1ers choix pour obtenir les portes restantes pouvant être choisies
    portes = portes[portes != premiers_choix].reshape(nb_tours, 2)
    
    if strategie == Strategie.GARDER:  
        # le présentateur retire une 2ème porte - finalement quelque soit la porte retirée, le joueur reste sur son choix donc:
        tableau_resultats = (premiers_choix == bonnes_portes).flatten()     # flatten: réduit à 1 dim
    
    elif strategie == Strategie.CHANGER:     
        # le présentateur retire une 2ème porte qui n'est pas la bonne porte (sauf si la bonne porte est le 1er choix)
        # au final, le résultat dépend de la présence / du nombre de bonnes portes parmi les 2 restantes
        p1 = portes[:,0].reshape(nb_tours, 1) == bonnes_portes          # 1ères bonnes portes restantes i.e dans la 1ère colonne
        p2 = portes[:,1].reshape(nb_tours, 1) == bonnes_portes          # 2èmes bonnes portes restantes i.e dans la 2ème colonne
        tableau_resultats = np.logical_or(p1, p2).flatten()             # union des tableaux

    else:
        raise ValueError("Stratégie ne faisant pas partie des choix possibles !")

    return tableau_resultats