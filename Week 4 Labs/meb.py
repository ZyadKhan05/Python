#Question 3- Mad Libs; Nested For Loops
print('This program will display Mad Lib like phrases with verbs, adjectives, and nouns to demonstrate nested for loops')

#Enter the two verbs and store them in variables
verb = input('Enter the first verb: ')
verb_2 = input('Enter the second verb: ')
    
verbs = (verb, verb_2)

#Enter three adjectives and store them in varbiables
adj = input('Enter the first adjective: ')
adj_2 = input('Enter the second adjective: ')
adj_3 = input('Enter the third adjective: ')

adjs = (adj, adj_2, adj_3)


#Enter two nouns and store them in variables
noun = input('Enter the first noun: ')
noun_2 = input('Enter the second noun: ')

nouns = (noun, noun_2)

#Use nested for loop in the verb, adjective, noun format.
for verb in verb:
    for adj in adj:
        for noun in noun:
            print(verbs,
                 adjs,
                 nouns)
                        
print(verb, adj, noun)
print(verb, adj, noun_2)
print(verb, adj_2, noun)
print(verb, adj_2, noun_2)
print(verb, adj_3, noun)
print(verb_2, adj_3, noun_2)
print(verb_2, adj, noun)
print(verb_2, adj, noun_2)
print(verb_2, adj_2, noun)
print(verb_2, adj_2, noun_2)
print(verb_2, adj_3, noun)
print(verb_2, adj_3, noun_2)
       
               
