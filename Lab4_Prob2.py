#Question 2- Dice Game using random number generator
import random #Import the module: random

wins = 0 #defining the win tally, you would start with zero wins
losses = 0 #defining the loss tally, you would start with zero losses

def purpose(): #function with the purpose of this program
    print('Hello, this function will simulate a dice game where you roll twice with the goal of getting a sum of 7')

# Get number of rolls
sims = int(input('How many times do you want to roll the dice: '))

#the main function 
def main(sims):
    purpose()  
    for rolls in range(sims):  
    #loop runs rolls amount of time
        roll = roll_dice(1,6)
        results(roll)

def roll_dice(x, y):
      #generate the amount of rolls
      roll_1 = random.randint(1,6)
      roll_2 = random.randint(1,6)
      return roll_1 + roll_2 #add the two rolls together


  
def results(dices):
  global wins #allows wins to be global throughtout the program
  global losses #allows wins to be global throughout the program
  if dices == 7: #if your two rolls add up to 7, you win
      wins = wins + 1 #everytime you win you get 1 tally 
      print('You rolled 7. You win') 
      
      
  else: #otherwise, you lose
      losses = losses + 1 #everytime you lose you get 1 tally 
      print('You earned', dices, 'points. Sadly you lost') 
      
      

        
# Call the main function
main(sims)

print('You won', wins, 'times!') #win total
print('You lost', losses, 'times.') #loss total
print('Your win rate was:', round(wins/sims, 4)) #prints the amount of wins divided by the amount of simulations 
print('Your loss rate was:', round(losses/sims, 4)) #prints the amount of losses divided by the amount of simulations
