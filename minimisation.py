from determinisation import *
from complementation import *
from autoProduit import point
import copy




def minimise(auto):
    
    # on déterminise et complete l'automate 
    auto = determinise(auto)
    # auto = complement(auto)

    # on calcules les classes de cet auto
    classes = equivalenceDeNerode(auto)
    
    # on reconstruit un nouvel auto avec ces classes
    nAuto = dict()
    nAuto['alphabet'] = auto['alphabet']
    nAuto['etats'] = classes
    
    # les état qui ont un état initial 
    # dans l'auto non minimisé

    nAuto['I'] = list()
    for etatInit in auto['I']:
        for etat in nAuto['etats']:

            # pas de doublons
            if etatInit in etat and etat not in nAuto['I']:
                nAuto['I'].append(etat)

    # meme chose pour les états terminaux
    nAuto['F'] = list()
    for etatInit in auto['F']:
        for etat in nAuto['etats']:

            # pas de doublons
            if etatInit in etat and etat not in nAuto['F']:
                nAuto['F'].append(etat)

    # les transitions 
    nAuto['transitions'] = list()

    # on part de l'unique état inital
    etat = nAuto['I'][0]

    for etat in nAuto['etats']:
        for a in nAuto['alphabet']:
            nAuto['transitions'].append([etat, a, pointMinim(auto, etat, a, nAuto)])

    return nAuto
        

def pointMinim(auto, etat, etiquette, nAuto):

    # on prend le premier état de etat
    # cela reient au meme grace a l'équivalence de Nérode
    etat = etat[0]

    # on prend la classe de l'état pointé par l'étiquette
    etatPointe = point(auto, etat, etiquette)

    for etat in nAuto['etats']:
        if etatPointe in etat:
            return etat


def equivalenceDeNerode(auto):
    """calcule des classe d'équivalance d'un automate"""

    # classes initales
    # liste contenant la liste de tout les états terminaux
    prevClasses = [[etat for etat in auto['etats'] if etat in auto['F']]]
    
    print(prevClasses, auto)
    # et tout les états non terminaux
    prevClasses.append([etat for etat in auto['etats'] if etat not in auto['F']])

    print(prevClasses)

    classes = calcNextClasse(prevClasses, auto)

    print(classes)

    # on s'arrete lorsque qu'on trouve deux fois les memes classes d'affilé 
    while prevClasses != classes:
        prevClasses = classes
        classes = calcNextClasse(prevClasses, auto)
        print(classes)

    # on renvoie les classes definitives
    return classes

    
def calcNextClasse(prevClasses, auto):
    
    classes = list()

    # pour chaque classe
    for classe in prevClasses:
        
        # les classes contentant un état ne change pas
        if len(classe) == 1:

            # on la remet tel quelle dans les nouvelles classes
            classes.append(classe)
            continue

        # on ajoutes les nouvelles classes
        classes.extend(calcNewClasse(classe, auto, prevClasses))
    
    return classes
        

def calcNewClasse(classe, auto, prevClasses):
    """renvoie uun dictionnaire avec comme clée 
    un tuple contenant les num des classe pour les lettes de l'alphabet
    et comme valeur la liste de tout les états de la classe qui ont ces resultats la
    """

    nClasse = dict()
    
    for etat in classe:

        resLst = list()

        for a in auto['alphabet']:

            # on ajoute les numéro de classe des etat 
            # ou mène les etiquettes
            resLst.append(getNumClasse(prevClasses, point(auto, etat, a)))
        
        # on converti en tuple pour qu'elle puisse entre une clée du dict
        res = tuple(resLst)

        # si la clée n'existe pas deja
        if res not in nClasse:
            nClasse[res] = [etat]
        else:
            nClasse[res].append(etat)

    
    # on revoi la liste de liste contenant tout les états qui ont le meme res
    return list(nClasse.values())
        

            

def getNumClasse(prevClasse, etat):
    """renvoi le numéro de la classe ou se trouve l'état """
    for i, classe in enumerate(prevClasse):
        if etat in classe:
            return i



    

if __name__ == "__main__":
    auto = {
        "alphabet":['a','b'],
        "etats": [1, 2, 3, 4, 5, 6],
        "transitions":[[1,'a',2], [1,'b',2], [2,'a',3], [2,'b',4], [3,'a',4], [3,'b',5], [4,'a',3], [4,'b',6], [5,'a',6], [5,'b',5], [6,'a',5], [6,'b',6]], 
        "I":[1],
        "F":[5, 6]
    }

    auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],
    "transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],
    [4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],
    "I":[0],"F":[0,1,2,5]}

    print(renommage(minimise(auto6)))    
    