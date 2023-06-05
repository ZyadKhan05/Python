#Problem 2- Write directory Information to a directory.txt file
def intro():
    print('Hello, this function will create a directory of contributors for a local community group.')
    
def main():
# Calling the function explaining the purpose of the program
    intro()
# The local variables of the program
    name = ''
    favorite_dessert = ''
    zip_code = 0
    num_contribution = 0
    num_contributors = 0

# Prompt user for the number of players
    num_contributors = int(input('Enter the number of ' \
                                 'contributors: '))

# Open directory.txt for writing
    file_object = open('directory.txt', 'w')
    
# Write data to file
    for i in range(num_contributors):
# Prompt for name
        name = input('Enter the name of the contributor: ')
        
# Prompt for favorite dessert 
        favorite_dessert = input('Enter your favorite dessert: ')

# Prompt for a Zip Code
        zip_code = int(input('Enter your zip code: '))
        
# Prompt for the monetary contribution amount
        num_contribution = int(input('Enter the amount they donated to the local community group: '))

# Write data to file  
        file_object.write(name + '\n')
        file_object.write(favorite_dessert + '\n')
        file_object.write(str(zip_code) + '\n')
        file_object.write(str(num_contribution) + '\n')

# Close the file
    file_object.close()

# Call the function
if __name__ == '__main__':
    main()

