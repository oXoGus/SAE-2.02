
#Toutes les fonctions ont été vérifiées
#Définition de la fonction pref qui reçoit un mot et retourne tous ses prefixes
def pref(mot) : 
    #On initialise la liste qui va contenir les prefixes
    lst=[]
    #Pour obtenir tous les prefixes, on va parcourir la longueur de la liste pour obtenir chaque bout
    for i in range(len(mot)+1) :
        #On ajoute le prefixe trouvé à la liste
        lst.append(mot[:i])
    return lst

def suf (mot) : 
    #On initialise la liste qui va contenir les suffixes de mot 
    lstsuf=[]
    #On stocke la longueur de mot
    l=len(mot)
    #On parcourt la longueur pour diminuer graduellement l'indice de début
    for i in range(l+1) : 
        lstsuf.append(mot[i:l])
    return lstsuf


def fact (mot) :
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
    #retourne le miroir de mot
    miror=""
    #On parcourt dans le sens inverse le mot caractère par caractère
    for i in range(len(mot)-1, -1, -1):
        #On ajoute chaque caractère au mot miror qui stocke le miroir
        miror+=mot[i]
    return miror

if __name__=='__main__' : 
    print(pref("coucou"))
    print(suf("coucou"))
    print(fact("coucou"))
    print(miroir("coucou"))
