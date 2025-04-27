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
    if len(auto['I']) != 1:
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


def marquer(etatsActif : list, auto, autoDet):
    """
    prend un état 
    un auto non déterministe
    et un auto déterministe
    
    on teste tout tes transistions de l'état actif
    on regroupe tout les transi partant de etatActif

    revoit tout les état où va les transitions
    pour append les états non marqué
    pas besoin de prendre l'auto determiste modif puisque c'est les modif 
    seront accessibles dans la fonc determise
    """

    # liste des états trouvé 
    etatsTrouve = list()

    # toutes les transi partant de l'état actif

    # liste de toutes les transi partant des états dans etatsActif
    transi = list()

    # pour chaque etat 
    for etat in etatsActif:
        transi.extend(list(filter(lambda transi : transi[0] == etat, auto['transitions'])))
    

    # pour chaque lettre de l'alphabet
    for a in auto['alphabet']:
        
        # liste des états qui sont 'pointé' par les transition d'étiquette a
        etatsPointe = list(set(map(lambda transi: transi[2], filter(lambda transi: transi[1] == a, transi))))

        # si il y a une ou plusieurs transi d'étiquette a
        if len(etatsPointe) > 0:

            # on ajoute la transition de etatsActif d'étiquette a et d'état pointé etatsPointe
            autoDet['transitions'].append([etatsActif, a, etatsPointe])

            if etatsPointe not in etatsTrouve:
                etatsTrouve.append(etatsPointe)

    
    # on marque l'état en le mettant dans les états de l'auto det
    autoDet['etats'].append(etatsActif)

    # on ajoute l'état dans F si il contient un état F de l'auto original
    
    # si l'intersection n'est pas vide
    if set(etatsActif).intersection(set(auto['F'])) != set(): 
        autoDet['F'].append(etatsActif)

    # on renvoit les état touvé pour les mettre dans étatsNonMarqué
    return etatsTrouve



def determinise(auto):
    """
    >>> auto2={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}   
    >>> determinise(auto2) == renommage({'alphabet': ['a', 'b'], 'I': [[0]], 'transitions': [[[0], 'a', [0, 1]], [[0, 1], 'a', [0, 1]], [[0, 1], 'b', [1]], [[1], 'a', [1]], [[1], 'b', [1]]], 'etats': [[0], [0, 1], [1]], 'F': [[0, 1], [1]]})
    True
    """
    
    # si l'auto est déja det 
    if deterministe(auto):
        return auto
    
    # on recréer un auto det
    autoDet = {
        'alphabet': auto['alphabet'],
        'I': [],
        'etats': [],
        'transitions': [],
        'F': []
    }

    # I est la liste des états initiaux 
    autoDet["I"] = [auto["I"]]

    # on part de l'état initial (la liste contenance tout les états initiaux)
    # l'état actif est l'état d'où part les transitions
    etatActif =  autoDet["I"][0]

    # on met l'état actif dans la liste des états non marqué
    # puisqu'on a pas encore test toute ces transitions
    
    # un état est marqué quand on a fait toutes ces transition possible

    etatsNonMarque = [etatActif]

    etatsMarque = []

    # tant qu'il reste des états non marqué
    while len(etatsNonMarque) > 0:

        # on marque l'état actif
        # en verifiant tout ces transistions possibles

        etatsTrouve = marquer(etatsNonMarque[0], auto, autoDet)
        
        # marque l'état marqué 
        etatsMarque.append(etatsNonMarque[0])

        # pour chaque état trouvé on l'ajoute dans les états non marqué 
        for e in etatsTrouve:
            if e not in etatsNonMarque and e not in etatsMarque:
                etatsNonMarque.append(e)
        
        # on retire l'état marqué des étatsNonMarqué
        etatsNonMarque.pop(0)
        
        
    
    return renommage(autoDet)



def renommage(auto):
    
    # on utilise un dict en tant que table de correspondance
    # sous la forme
    # [ancient nom] : nouveau nom 

    newName = dict()

    for i, etat in enumerate(auto['etats']):
        newName[tuple(etat)] = i
    
    auto['etats'] = [i for i in range(len(auto['etats']))]

    # on modif les transi avec la table de correspondance newName
    
    # on la recontruit de 0
    nTransiLst = list()

    for transi in auto['transitions']:
        nTransiLst.append([newName[tuple(transi[0])], transi[1], newName[tuple(transi[2])]])
    auto['transitions'] = nTransiLst

    # meme chose pour I 
    auto['I'] = [newName[tuple(etatInit)] for etatInit in auto['I']]

    # meme chose pour F
    auto['F'] = [newName[tuple(etatFin)] for etatFin in auto['F']]

    return auto
        
if __name__ == "__main__":


    import doctest

    from genAuto import genAuto

    doctest.testmod(verbose=1)
    
    
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3], "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}

    auto1 ={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    
    auto2={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}   

    #print(determinise(auto2))

    #print(renommage(determinise(auto2)))

    #print(deterministe(determinise(genAuto())))