import os, sys, random
"""
os: input word list if we can't find it
sys: exit when we're done
random: get random word
"""

class Game(object):
    def __init__(self):
        pass

    def loadWords(self):
        WORDLIST_FILENAME = "words.txt"
        i = 0
        while i >= 0:
            try:
                #print("Loading word list from file: "+WORDLIST_FILENAME)
                inFile = open(WORDLIST_FILENAME, 'r')
                if i > 0:
                    break
            except FileNotFoundError:
                print("I can\'t find any file named "+WORDLIST_FILENAME+" in "+os.getcwd())
                WORDLIST_FILENAME = input("Please tell me the path and name of the file relative to "+os.getcwd()+": ")
            i += 1
        inFile = open(WORDLIST_FILENAME, 'r')
        # self.wordList: list of strings
        self.wordList = []
        for line in inFile:
            if len(line)==self.length+1: # Go through the list and pull out all 3-letter words
                self.wordList.append(line.strip())
        try:
            print(str(len(self.wordList)), str(self.length)+"-letter words loaded from", WORDLIST_FILENAME)
        except:
            print("There are no "+str(self.length)+"-letter words on the list!")
        # Uncomment this to choose a random word
        self.word = self.wordList[random.randint(0,len(self.wordList))]
        #self.word = "TREE"


    def won(self):
        """Check if we won. If not, find how many matches we made."""

        if self.guess == self.word:
            if self.round==0:
                print("You won! You guessed the word", self.word, "on the first try!")
            else:
                print("You won! You guessed the word", self.word, "in", self.round+1, "tries.")
            sys.exit()
            

    def isWordValid(self, word):
        if len(self.guess) != self.length and self.guess != "Q":
            print("Word should be", self.length, "letters long, not", len(self.guess))
        else:
            self.placed()
            self.misplaced()
            return True


    def placed(self):
        self.placedLetters = ""
        numPlaced = 0
        for i in range(min(len(self.guess),len(self.word))):
            if self.guess[i] == self.word[i]:
                # Check if the letters in position i match
                numPlaced += 1
                self.isPlaced = True
                # Add the placed letter from the word
                self.placedLetters += self.word[i]
        if numPlaced != 0:
            print("Place:", numPlaced, "("+self.placedLetters+")")
        else:
            print("Place: None")

    def misplaced(self):
        """Check if we misplaced any letters."""
        self.misplacedLetters = ""
        for letter in self.guess:
            if letter in self.word and letter not in self.placedLetters:
                self.misplacedLetters += letter
        if len(self.misplacedLetters) != 0:
            print("Miss :", str(len(self.misplacedLetters)), "("+self.misplacedLetters+")")
        else:
            print("Miss : None")

    def play(self):
        nextRound = True
        print("'Place' (placed) means the letters that you placed correctly")
        print("'Miss' (missed) means letters that you placed in the wrong spots, but are still in the word")
        print("Enter 'Q' as your guess to exit")
        try:
            self.length = int(input("How many letters in the word? (3) "))
        except ValueError:
            self.length=3
        self.loadWords()
        print("Word :", self.word)
        try:
            tries=int(input("How many tries do you want? (10) "))
            if tries==1: tries=2
        except ValueError:
            tries=10
        for self.round in range(tries):
            
            print("Round", self.round+1)
            while True:
                self.guess=input("Guess: ").upper()
                self.isWordValid(self.guess)
                self.won()
                if nextRound==False:
                    self.round -= 1
                if self.guess=="Q":
                    print("The word was", self.word)
                    break
                
            
            
        # If we didn't win (exited the loop) we lost
        print("You lost!")


if __name__ == '__main__':
    g=Game()
    g.play()
