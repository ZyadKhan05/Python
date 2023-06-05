#Question 2-Bowling Average; Input Validation
print('Hello, this program will ask for 3 bowling scores from 0-300. Then the average of the three scores will be given')
score = int(input('Enter the 1st bowling score, it can not be greater than 300: ')) #identify the first score

# Validate the bowling score
while(score > 300) or (score < 0):
        print('ERROR: the score is invalid.')
        score = int(input('Enter a correct bowling score: '))

score_2 = int(input('Enter the 1st bowling score, it can not be greater than 300: '))#identify the second score

# Validate the second bowling score
while(score_2 > 300) or (score_2 < 0):
        print('ERROR: the score is invalid.')
        score_2 = int(input('Enter a correct bowling score: '))

score_3 = int(input('Enter the 1st bowling score, it can not be greater than 300: '))#identify the third score

# Validate the third bowling score
while(score_3 > 300) or (score_3 < 0):
        print('ERROR: the score is invalid.')
        score_3 = int(input('Enter a correct bowling score: '))

#Get the average of all three scores
avg_score = (score + score_2 + score_3) / 3 #add up all three scores and divide by 3 to get the average.
print(avg_score)
