
#Toutes les fonctions ont été vérifiées
#Définition de la fonction pref qui reçoit un mot et retourne tous ses prefixes
def pref(mot) : 
    """
    >>> print(pref("coucou"))
    ['', 'c', 'co', 'cou', 'couc', 'couco', 'coucou']
    """
    #On initialise la liste qui va contenir les prefixes
    lst=[]
    #Pour obtenir tous les prefixes, on va parcourir la longueur de la liste pour obtenir chaque bout
    for i in range(len(mot)+1) :
        #On ajoute le prefixe trouvé à la liste
        lst.append(mot[:i])
    return lst

def suf (mot) : 
    """
    >>> print(suf("coucou"))
    ['coucou', 'oucou', 'ucou', 'cou', 'ou', 'u', '']
    """
    #On initialise la liste qui va contenir les suffixes de mot 
    lstsuf=[]
    #On stocke la longueur de mot
    l=len(mot)
    #On parcourt la longueur pour diminuer graduellement l'indice de début
    for i in range(l+1) : 
        lstsuf.append(mot[i:l])
    return lstsuf


def fact (mot) :
    """
    >>> print(fact("coucou"))
    ['', 'c', 'co', 'cou', 'couc', 'couco', 'coucou', 'o', 'ou', 'ouc', 'ouco', 'oucou', 'u', 'uc', 'uco', 'ucou']
    """
    #Va renvoyer l'ensemble des facteurs de mot
    lstfact=[]
    #On stocke la longueur du mot
    l=len(mot)
    #On parcourt la longueur du mot pour l'indice du début du facteur 
    for i in range(l+1) : 
        #Pour l'indice de la fin du facteur
        for j in range(i, l+1) :
            if mot[i:j] not in lstfact :
                lstfact.append(mot[i:j])
    return lstfact

def miroir(mot):
    """
    >>> print(miroir("coucou"))
    uocuoc
    """
    return mot[::-1]

if __name__=='__main__' : 
    import doctest
    
    doctest.testmod(verbose=1)
