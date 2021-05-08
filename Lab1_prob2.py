#Question 2
print('Hello this program is a Carroll County property tax calculator. All you need to do is enter the value of the property')#inform the user about what this program does
propertyValue = int(input('Enter the value of the property: ')) 
CARROLL_PROP_TAX_RATE = 0.01018 #The tax rate for Carroll County
tax = CARROLL_PROP_TAX_RATE * propertyValue #The equation to figure out the tax
print ('The property tax is $%.2f' % tax) 
