#Problem 2 - Set Operations with Baltimore Orioles
#intro function that describes what the program does
def intro():
    print('Hello this program will create two new sets: same_orioles and total_orioles')
    
def main():
#create the set orioles2020 using the text file Orioles_2020
    orioles2020 = set(line.strip() for line in open('Orioles_2020.txt'))
#print the length of orioles2020
    print('The number of players in the set orioles2020 is:', len(orioles2020))

#create the set orioles2020 using the text file Orioles_2020
    orioles2021 = set(line.strip() for line in open('Orioles_2021.txt'))
#print the length of orioles2021
    print('The number of players in the set orioles2021 is:', len(orioles2021))

#find the players who were on both orioles2020 set and orioles2021 set    
    same_orioles = orioles2020.intersection(orioles2021)
#print the players on both rosters
    print('The players who were on both rosters are:', same_orioles)
#print the length of players on both rosters
    print('The number of players who were on both rosters is:', len(same_orioles))
    
 #find the total of both sets   
    total_orioles = orioles2020.union(orioles2021)
#print the total of players on both rosters
    print('The total players on either roster are:', total_orioles)
#print the amount of players
    print('The number of total players on both rosters is:', len(total_orioles))

#run the main function
main()
