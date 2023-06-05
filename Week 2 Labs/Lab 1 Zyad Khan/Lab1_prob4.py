#Question 4

print('Hello, this is a US Dollar to British Pound Sterling currency converter.')#Inform the user about the program
dollar = int(input('Please enter the amount of US dollars to be converted: ')) #Asks the user to enter the dollar amount
#The exchange rate is 0.731257, but it needs to be rounded to 0.01
exchange_rate = 0.731257

pound =   dollar * exchange_rate #conversion equation
print('The amount in British Pounds is :', u' \u00a3', round(pound,2))
