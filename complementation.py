from determinisation import *

def complet(auto) : 
    """ 
    >>> auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3], "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    >>> auto1 ={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    >>> print(complet(auto0))
    False
    >>> print(complet(auto1))
    True
    """
    
    #On vérifie dans un premier temps avec un map que tous les états de la liste des etats apparaissent dans la transition
    #On fait ensuite une boucle for dans laquelle on vérifie grâce à un filter que chaque lettre contienne tout l'alphabet
    #S'ils ne sont pas tous dans l'alphabet, alors on s'arrête la et on return false, sinon on continue et à le fin on return true
    if all(list(map(lambda x, y: x==y, auto["transitions"][0], auto["etats"]))) : 
        return False 
    #Pour chaque etat 
    for etat in auto["etats"] : 
        #Liste contenant les lettres des transitions de l'etat 
        lst=[]
        for transit in auto['transitions'] :
            if transit[0]==etat and transit[1] not in lst: 
                lst.append(transit[1])

        # on utilise les set pour que l'orde des étiquettes n'importe pas
        if set(lst)!=set(auto['alphabet']):
            return False 
    return True


def complete (auto) :

    """
    >>> auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3], "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    >>> complete(auto0) == {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4], 'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3], [0, 'b', 4], [2, 'b', 4], [3, 'a', 4], [3, 'b', 4], [4, 'a', 4], [4, 'b', 4]], 'I': [0], 'F': [3]}
    True
    """


    #Complète un automate rentré en paramètre
    #auto==> l'automate, prend la forme d'un dictionnaire, contenant les clés 'etats', 'transitions', 'alphabet', 'I', 'F' 
    
    if complet(auto) : 
        return auto
    
    # l'état puis est l'état le plus grand + 1
    puits = max(auto["etats"]) + 1

    auto['etats'].append(puits)
    #Pour chaque état 
    for etat in auto['etats'] : 
        #Liste des lettres dont il faudra rajouter les transitions pour completer
        lst=[]
        #On ajoute les étiquettes qu'on trouve sur les transitions de l'état
        for transit in auto['transitions'] :
            if transit[0]==etat and transit[1] not in lst: 
                lst.append(transit[1])
        
        #Si il faut rajouter des transition vers le puits
        if set(lst)!=set(auto['alphabet']):
            for lettre in auto['alphabet'] :
                if lettre not in lst : 
                    auto['transitions'].append([etat, lettre, puits])
    return auto

def complement (auto) :
    """
    >>> auto3 = {"alphabet":['a','b'],"etats": [0,1,2,], "transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}
    >>> complement(auto3) == {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3], 'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'b', 2], [0, 'b', 3], [2, 'a', 3], [3, 'a', 3], [3, 'b', 3]], 'I': [0], 'F': [0, 1, 3]}
    True
    """
    # on recréer un nouvel auto pour ne pas modifier celui donné en param
    detAuto=determinise(auto)
    detAuto=complete(detAuto)
    compAuto=dict()
    compAuto['alphabet']=detAuto['alphabet'].copy()
    compAuto['etats']=detAuto['etats'].copy()
    compAuto['transitions']=detAuto["transitions"].copy()
    compAuto['I']=detAuto['I'].copy()
    lst=[]

    # les états non terminaux le devienent 
    # et les états terminaux devienent non terminaux
    for etat in detAuto['etats'] : 
        if etat not in detAuto['F']:
            lst.append(etat)
    compAuto['F']=lst
    return compAuto


if __name__ == '__main__' : 

    #Automates de test
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],
"transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    auto1 ={"alphabet":['a','b'],"etats": [0,1],
"transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto3 ={"alphabet":['a','b'],"etats": [0,1,2],
    "transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

    import doctest
    
    doctest.testmod(verbose=1)