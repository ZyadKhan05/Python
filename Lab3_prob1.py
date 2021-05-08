#Question 1- Perimeter for a n-sided Polygon
sides = int(input('Enter the amount of sides your polygon has: ')) #Asks user to input the amount of sides their polygon has
length = 0

for i in range(sides):
    length += float(input('Enter the values of each side: ')) #obtain the values of the sides
    
       
    #the accumlator
    perimeter = 0.0
    perimeter = length 

print('The perimeter of this' ,sides,'sided polygon is:' , perimeter, 'units') #display the perimeter
 

