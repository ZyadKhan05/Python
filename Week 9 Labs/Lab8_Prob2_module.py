#Problem 2 Module

#create the class book
class Book:
    def __init__(self, title, author, price, rating):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__rating = rating

#set the variable title of the book        
    def set_title(self, title):
        self.__title = title

#set the variable author of the book          
    def set_author(self, author):
        self.__author = author

#set the variable price for the book from Amazon.com            
    def set_price(self, price):
        self.__price = price

#set the rating from amazon
    def set_rating(self, rating):
        self.__rating = rating

#get the title variable        
    def get_title(self):
        return self.__title

#get the author variable
    def get_author(self):
        return self.__author

#get the price variable            
    def get_price(self):
        return self.__price

#get the rating variable        
    def get_rating(self):
        return self.__rating

#str method
    def __str__(self,book):
        print("The title of the book: " + self.__title)
        print("The Author's name: " + self.__author)
        print("The Price of the book:" , self.__price)
        print("The Rating of the book:" , self.__rating, "out of 5 stars")

              
            
        
