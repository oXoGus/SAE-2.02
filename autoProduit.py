from determinisation import * 
from complementation import *

def autoProd(auto1, auto2):


    # on créé l'auto produit
    autoProd = {

        # on part du principe que les deux auto 
        # on le même alphabet
        'alphabet': auto1['alphabet'],
        'I': [],
        'etats': [],
        'transitions': [],
        'F': []
    }

    etatActif = (auto1['I'][0], auto2['I'][0])

    # état initial 
    autoProd['I'] = [etatActif]

    # on marque l'état acitf 
    marquerProdRec(auto1, auto2, autoProd, etatActif)

    # la magie de la récusivité 

    # on le renome pas pour avoir les paire pour inter et difference
    return autoProd



def marquerProdRec(auto1, auto2, autoProd, etatActif):
    """
    fonction comme la la fonction marquer pour l'algo déterminise
    mais de manière recursive
    
    """
    # on marque l'état actif
    autoProd['etats'].append(etatActif)

    # comme l'automate est complet et dét
    # on utilise la fonction de transition sur toutes les lettres
    for a in autoProd['alphabet']:
        
        # l'état trouvé pour l'etiquette a
        etatTrouve = (point(auto1, etatActif[0], a), point(auto2, etatActif[1], a))

        # si il n'y pas d'état trouvé pour un des deux états 
        # on passe a la lettre suivante
        if None in etatTrouve:
            continue
        
        # on ajoute la transtion
        autoProd['transitions'].append([etatActif, a, etatTrouve])

        # si on l'a pas déja testé
        if etatTrouve not in autoProd['etats']:
            
            # on le marque en faisant un appel recusif
            marquerProdRec(auto1, auto2, autoProd, etatTrouve)
            


def point(auto, etat, etiquette):
    """
    fonction de transition d'un automate déterministe
    """
    # renvoie l'état atteint par la transition de l'état etat et d'étiquette etiquette
    etats =  list(map(lambda transi: transi[2], filter(lambda transi: transi[0] == etat and transi[1] == etiquette, auto['transitions'])))
    
    # si l'auto n'est pas complet
    if etats == []:
        return None
    return etats[0]


def inter(auto1, auto2):
    """
    >>> auto4 ={"alphabet":['a','b'],"etats": [0,1,2], "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}
    >>> auto5 ={"alphabet":['a','b'],"etats": [0,1,2], "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]], "I":[0],"F":[0,1]}
    >>> inter(auto4, auto5) == renommage({'alphabet': ['a', 'b'], 'I': [(0, 0)], 'transitions': [[(0, 0), 'a', (1, 0)],[(1, 0), 'b', (2, 1)], [(2, 1), 'a', (2, 1)], [(2, 1), 'b', (2, 2)],[(2, 2), 'a', (2, 2)], [(2, 2), 'b', (2, 0)], [(2, 0), 'a', (2, 0)],[(2, 0), 'b', (2, 1)]],'etats': [(0, 0), (1, 0), (2, 1), (2, 2), (2, 0)], 'F': [(2, 0), (2, 1)]})
    True
    """
    
    # on déterminise les deux auto
    auto1 = determinise(auto1)
    auto2 = determinise(auto2)

    # on fait l'automate produit 
    auto = autoProd(auto1, auto2)

    # on met dans F les et etats (F1, F2)
    auto['F'] = list(filter(lambda etats: etats[0] in auto1['F'] and etats[1] in auto2['F'], auto['etats']))
    
    # pour que le auto['F] est = à celui dans l'exemple 
    auto['F'] = sorted(auto['F'], key=lambda etats: etats[1]) 
    
    return renommage(auto)

def difference(auto1, auto2):
    """
    >>> auto4 ={"alphabet":['a','b'],"etats": [0,1,2], "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]} 
    >>> auto5 ={"alphabet":['a','b'],"etats": [0,1,2], "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]], "I":[0],"F":[0,1]}
    >>> toSet(difference(auto4,auto5)) == toSet({'alphabet': ['a', 'b'], 'I': [(0, 0)], 'transitions': [[(0, 0), 'a', (1, 0)], [(0, 0), 'b', (3, 1)], [(3, 1), 'a', (3, 1)], [(3, 1), 'b', (3, 2)], [(3, 2), 'a', (3, 2)], [(3, 2), 'b', (3, 0)], [(3, 0), 'a', (3, 0)], [(3, 0), 'b',(3, 1)], [(1, 0), 'a', (3, 0)], [(1, 0), 'b', (2, 1)], [(2, 1), 'a', (2, 1)], [(2, 1), 'b', (2, 2)], [(2, 2), 'a', (2, 2)], [(2, 2), 'b', (2, 0)], [(2, 0), 'a', (2, 0)], [(2, 0), 'b', (2, 1)]], 'etats': [(0, 0), (3, 1), (3, 2), (3, 0), (1, 0), (2, 1), (2, 2), (2, 0)], 'F': [(2, 2)]})
    True
    """
    # on déterminise les deux auto
    auto1 = determinise(auto1)
    auto2 = determinise(auto2)

    # on les completes aussi
    auto1 = complete(auto1)
    auto2 = complete(auto2)
    
    # on fait l'automate produit 
    auto = autoProd(auto1, auto2)

    # on met dans F les et etats (F1, not F2)
    auto['F'] = list(filter(lambda etats: etats[0] in auto1['F'] and etats[1] not in auto2['F'], auto['etats']))

    return auto


def toSet(auto):
    """
    transforme tout les listes en set pour que 
    l'ordre des élément ne rendent pas a comparaison des deux auto faux
    """
    # marche que sur un automate déja renomé (pas de liste de liste)
    auto['alphabet'] = set(auto['alphabet'])
    auto['I'] = set(auto['I'])
    auto['F'] = set(auto['F'])
    auto['transitions'] = set(map(lambda transi: tuple(transi), auto['transitions']))
    auto['etats'] = set(auto['etats'])
    return auto



if __name__ == "__main__":

    from genAuto import genAuto

    auto4 ={"alphabet":['a','b'],"etats": [0,1,2], "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}

    auto5 ={"alphabet":['a','b'],"etats": [0,1,2], "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]], "I":[0],"F":[0,1]}

    diff = difference(auto4, auto5)
    
    test = {'alphabet': ['a', 'b'], 'I': [(0, 0)], 'transitions': [[(0, 0), 'a', (1, 0)], [(0, 0), 'b', (3, 1)], [(3, 1), 'a', (3, 1)], [(3, 1), 'b', (3, 2)], [(3, 2), 'a', (3, 2)], [(3, 2), 'b', (3, 0)], [(3, 0), 'a', (3, 0)], [(3, 0), 'b',(3, 1)], [(1, 0), 'a', (3, 0)], [(1, 0), 'b', (2, 1)], [(2, 1), 'a', (2, 1)], [(2, 1), 'b', (2, 2)], [(2, 2), 'a', (2, 2)], [(2, 2), 'b', (2, 0)], [(2, 0), 'a', (2, 0)], [(2, 0), 'b', (2, 1)]], 'etats': [(0, 0), (3, 1), (3, 2), (3, 0), (1, 0), (2, 1), (2, 2), (2, 0)], 'F': [(2, 2)]}
    #print(set(map(lambda transi: tuple(transi), test['transitions'])) == set(map(lambda transi: tuple(transi), diff['transitions'])))
    #print(set(test['etats']) == set(diff['etats']))
    import doctest
    
    doctest.testmod(verbose=1)