from random import randrange

def genAuto(alphabet = ['a', 'b']):
    """renvoie un automate aléatoire"""

    auto = {
        'alphabet': alphabet,
        'I': [],
        'etats': [],
        'transitions': [],
        'F': []
    }

    # nb état entre 2 et 6 plus d'état ferait trop de transi 
    auto['etats'] = list(range(randrange(2, 6)))

    # 1 ou plusieurs états initiaux
    for i in range(randrange(1, len(auto['etats']) + 1)):
        etatInitRandom = auto['etats'][randrange(len(auto['etats']))]
        if etatInitRandom not in auto['I']:
            auto['I'].append(etatInitRandom)

    # meme chose pour les états finaux
    for i in range(randrange(1, len(auto['etats']) + 1)):
        etatFinRandom = auto['etats'][randrange(len(auto['etats']))]
        if etatFinRandom not in auto['F']:
            auto['F'].append(etatFinRandom)

    # les transisitons aléatoire
    # nb transi max pour n états len(auto['alphabet']**n
    for i in range(randrange(1, len(auto['alphabet'])**len(auto['etats']))):
        transiRandom = [auto['etats'][randrange(len(auto['etats']))], auto['alphabet'][randrange(len(auto['alphabet']))], auto['etats'][randrange(len(auto['etats']))]]
        if transiRandom not in auto['transitions']:
            auto['transitions'].append(transiRandom)    
    
    return auto


if __name__ == "__main__":
    print(genAuto())