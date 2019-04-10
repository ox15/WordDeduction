import sys, random

class Game(object):
    def __init__(self):
        pass

    def loadWords(self):
        WORDLIST_FILENAME = "words.txt"

        try:
            print("Loading word list from file: "+WORDLIST_FILENAME)
            # inFile: file
            inFile = open(WORDLIST_FILENAME, 'r')
        except FileNotFoundError:
            print("File not found:", WORDLIST_FILENAME)
            sys.exit()
        else:
            # self.wordList: list of strings
            self.wordList = []
            for line in inFile:
                if len(line)==5: # Go through the list and pull out all 3-letter words
                    self.wordList.append(line.strip())

            print("  ", len(self.wordList), "words loaded.")

            # Uncomment this to choose a random word
            #self.word = self.wordList[random.randint(0,len(self.wordList))]
            self.word = "TREE"


    def won(self):
        """Check if we won. If not, find how many matches we made."""

        if self.guess == self.word:
            print("You won! The word was", self.word)
            sys.exit()
        else:
            self.placed()
            self.misplaced()





    def placed(self):
        self.placedLetters = set()
        numPlaced = 0
        for i in range(len(self.guess)):
            if self.guess[i] == self.word[i]:
                # Check if the letters in position i match
                numPlaced += 1
                self.isPlaced = True
                # Add the placed letter from the word
                self.placedLetters.add(self.word[i])
        if numPlaced != 0:
            print("Correctly placed letters:", numPlaced)
            print(self.placedLetters)
        else:
            print("No letters were placed correctly")
        return i

    def misplaced(self):
        """Check if we misplaced any letters."""
        self.misplacedLetters = set()
        for letter in self.guess:
            if letter in self.word and letter not in self.placedLetters:
                self.misplacedLetters.add(letter)
        if len(self.misplacedLetters) != 0:
            print("Misplaced letters:", str(len(self.misplacedLetters)))
            print(self.misplacedLetters)
        else:
            print("No letters were misplaced")


    def play(self):
        self.length = input("How many letters in the word? [3-")
        self.loadWords()
        print("Word :", self.word)
        #while True:
            # Run and quit once for easier debugging.
        self.guess=input("Guess: ").upper()
        """if self.guess=="Q":
            break"""
        self.won()


if __name__ == '__main__':
    g=Game()
    g.play()
