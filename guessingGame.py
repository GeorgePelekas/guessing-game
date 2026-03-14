wor=input("Give me a secret word ")
word=set(wor)
tries=5
while tries>0 and len(word)>0:
        guess=input("Make a guess with a letter: ")
        if guess in word:
                word.remove(guess)
                print("you found the letter",guess)
                
        elif guess not in word:
                tries-=1
                print("you did not find any letter, you have ",tries," left")
if len(word)==0:
        print("you won! the word was",wor)
else:
        print("you lost the word was",wor)

