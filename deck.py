from card import Card
from random import randint

class Deck:

    def __init__(self):
        self.cards = self.createDeck()
    
    def createDeck(self):
        deck = []
        for cardName in range(13):
            for cardSuit in range(1,5):
                deck.append(Card(cardName,cardSuit))
        return deck
    
    def shuffle(self):
        #generic shelf
        for indice in range(len(self.cards)):
            currentDeck = self.cards[indice:]
            swapIndice = randint(0,len(currentDeck)-1) 

            self.cards[indice],self.cards[indice + swapIndice] = currentDeck[swapIndice],self.cards[indice]

        print("deck shuffled")
        return self.cards
