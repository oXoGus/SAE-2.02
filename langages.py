
def concatene(L1, L2):
    """
    >>> L1=['aa','ab','ba','bb']
    >>> L2=['a', 'b', '']
    >>> print(concatene(L1,L2))
    ['aaa', 'aab', 'aa', 'aba', 'abb', 'ab', 'baa', 'bab', 'ba', 'bba', 'bbb', 'bb']
    """
    # 1.2.1

    # on pourrait utiliser un set pour supp les doublons directement mais le doctest met une erreur
    # parce que les élément dans un set sont pas dans le même ordre
    concatLst = list()
    
    # pour chaque mot de L1
    for m1 in L1:
        
        # on le concatene avec tout les mot de L2
        for m2 in L2:

            if m1 + m2 not in concatLst:
                concatLst.append(m1 + m2)
    
    # on renvoie bien le res sous forme de list
    return concatLst


def puis(L, n):
    """
    >>> L1=['aa','ab','ba','bb']
    >>> print(puis(L1,2))
    ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']
    """

    # 1.2.2

    # on part du mot vide pour que losque n = 1 
    # res = L
    res = ['']
    for _ in range(n):
        res = concatene(res, L)

    return res


# 1.2.3
# on ne peut pas faire une fonction calculant l'étoile d'un langage 
# puisqu'il est impossible de représenter une infinitée de mots en python 

def tousmots(A, n):
    """
    >>> print(tousmots(['a','b'],3))
    ['', 'a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
    """

    # on fait la puis de 0 a n
    res = list()

    for i in range(n + 1):
        res.extend(puis(A, i))

    return res



if __name__ == "__main__":

    import doctest

    doctest.testmod(verbose=1)    


