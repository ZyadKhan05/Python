#Question 3
#Inform the user about the program
print('Hello, this is a Teaspoon to Milliliter converter. Put in the amount of teaspoons and it will be converted to milliliters for you')
#Get the teaspoon value from the user
t = int(input('How many teaspoons: '))
#convert that value into ml
ml = 0
ml = t * 4.92892
print(round(ml,2)) #Get the ml value that is rounded to 0.01
