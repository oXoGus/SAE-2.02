#Toutes les fonctions ont été vérifiées 

def defauto () : 
    #cette fonction permet la saisie d'un automate sans créer de doublon
    #Pour saisir un automate, on doit avoir le quintuplet suivant : (Q, A, E, I, F)
    
    #On va d'abord s'occuper de l'ensemble fini d'états Q 

    lstQ = []

    entree=""
    while entree!="stop" :
        entree=input("Entrez vos états")
        if entree!="stop" :
            lstQ.append(entree)
    
    #Ensuite on s'occupe de l'ensemble des états initiaux
    lstI =[]
    initial=""
    while initial!="stop" :
        initial=input("Entrez vos états initiaux")
        if initial!="stop":
            if initial not in lstQ : 
                print("Non valide")
                continue
            lstI.append(initial)
    
    #Ensuite on s'occupe des états finaux 
    lstF=[]
    final=""
    while final!="stop" :
        final=input("Entrez vos états finaux")
        if final!=stop : 
            if final not in lstQ :
                print("Non valide")
                continue
            lstF.append(final)
    
    #Il nous reste l'alphabet et l'ensemble des transitions

    #On fait d'abord l'alphabet 

    #Liste qui va accueuillir les éléments de l'alphabet
    lstA=[]
    lettre=""

    while lettre!="stop" : 
        lettre=input("Entrez les lettres de votre alphabet")
        if lettre!="stop" :
            lstA.append(lettre)
    
    #On a l'alphabet maintenant on va faire l'ensemble de transitions

    lstE=[]
    
    #Les transitions vont prendre la forme d'un (état, lettre, état)
    #On pourrait faire toutes les transitions possible, mais il serait tout de même plus simple de demander les transitions une à une à l'utilisateur parce que sinon on risque d'avoir des transitions qui n'existent pas dans notre automate

    transition=""
    while transition!="stop": 
        transition=input("Entrez la transition sous le format:Q a P")
        if transition!="stop" : 
            l=transition.split(" ")
            #Si l'argument n'a pas le bon nombre d'argument ou le mauvais format
            if len(l)!=3 : 
                print("Nombre d'argument invalide")
                continue
            #Si les arguments entrés ne font pas partis des états et de l'alphabet entré
            if l[0] not in lstQ : 
                print("Etat ", l[0], " invalide")
                continue
            if l[1] not in lstA : 
                print("Lettre ", l[1], " invalide")
                continue
            if l[2] not in lstQ : 
                print("Etat ", l[2], " invalide ")
                continue
            lstE.append((l[0], l[1], l[2]))

    
    return {"etats" : lstQ, "alphabet" :lstA, "transitions" :lstE, "I" :lstI, "F" : lstF}


def lirelettre(lstE, lstQ, a) :
    #A quoi ça sert d'avoir la liste des états si on a déjà la liste des transitions qui contiennent déjà les états
    etatArrivee=[]
    for transition in lstE : 
        if transition[1]==a and transition[2] not in etatArrivee and transition[0] in lstQ:
            etatArrivee.append(transition[2])
    return etatArrivee

#Fonction vérifiées jusqu'ici

def liremot (lstE, lstI, mot) : 
    """ Cette fonction renvoit les états finaux dans lesquels on peut arriver en lisant un mot et en partant d'une liste d'états avec les transitions du graphe
    lstE ==> liste de transitions du graphe
    lstI ==> liste des états desquels on part pour lire le mot, soit les états initiaux
    mot ==> le mot qu'on souhaite lire"""
    #On commence par partir depuis un état initial 
    #La fonction lirelettre va lire les lettres en partant de l'état initial,
    etatArr=lstI
    #On va chercher a lire la première lettre en partant 
    for lettre in mot : 
        #on va partir des états précédents pour lire la lettre et les états finaux deviendront les prochains états initiaux
        etatArr=lirelettre(lstE, etatArr, lettre)
    return etatArr

def accepte (auto, mot) :
    etatsArr=liremot(auto["transitions"], auto["I"], mot)
    #print(etatsArr, auto["F"])
    if len(etatsArr)>0 and etatsArr == auto["F"]: 
        return True 
    return False


def langage_accept (automate, n) :
    acceptes=[]
    for i in range(n+1) : 
        langage=puis(automate["alphabet"], i)
        for mot in langage : 
            if accepte(automate, mot) :
                acceptes.append(mot)
    return acceptes


#1.3.6 On ne peut pas faire une fonction qui renvoie le langage accepté par un automate car celui-ci peut être infini, notamment le langage L* pour lequel on ne peut pas faire de fonction


if __name__ == '__main__' :

    from langages import puis 

    auto ={"alphabet":['a','b'],"etats": [1,2,3,4], 
    "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]],
    "I":[1],"F":[4]}

    print(langage_accept(auto, 3))
