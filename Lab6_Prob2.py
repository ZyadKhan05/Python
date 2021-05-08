#Problem 2- Use matplotlib to graph Bowie Baysox text file
#import the module
import matplotlib.pyplot as plt

#intro to describe what this program's purpose is
def intro():
    print('Hello, this program will use the module matplotlib to graph the attendance of Bowie Baysox annual attendance')

def main():
#open the bowie baysox file
    file_object = open('Bowie_Baysox_attend.txt', 'r')
#set the y value as a empty list
    y = []
#for loop for each value in the text file
    for i in range(0,13):
#read each line of the file
        y_value = file_object.readline()
#make each line of the file into a float
        y_value = float(y_value.rstrip())
        y.append(y_value)        
#set the x-coordinate values, which are the years
        x = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

#plot the file as a line graph with red color
    plt.plot(x, y, color='red', marker = 'o')
#name the graph
    plt.title('Bowie Baysox Annual Attendance')
#label the x and y axes
    plt.xlabel('Year')
    plt.ylabel('Attendance')
    plt.show()
    file_object.close()

#call the main function   
main()
