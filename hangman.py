""" This program is a game that asks the user to guess a random word """
import random
import string
words=["hello","hi","good","bad","great","funny","bye","how","here"]    #it would be a long list of words

def get_a_word(words) :
    word = random.choice(words)
    if ' ' in word or '-' in word :
        word = random.choice(words)
    return word

def hangman() :
    print("WELCOME !!!\n*******This is a hangman game, you have to guess a random word*******")
    word = get_a_word(words)                #un mot aleatoire
    wordLetters = set(word.upper())         #les lettres qui composent 'word'
    alphabet = set(string.ascii_uppercase)  #les lettres de l'alphabet
    usedLetters = set()                     #les lettres deja utilisees par l'utilisateur
    userWord = ""
    for i in word:
        userWord+= "-"
    print(userWord)                         #le mot de l'utilisateur

    while userWord.lower() != word:         #continuer jusqu'a ce que le mot de l'utilisateur ressemble au mot a trouver
        userLetter = input("Guess a letter : ").upper()     #l'utilisateur va entrer une lettre
        if userLetter in alphabet - usedLetters :           #si la lettre n'a pas encore ete utilisee
            usedLetters.add(userLetter)                     #ajouter aux lettres deja utilisees
            use=""
            for u in usedLetters:
                use += u
            print("You have used :"+use)                    #afficher les lettres deja utilisees
            if userLetter in wordLetters :                  #si la lettre fait partie du mot a trouver
                wordLetters.remove(userLetter)              #enlever cette lettre
                userWord = word.upper()                     #copier le mot a trouver
                for w in userWord:                          #pour chaque lettre de ce mot a trouver
                    if w in wordLetters:                    #masquer les lettres pas encore trouvees
                        userWord = userWord.replace(w,'-')
            else :
                print("Please try again !")                 #demander de recommencer si la lettre ne fait pas partie du mot a trouver
            print("The current word is : "+userWord)
        else :
            print("You have already used this letter.")

    print("Congrats, you have guessed the word \""+ word+"\" correctly !!!")

hangman()
