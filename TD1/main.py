# we define the words and the letters we are able to right in available word and letters

available_words = []
file = open("frenchssaccent.dic",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()
letters = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']

# we create a function wich returns the words we are able to write

def words_possible(available_words, letters):
    words = []
    for word in available_words:
        letters_available = list(letters)
        can_form = True
        for letter in word:
            if letter not in letters_available:
                can_form = False
            else:
                letters_available.remove(letter)
        if can_form:
            words.append(word)
    return words

# exercise 1/2

def longest_word_possible(available_words, letters):
    length = 0
    longest_word = []
    words = words_possible(available_words, letters)
    for word in words:
        if len(word) > length:
            longest_word = [word]
            length = len(word)
        elif len(word) == length:
            longest_word.append(word)
    return (longest_word, length)

# Here is a different version
def longest_word_possible_dif(available_words, letters):
    length = 0
    longest_word = []
    for word in available_words:
        letters_available = list(letters)
        if len(word) >= length:
            test = 1
            for letter in word:
                if letter not in letters_available:
                    test = 0
                else:
                    letters_available.remove(letter)
            if test == 1 and len(word) == length:
                length = len(word)
                longest_word.append(word)
            elif test == 1 and len(word) > length:
                length = len(word)
                longest_word = [word]
    return longest_word

# exercise 3

# let's define the points associated to the letters with a dictionnary

points = {'a' : 1, 'e' : 1,'i' : 1,'l' : 1,'n' : 1,'o' : 1,'r' : 1,'s' : 1,'t' : 1,'u' : 1,'d' : 2,'g' : 2,'m' : 2,'b' : 3,'c' : 3,'p' : 3,'f' : 4,'h' : 4,'v' : 4,'j' : 8,'q' : 8,'k' : 10,'w' : 10,'x' : 10,'y' : 10,'z' : 10}

def score(word):
    score = 0
    letter = list(word)
    for letter in word:
        score += points[letter]
    return score


def max_score(words):
    maximum = 0
    max_word = []
    for word in words:
        if score(word) > maximum:
            max_word = [word]
            maximum = score(word)
        elif score(word) == maximum:
            max_word.append(word)
    return (max_word,maximum)

def highest_score(available_words, letters):
    max = 0
    max_score_words = []
    words = words_possible(available_words, letters)
    return max_score(words)

# Here is a different version
def highest_score_dif(available_words, letters):
    max = 0
    max_score_words = []
    for word in available_words:
        letters_available = list(letters)
        if score(word) >= max:
            can_form = True
            for letter in word:
                if letter not in letters_available:
                    can_form = False
                else:
                    letters_available.remove(letter)
            if can_form and score(word) > max:
                max = score(word)
                max_score_words = [word]
        elif can_form and score(word) == max:
                max_score_words.append(word)
    return (max_score_words, score(max_score_words[0]))

# Exercice 4
# let's define a list wich represents the alphabet

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def highest_score_joker(available_words, letters):
    max_score = 0
    max_score_words = []

    for word in available_words:
        # Loop through each letter position in the word
        for i in range(len(word) + 1):
            # Generate a word variation with the joker at position i
            word_with_joker = word[:i] + '?' + word[i:]
            # Try replacing the joker with each letter from the available letters
            for letter in alphabet:
                new_word = word_with_joker.replace('?', letter)
                if new_word in available_words:
                    word_score = score(new_word) - points[letter]
                    if word_score > max_score:
                        max_score = word_score
                        max_score_words = [new_word]
                    elif word_score == max_score:
                        max_score_words.append(new_word)

    return max_score_words, max_score

# prints

print("Le/s mot/s le/s plus long/s possible/se st/sont :", longest_word_possible(available_words, letters)[0],"avec une longueur de", longest_word_possible(available_words, letters)[1])
print("Le/s mot/s avec le plus haut score est/sont :", highest_score(available_words, letters)[0],"avec un score de", highest_score(available_words, letters)[1])

#print("The longest word/s possible is/are :", longest_word_possible(available_words, letters))
#print("The word/s with the highest score/s is/are :", highest_score(available_words, letters)[0][0], "with a score of",highest_score(available_words, letters)[1])
