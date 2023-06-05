#Problem 1- Student Class
#Intro function explaining the purpose of the program 
def intro(): 
    print('Hello, this program will create a class called student and store info')
#import the class Student from the py file
from Lab8_Prob1_module import Student

#main function
def main():
#run the intro statement
    intro()

#input the user for: Name, Major, and the amount of credits earned    
    name = input('What is your name: ')
    major = input('What is your major: ')
    credits_earned = input('How many credits have you earned: ')

#create the student 1    
    student1 = Student(name, major, credits_earned)

#print all of the info    
    print('\nName:', student1.get_name())
    print('The students major:', student1.get_major())
    print('Amount of credits earned:', student1.get_credits_earned())

#call the main function
main()

    

    
    
