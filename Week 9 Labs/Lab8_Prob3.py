# Problem 3 - Professional Sports Team Class/ MLB Teams Subclass

#intro function to describe what the program will do
def intro():
    print('This program will prompt the user for information for one MLB team and display the information back to the user')

#import the MLB_Teams subclass
from chp11_sp2021_lab import MLB_TEAMS

def main():
    
#call the intro function
    intro()

#input the user for the team name, home city, sport, mascot, team batting average, team pitching ERA
    team_name = input('Enter the team name: ')
    home_city = input('Enter the home city of the team: ')
    sport = input('Enter the sport of the team: ')
    mascot = input('Enter the mascot of the team: ')
    team_batting_average = input('Enter the batting average for this team: ')
    team_pitching_ERA = input('Enter the earned run average for this team: ')
    
#create the MLB team
    MLB_Team = MLB_TEAMS(team_name, home_city, sport, mascot, team_batting_average, team_pitching_ERA)

#display the data to the user
    print('The name of the team is:', MLB_Team.get_team_name())
    print('The city of of the team is:', MLB_Team.get_home_city())
    print('The sport of the team is:', MLB_Team.get_sport())
    print('The mascot of the team is:', MLB_Team.get_mascot())
    print('The team batting average of the team is:', MLB_Team.get_team_batting_average())
    print('The team pitching earned run average is:', MLB_Team.get_team_pitching_ERA())

#call the main function
main()
    
