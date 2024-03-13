# Exercice 1

tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
mots_possibles = ['sacre', 'sabre', 'baser', 'cabre', 'garce',
'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare',
'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars',
'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars',
'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas',
'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']



def longest_word_possible(available_words, letters):
    length = 0
    longest_word = []
    for word in available_words:
        letters_available = list(tirage)
        if len(word) >= length:
            test = 1
            lettres = list(word)
            for lettre in lettres:
                if lettre not in letters_available:
                    test = 0
                else:
                    letters_available.remove(lettre)
            if test == 1:
                length = len(lettres)
                longest_word.append(word)

    return longest_word

# Exercice 2

available_words = []

file = open("motssansaccent.txt",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()

print("Le mot le plus long possible est :",longest_word_possible(mots_possibles, tirage))

# Exercice 3

points = {"a" : 1, "e" : 1,"i" : 1,"l" : 1,"n" : 1,"o" : 1,"r" : 1,"s" : 1,"t" : 1,"u" : 1,"d" : 2,"g" : 2,"m" : 2,"b" : 3,"c" : 3,"p" : 3,"f" : 4,"h" : 4,"v" : 4,"j" : 8,"q" : 8,"k" : 10,"w" : 10,"x" : 10,"y" : 10,"z" : 10}

def score(word):
    lettres = list(word)
    score = 0
    for letter in lettres:
        score += points[letter]
    return score

#print("Le score est de :",score("renaud"))

def max_score(words):
    maximum = 0
    max_word = words[0]
    for word in words:
        if score(word) > maximum:
            max_word = word
            maximum = score(word)
    return max_word

#print(max_score(["renaud", "alexis", "baumgarten"]))

def longest_word_possible_score(available_words, letters):
    length = 0
    longest_word = []
    for word in available_words:
        letters_available = list(tirage)
        if len(word) >= length:
            test = 1
            lettres = list(word)
            for lettre in lettres:
                if lettre not in letters_available:
                    test = 0
                else:
                    letters_available.remove(lettre)
            if test == 1:
                length = len(lettres)
                longest_word.append(word)

    return max_score(longest_word)

print(longest_word_possible_score(mots_possibles,tirage))