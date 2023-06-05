#Problem 2 - Book Class
def intro():
    print('Hello, This program creates a class called book that contains the title, author, price, and rating of that book. ')

#importing the class: Book from the py file
from Lab8_Prob2_module import Book

def main():
#call the intro statement
    intro()
#set the local variables for Book1
    title = "Harry Potter and the Sorcerer's Stone"
    author = "J.K. Rowling"
    price = 11.47
    rating = 4.8
    book1 = Book(title, author, price, rating)

#display the info for book 1
    (book1.__str__(book1))
    print('             ') #create an indent
 
#set the local variables for book2    
    title = "Harry Potter and the Chamber of Secrets"
    author = "J.K. Rowling"
    price = 12.00
    rating = 4.9
    book2 = Book(title, author, price, rating)
    
#display the info for book2
    (book2.__str__(book2))
    print(' ')#create an indent

#set the local variables for book3    
    title = "Harry Potter and the Prisoner of Azkaban"
    author = "J.K. Rowling"
    price = 21.45
    rating = 4.9
    book3 = Book(title, author, price, rating)

#display the info for book 3
    (book3.__str__(book3))
    print(' ') #create an indent

#Set the local variables for book4
    title = "Harry Potter and the Goblet of Fire"
    author = "J.K. Rowling"
    price = 25.68
    rating = 4.9
    book4 = Book(title, author, price, rating)

#display the info for book 4
    (book4.__str__(book4))

#call the main function   
main()    

