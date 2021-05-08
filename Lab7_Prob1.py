#Problem 1- Python Superhero Name

def intro():
    print('Hello this program will take a Zodiac sign and eye color and give you a unique Superhero Name')

#create the dictionary for the zodiac signs with the key values
zodiac = {'Aries' : 'Red', 'Tarus' : 'Orange', 'Gemini' : 'Yellow', 'Cancer' : 'Green', 'Leo' : 'Blue', 'Virgo' : 'Indigo', 'Libra' : 'Violet', 'Scorpio' : 'Pink', 'Saggitarius' : 'Brown', 'Capricorn' : 'Gray', 'Aqarius' : 'Lavender', 'Pisces' : 'Turquoise'}

#create the dictionary for the eye color with the key values
eye = {'brown' : 'Thor', 'blue' : 'Wolverine', 'hazel' : 'Iron Man', 'green' : 'Ghost Rider', 'gray' : 'Daredevil', 'amber' : 'Hulk'}

def main():
#input the user for the zodiac sign in uppercase
    color = input('Enter your Zodiac Sign (Uppercase): ')

#if the user inputs a color not in the dictionary, prompt error
    if color not in zodiac:
        print(color, 'is an invalid value.')

#input the user for the eye color in lowercase
    superhero = input('Enter an eye color of your choice (lowercase): ')

#if the eye color is not in the dictionary, prompt error
    if superhero not in eye:
        print(superhero, 'is an invalid value.')

#print the users superhero 
    print('Your zodiac superhero is:',zodiac[color], eye[superhero])

main()
