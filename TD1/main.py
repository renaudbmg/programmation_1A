# Exercice 1

tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
mots_possibles = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']


def mot_le_plus_long_possible(mots_possibles, tirage):
    longeur = 0
    for mot in mots_possibles:
        test = 1
        lettres = list(mot)
        for lettre in lettres:
            if lettre not in tirage:
                test = 0
        if len(lettres) > longeur and test == 1:
            longeur = len(lettres)
            mot_le_plus_long = mot

    return mot_le_plus_long


# Exercice 2

available_words = []

file = open("motssansaccent.txt",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()

print("Le mot le plus long possible est :",mot_le_plus_long_possible(available_words, tirage))
