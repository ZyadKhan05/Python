#Question 1 Tip, Tax, and Total
def purpose():
    print('The purpose of this program is to calculate the tax, tip, and total for a purchase at a restaurant')

#function to get the amount for the Sales Tax
def tax(cost):
    return(cost * 0.06)

#function to get the amount for the Tip 
def tip(cost):
    return(cost * 0.20)

#the main function
def main():
    purpose()
    cost = float(input('The cost of the food is: $ '))
    total = cost + tax(cost) + tip(cost)
    print('Food amount is: $',round(cost,2), 'The tip amount is: $', round(tip(cost), 2), 'and the Maryland sales tax is: $', round(tax(cost), 2), 'The total would be: $', round(total,2) )
    

#call the function so that the program can run
main()
