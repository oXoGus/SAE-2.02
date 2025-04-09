
def emonde (auto) :
    #Par définition, un automate est émondé uniquement s'il est accessible et coaccessible
    return accessible(auto) and coaccessible(auto)


def accessible(auto) :
    lst=[]
    #On va parcourir tous les états et vérifier s'ils sont accessible depuis l'état initial
    for transition in auto['transitions']:
        #print(transition[0], auto['I'], transition[0] in auto['I'] and transition[2] not in lst, transition[0] in lst )
        if transition[0] in auto['I'] :
            if transition[0] not in lst : 
                lst.append(transition[0])
            if transition[2] not in lst : 
                lst.append(transition[2])
        #Si l'état n'est pas directement accessible par l'état initial mais par un etat qui lui l'est 
        elif transition[0] not in auto['I'] and transition[0] in lst and transition[2] not in lst:
            lst.append(transition[2])
    #Si la liste des états est identique à celle de l'ensemble des états de l'automate, alors il est bien accessible
    #print(lst, auto["etats"])
    if lst==auto['etats'] : 
        return True
    return False
            


def coaccessible (auto):
    lst=[]
    for i in range(len(auto["transitions"])-1, -1, -1): 
        transition=auto['transitions'][i]
        #Si l'état d'arrivée de la transition est l'état final, on ajoute à la liste des états coaccessibles
        if transition[2] in auto['F'] :
            if transition[0] not in lst :
                lst.append(transition[0])
            if transition[2] not in lst : 
                lst.append(transition[2])
        
        #Si l'état d'arrivée n'est pas l'état final, mais que l'état d'arrivée est un état coaccessible, alors on l'ajoute a la liste des états coaccessibles
        if transition[2] not in auto['F'] and transition[0] not in lst and transition[2] in lst:
            lst.append(transition[0])
    #Si tous les états de l'automate se trouve dans la liste des états coaccessibles de l'automate, alors on retourne True 
    #print(lst, auto["etats"])
    if set(lst)==set(auto['etats']):
        return True
    return False
        
            

def prefixe (auto) : 
    #On vérifie que l'automate est emonde sinon on ne retourne rien
    if emonde(auto)==False:
        return None
    
    #On crée l'automate ou on va uniquement changer les états finaux ou on va attribuer l'ensemble des états de l'automate afin de pouvoir finir a chaque état pour obtenir les préfixes
    PrefAuto={
        "etats" : auto["etats"].copy(),
        "transitions" : auto["transitions"].copy(),
        "I" : auto["I"].copy(),
        "alphabet" : auto["alphabet"].copy(),
        "F" : auto["etats"].copy()
    }
    
    return PrefAuto

def suffixe (auto) : 
    #On vérifie que l'automate soit bien émondé 
    if emonde(auto)==False :
        return None
    #On crée le nouvel automate ou on va uniquement modifier les états initiaux où on va attribuer l'ensemble des états de l'automate
    SuffAuto = {
        "etats" : auto["etats"].copy(),
        "transitions" : auto["transitions"].copy(),
        "I": auto["etats"].copy(),
        "alphabet" : auto["alphabet"].copy(),
        "F" : auto["F"].copy()
    }
    return SuffAuto

def facteur (auto) :
    #Pour un automate qui accepte le facteur, il faut d'abord qu'il soit émondé 
    if emonde(auto)==False:
        return None
    #On retourne ensuite le suffixe du préfixe de l'automate car ainsi on rend avec prefixe tous les états en états finaux et tous les états en état initial avec suffixe
    return suffixe(prefixe(auto))

def miroir (auto) : 
    #On vérifie que l'automate est bien émondé 
    if emonde(auto)==False:
        return None
    #On crée le nouvel automate 
    MiroirAuto = {
        #On attribue tous les états
        "etats" : auto["etats"].copy(),
        #Le même alphabet
        "alphabet": auto["alphabet"].copy(),
        #On inverse les états initaux et les états finaux 
        "I" : auto["F"].copy(),
        "F" : auto["I"].copy(),
        #On crée la clé qui correspond a la liste de transitions  
        "transitions" : []
    }
    for transition in auto['transitions'] : 
        #On inverse le sens des transitions en inversant uniquement les deux états de la transition
        MiroirAuto["transitions"].append((transition[2], transition[1], transition[0]))
    return MiroirAuto


if __name__ == '__main__' :
    auto={
        'etats' : [1, 2, 3, 4, 5, 6, 7],
        'transitions' : [(1, 'c', 2), (2, 'o', 3), (3, 'u', 4), (4, 'c', 5), (5, 'o', 6), (6, 'u', 7)],
        'I' : [1],
        'F' : [7],
        'alphabet' : ['c', 'o', 'u']
    }

    print(accessible(auto))
    print(coaccessible(auto))
    print(prefixe(auto))
    print(suffixe(auto))
    print(facteur(auto))
    print(miroir(auto))