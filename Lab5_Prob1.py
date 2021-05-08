#Problem 1- Lucas numbers recursion
# This program uses recursion to print numbers from the Lucas series.

#intro function explaining the program
def intro ():
    print('Hello, this program will use recursoon to print numbers from the Lucas series')
    print('The lucas numbers are a sequence of integers, each integers is defined to be the sum of its two immediately previous terms') 

#the main function
def main():
    intro()
    n = int(input('Enter the amount of Lucas numbers you want to display: ')) #input the user to enter the amount of lucas numbers they wsnt to go to
    print('The first', n, 'numbers in the') 
    print('Lucas series are:')

    for number in range(n): #for the numbers in rsnge of n: the inputed value
        print(lucas(number)) 
    
# The lucas function returns the number inputed by the user in the Lucas series
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# Calling the main function
main()
