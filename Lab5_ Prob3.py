#Problem 3- Read/Display directory file with summary stats and exception handling
def intro():
    print('Hello, this function will display summary statistics from the directory.txt file.')

   
def main():
    try:
#Calling the function explaining the purpose of the program
        intro()

        
#The local variables of the program
        line = ''
        name = ''
        favorite_dessert = ''
        zip_code = 0
        num_contribution = 0
#Open directory.txt for writing
        infile = open('directory.txt', 'r')
        
#Read the first name
        name = infile.readline()

        while name != '':
            favorite_dessert = infile.readline()
            zip_code = int(infile.readline())
            num_contribution = int(infile.readline())

            name = name.rstrip('\n')
       
#display data 
        print(f'Name: {name!r}')
        print(f'Favorite Dessert: {favorite_dessert!r}')
        print(f'Zip Code: {zip_code!r}')
        print(f'Contribution Amount: ${num_contribution!r}')
    
#exception handling
    except IOError:
        print("File doesn't exist cannot perform operations on the file")
    except ValueError:
        print("Invalid input:")
        print(repr(line))
    else:
        print("No name entered:{}".format(name))
        print("No dessert entered:{}".format(favorite_dessert))
        print("No zip code entered:{}".format(zip_code))
        print("No monetary contribution entered:{}".format(num_contribution))       
#read next name
    name = infile.readline()
    
# Close the file
    infile.close()
            

main()

def number_contributors():
    num_contributors = 1
    print('The number of contributors were: ', num_contributors)

number_contributors()
