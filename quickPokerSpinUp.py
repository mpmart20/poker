from deck import Deck
from player import Player
from collections import deque

class Poker:
    #5 card poker classic, NOT texas

    def __init__(self):
        self.deck = deque(Deck().shuffle())
        self.players = []

    def dealToPlayers(self):
        for player in self.players:
            currentCard = self.deck.popleft()
            player.hand.append(currentCard)
        
    def startGame(self, names):
        # we deal 5 cards at a time 
        for name in names:
            self.players.append(Player(name))
        for currentCard in range(5):
            self.dealToPlayers()
    
    def calculateHand(self, player):
        """
        TODO: FIGURE SCORING PATTERN
        0-12 face value ?
        13-25 pair values ?
        Needs research
        will just counts pairs atm
        """
        handStats = {
            'rawPoints':0,
            'pairs':0
        }
        seenCards = {}
        for card in player.hand:
            handStats['rawPoints'] += card.name
            current = seenCards.get(card.name)
            if (current):
                seenCards[card.name] += 1
                if(seenCards[card.name] % 2 is 0):
                    handStats['pairs'] += 1
            else:
                seenCards[card.name] = 1

        return handStats
    
    def isWinner(self, numPairs, score, maxPairs, maxScore):
        if ((numPairs > maxPairs) or ((numPairs is maxPairs) and (score > maxScore))):
            return True
        return False
    
    def endGame(self):
        #uses just pairs atm
        # three of a kind counts a 4
        winningPlayerIndex = 0
        maxPairs = 0
        maxRawScore = 0
        for count,player in enumerate(self.players):
            handInfo = self.calculateHand(player)
            if (self.isWinner(handInfo['pairs'],handInfo['rawPoints'],maxPairs,maxRawScore)):
                winningPlayerIndex = count
                maxPairs = handInfo['pairs']
                maxRawScore = handInfo['rawPoints']
        print('%s has won!' % self.players[winningPlayerIndex].name)
     
        
            
#Mock Game
game = Poker()
game.startGame(['Wilson', 'Rob'])
game.endGame()


    