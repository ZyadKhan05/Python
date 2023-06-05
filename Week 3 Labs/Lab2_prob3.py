#Question 3: Points in the Cartesian Plane
print('This program will get an x & y value and give the user which quadrant of a plane it belongs to')
x = int(input('Enter the x value: ')) #asks the user for the x value
y = int(input('Enter the y value: ')) #asks the user for the y value

if (x > 0 and y > 0):
   print('This point lies in the: First Quadrant')

elif (x < 0 and y > 0):
   print('This point lies in the: Second Quadrant')

elif (x < 0 and y < 0):
    print('This point lies in the: Third Quadrant')

elif (x > 0 and y < 0):
    print('This point lies in the: Fourth Quadrant')

elif (x > 0 and y == 0):
    print('This point lies at the Positive x axis')

elif (x == 0 and y > 0):
    print('This point lies at the positive y axis')

elif (x < 0 and y == 0):
    print('This point lies at the negative x axis')

elif (x == 0 and y < 0):
    print('This point lies at the negative y axis')

else:
    print('This point lies at the Origin')




