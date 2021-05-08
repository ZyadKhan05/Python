def intro():
    print('Hello, this program will collect a string from the user. Then it will take the first letter of those words to create a password')

word = ''

def main():
    intro()
    result = ''
    word = input('Enter your sentence to create a password: ')
    words = word.split()
    password = [word[0] for word in words]
    print('Your new password is:', "".join(password))
    
main()
