def deterministe(auto):
    """
    >>> auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3], "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    >>> auto2={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    >>> print(deterministe(auto0))
    True
    >>> print(deterministe(auto2))
    False
    """

    # un auto est dét si 

    # il a 1 seul état inial 
    if len(auto["I"]) != 1:
        return False
    
    # et si pour tout état q 
    # il y a au plus une transition
    # vers p etiqueté a
    for q in auto["etats"]:
        
        # pour chaque état q on prend tout les transition partant de q avec filter
        # aver map on remplace les transistion pat les etiquette 
        # si il y'a des doublons alors l'auto n'est pas det
        etiquettes = list(map(lambda transistion: transistion[1], filter(lambda transition: transition[0] == q, auto['transitions']))) 
        
        # pour voir les doublons
        if len(etiquettes) != len(set(etiquettes)):
            return False
    
    return True


def determinise(auto):
    """
    >>> auto2={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}   
    >>> print(determinise(auto2))
    {'alphabet': ['a', 'b'], 'I': [[0]], 'transitions': [[[0], 'a', [0, 1]], [[0, 1], 'a', [0, 1]], [[0, 1], 'b', [1]], [[1], 'a', [1]], [[1], 'b', [1]]], 'etats': [[0], [0, 1], [1]], 'F': [[0, 1], [1]]}
    """
    
    # si l'auto est déja det 
    if deterministe(auto):
        return auto
    
    # I est la liste des états initiaux 
    auto["I"] = [auto["I"]]

    # les transitions 
    #     
    



if __name__ == "__main__":


    import doctest

    doctest.testmod(verbose=1)
    
    
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3], "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}

    auto1 ={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    
    auto2={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}   
