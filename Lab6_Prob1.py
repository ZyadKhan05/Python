#Problem 1- Daily Step Count
#intro function explaining the purpose of the function
def intro():
    print('Hello, this program will input the user to enter the number of steps taken each day and display statistics')
#the main function
def main():
    intro()
#ask the user the steps they had on Sunday
    sunday_steps = int(input('Enter the amount of steps you had on Sunday: '))
#ask the user the steps they had on Monday
    monday_steps = int(input('Enter the amount of steps you had on Monday: '))
#ask the user the steps they had on Tuesday
    tuesday_steps = int(input('Enter the amount of steps you had on Tuesday: '))
#ask the user the steps they had on Wednesday
    wednesday_steps = int(input('Enter the amount of steps you had on Wednesday: '))
#ask the user the steps they had on Thursday
    thursday_steps = int(input('Enter the amount of steps you had on Thursday: '))
#ask the user the steps they had on Friday
    friday_steps = int(input('Enter the amount of steps you had on Friday: '))
#ask the user the steps they had on Saturday
    saturday_steps = int(input('Enter the amount of steps you had on Saturday: '))

    
    total_steps = sunday_steps + monday_steps + tuesday_steps + wednesday_steps + thursday_steps + friday_steps + saturday_steps
    avg_steps = total_steps//7
    
    step_lists = [sunday_steps, monday_steps, tuesday_steps, wednesday_steps, thursday_steps, friday_steps, saturday_steps]


    max_steps = max(step_lists)
    min_steps = min(step_lists)
    
    print('The total steps you had in the week was:', total_steps)
    print('The average steps you had in the week was:',round(avg_steps,1))
    print('The most steps you had in the week was:', max_steps)
    print('The fewest steps you had in the week was:',min_steps)
    
main()


    
