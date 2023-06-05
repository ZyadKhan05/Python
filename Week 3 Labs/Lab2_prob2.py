#Question 2: Enhanced Fujita Tornado Scale
print('This program will ask the user for a 3-second wind gust and return the EF rating')
wind_gust = int(input('Enter the 3 second wind gust speed in mph: ')) #user is asked to enter the wind speed

if (wind_gust >= 65) and (wind_gust <= 85):
    print('This wind is considered a 0 rating on the EF Scale') #the EF scale has wind speeds 65-85 mph as the EF rating 0

elif (wind_gust >= 86) and (wind_gust <= 110):
    print('This wind is considered a 1 rating on the EF Scale') #The EF scale has wind speeds 86-110 mph as the EF rating 1

elif (wind_gust >= 111) and (wind_gust <= 135):
    print('This wind is considered a 2 rating on the EF Scale') #The EF scale has wind speeds of 111-135 mph as rating 2

elif (wind_gust >= 136) and (wind_gust <= 165):
    print('This wind is considered a 3 rating on the EF Scale') #The EF scale has wind speeds of 136-165 mph as rating 3

elif (wind_gust >= 166) and (wind_gust <= 200):
    print('This wind is considered a 4 rating on the EF Scale') #The EF scale has wind speeds of 166-200 as rating 4

elif (wind_gust > 200):
    print('This wind is considered a 5 rating on the EF Scale') #The EF scale classifies anything over 200mph as level 5

else:
    print('This is too low to be considered on the EF Scale')#The EF scale doesn't measure anything under 65 mph so it is considered too low 
