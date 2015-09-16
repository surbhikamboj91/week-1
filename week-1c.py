import random

gameStake = 100
cards = range(10)
game = 1


    
def play(dealerCard, playerCard):        
   
    for i in range(7):
        dealerCard = random.randint(0,9)
        playerCard = random.randint(0,9)
        if playerCard < dealerCard:

            print "player " + str(i) + " Lose, " + str(playerCard) + " vs. " + str(dealerCard)       


        else:
        
            print "player " + str(i) + " Win, " + str(playerCard) + " vs. " + str(dealerCard)
            
game += 1
            

          
   
print 'game ' + 'results: '
