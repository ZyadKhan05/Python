import math #imports the module math
def purpose():
    print('Hello, this function prompts the user for the radius of a sphere and give an option for the volume and the surface area for the sphere')

VOLUME_SPHERE_CHOICE = 1
SURFACE_AREA_CHOICE = 2
QUIT_CHOICE = 3

def main():
    purpose()
    choice = 0 
    while choice != QUIT_CHOICE: #in ord
        display_menu()

        choice = int(input('Enter your choice: ')) #ask the user for which choice they want to make

        if choice == VOLUME_SPHERE_CHOICE:
            r = float(input('Enter the radius of your sphere: ')) #prompt the user for a radius value

            surfaceArea = 4 * math.pi * r **2 #calculation to get the Surface Area of a sphere
            print('The Surface Area is: ', round(surfaceArea,2))

        elif choice == SURFACE_AREA_CHOICE:
            r = float(input('Enter the radius of your sphere: ')) #prompt the user for a radius value

            volume = (4/3) * (math.pi * r **3) #calculation to get the Volume of a sphere
            print('The Volume is: ', round(volume,2))

        elif choice == QUIT_CHOICE: #if the user chooses the quit option
            print('Now exiting the program...') #end program

        else:
            print('Error: Invalid choice.') #allows user to re-enter their choice

            
def display_menu(): #function of the display menu
    print('        MENU') 
    print('1) Volume of a Sphere') #the first choice of the menu: Volume
    print('2) Surface Area of a Sphere') #the second choice of the menu: Surface Area
    print('3) Quit') #the third and last option of the menu: Quit the program

#call the main function    
main()
