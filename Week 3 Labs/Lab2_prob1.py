#Question 1: Baseball Field Positions
print('This program will take a number from 1-9 and give the user the corresponding baseball field position')
num = int(input('Enter a number from 1-9: ' )) #asks the user to enter the number of their chosing

if num == 1 : #Pitcher
   print('The field position for this number is: Pitcher')
elif num == 2 : #Catcher
   print('The field position for this number is: Catcher') 
elif num == 3 : #1st Baseman
   print('The field position for this number is: First Baseman')
elif num == 4 : #2nd Baseman
   print('The field position for this number is: Second Baseman')
elif num == 5 : #3rd Baseman
   print('The field position for this number is: Third Baseman')
elif num == 6 : #Shortstop
   print('The field position for this number is: Shortstop')
elif num == 7 : #Left Fielder
   print('The field position for this number is: Left Fielder')
elif num == 8 : #Center Fielder
   print('The field position for this number is: Center Fielder')
elif num == 9 : #Right Fielder
   print('The field position for this number is: Right Fielder')
else:
   print('Invalid value') #If the value is not a number 1-9, it will say invalid value')
