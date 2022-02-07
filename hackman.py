import config
import requests

class hackman():
    def __init__(self):
        self.word = ""
        self.displayWord = ""
        self.userGuess = ""
        self.params = {
            "key": config.api_key,
            "length": 15
        }

    # gets a word from API
    def callAPI(self):
        response = requests.get("https://clemsonhackman.com/api/word", self.params)
        self.word = response.json()["word"]
        for x in range(len(self.word)):
            self.displayWord += "_"
            
        return self.word

    def resetGame(self):
        self.displayWord = ""
        self.userGuess = ""
        self.callAPI()
    
    # returns true if letter was correctly guessed/repeat
    def guessLetter(self, letter):
        if self.userGuess.find(letter) != -1:
            return True    
        self.userGuess += letter
        return self.updateDisplayWord(letter)

    def updateDisplayWord(self, letter):
        # returns false if letter is incorrect
        index = self.word.find(letter)
        if index == -1:
            return False
        
        # updates display word to contain all instances of guessed letter
        while index != -1:
            self.displayWord = self.displayWord[:index] + letter + self.displayWord[index + 1:]
            index = self.word.find(letter, index + 1)
        return True
    
    # check win condition
    def win(self):
        return self.word == self.displayWord
