#Problem 1 Module

#create the class called student 
class Student: 
    def __init__(self, name, major, credits_earned):
        self.__name = name
        self.__major = major
        self.__credits = credits_earned
#set the name 
    def set_name(self, name):
        self.__name = name
#set the major of the student            
    def set_major(self, major):
        self.__major = major
#set the amount of credits earned by the student          
    def set_credits(self, credits_earned):
        self.__credits = credits_earned
#get the student's name                
    def get_name(self):
        return self.__name
#get the student's major           
    def get_major(self):
        return self.__major
#get the amount of credits the student has earned        
    def get_credits_earned(self):
        return self.__credits
