from langages import puis

def defauto () : 
    #cette fonction permet la saisie d'un automate sans créer de doublon
    #Pour saisir un automate, on doit avoir le quintuplet suivant : (Q, A, E, I, F)
    
    #On va d'abord s'occuper de l'ensemble fini d'états Q 

    # supprime les doublons
    Q = set()

    entree=""
    while entree!="stop" :
        entree=input("Entrez vos états : ")
        if entree!="stop" :
            Q.add(entree)
    

    #Ensuite on s'occupe de l'ensemble des états initiaux
    I = set()
    initial=""
    while initial!="stop" :
        initial=input("Entrez vos états initiaux : ")
        if initial!="stop":
            if initial not in Q : 
                print("cet état n'existe pas ")
                continue
            I.add(initial)
    
    #Ensuite on s'occupe des états finaux 
    F=set()
    final=""
    while final!="stop" :
        final=input("Entrez vos états finaux : ")
        if final!="stop" : 
            if final not in Q :
                print("cet état n'existe pas ")
                continue
            F.add(final)
    
    #Il nous reste l'alphabet et l'ensemble des transitions

    #On fait d'abord l'alphabet 

    # les éléments de l'alphabet
    A=set()
    lettre=""

    while lettre!="stop" : 
        lettre=input("Entrez les lettres de votre alphabet : ")
        if lettre!="stop" :
            A.add(lettre)
    
    #On a l'alphabet maintenant on va faire l'ensemble de transitions

    E=set()
    
    #Les transitions vont prendre la forme d'un (état, lettre, état)
    #On pourrait faire toutes les transitions possible, mais il serait tout de même plus simple de demander les transitions une à une à l'utilisateur parce que sinon on risque d'avoir des transitions qui n'existent pas dans notre automate

    transition=""
    while transition!="stop": 
        transition=input("Entrez la transition sous le format Q a P : ")
        if transition!="stop" : 
            l=transition.split(" ")
            #Si l'argument n'a pas le bon nombre d'argument ou le mauvais format
            if len(l)!=3 : 
                print("Nombre d'argument invalide")
                continue
            #Si les arguments entrés ne font pas partis des états et de l'alphabet entré
            if l[0] not in Q : 
                print("Etat ", l[0], " invalide")
                continue
            if l[1] not in A : 
                print("Lettre ", l[1], " invalide")
                continue
            if l[2] not in Q : 
                print("Etat ", l[2], " invalide ")
                continue
            E.add((l[0], l[1], l[2]))

    
    return {"etats" : list(Q), "alphabet" :list(A), "transitions" :list(E), "I" :list(I), "F" : list(F)}


def lirelettre(E, Q, a) :
    """
    >>> auto ={"alphabet":['a','b'],"etats": [1,2,3,4], "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]], "I":[1],"F":[4]}
    >>> print(lirelettre(auto["transitions"],auto["etats"],'a'))
    [2, 4]
    """
    etatArrivee=set()
    for transition in E : 
        if transition[1]==a and transition[0] in Q:
            etatArrivee.add(transition[2])
    return list(etatArrivee)


def liremot (T, E, m) : 
    """
    >>> auto ={"alphabet":['a','b'],"etats": [1,2,3,4], "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]], "I":[1],"F":[4]}
    >>> print(liremot(auto["transitions"],auto["etats"],'aba'))
    [4]
    """
    #Cette fonction renvoit les états finaux dans lesquels on peut arriver en lisant un mot et en partant d'une liste d'états avec les transitions du graphe
    #E ==> liste de transitions du graphe
    #I ==> liste des états desquels on part pour lire le mot, soit les états initiaux
    #mot ==> le mot qu'on souhaite lire
    
    #On commence par partir depuis un état initial 
    #La fonction lirelettre va lire les lettres en partant de E,
    etatArr=E
    #On va chercher a lire la première lettre en partant 
    for lettre in m : 
        #on va partir des états précédents pour lire la lettre et les états finaux deviendront les prochains états initiaux
        etatArr=lirelettre(T, etatArr, lettre)
        #print(etatArr)
    return etatArr

def accepte (auto, m) :
    """
    >>> auto ={"alphabet":['a','b'],"etats": [1,2,3,4], "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]], "I":[1],"F":[4]}
    >>> print(accepte(auto,'aba'))
    True
    """
    etatsArr=liremot(auto["transitions"], auto["I"], m)

    if len(etatsArr)>0 and set(etatsArr).intersection(set(auto["F"])) != set(): 
        return True 
    return False


def langage_accept (auto, n) :
    """
    >>> auto ={"alphabet":['a','b'],"etats": [1,2,3,4], "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]], "I":[1],"F":[4]}
    >>> print(langage_accept(auto, 3))
    ['aba']
    """
    acceptes=set()
    for i in range(n+1) : 
        langage=puis(auto["alphabet"], i)
        for mot in langage : 
            if accepte(auto, mot) :
                acceptes.add(mot)
    return list(acceptes)


#1.3.6 On ne peut pas faire une fonction qui renvoie le langage accepté par un automate car celui-ci peut être infini, 
# notamment le langage A* pour lequel on ne peut pas faire de fonction


if __name__ == '__main__' :

    import doctest


    doctest.testmod(verbose=1)

    auto ={"alphabet":['a','b'],"etats": [1,2,3,4], "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]], "I":[1],"F":[4]}
    auto = defauto()
    print(auto)
    #print(accepte(auto,'aba'))
    #liremot(auto["transitions"], auto["I"], "aba")