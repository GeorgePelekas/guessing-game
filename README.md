# guessing-game
def kremala(word):
    tries = 5
    guess = input("guess a word: ")
    while tries >1:
        if guess in word:
            print("you found the letter",guess)
            guess = input("make another guess: ")
        else:
            tries -=1
            print("you found nothing you have ",tries,"left")
            guess = input("make another guess: ")
        
        if tries == 1:
            print("you lost the word was"+word)
leksi = input("give me a secret word")
kremala(leksi)
