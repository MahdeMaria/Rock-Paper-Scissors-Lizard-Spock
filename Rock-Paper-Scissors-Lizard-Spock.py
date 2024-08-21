import random

pairs = [("Scissors","Paper"),
        ("Scissors", "Lizard"),
        ("Paper","Rock"),
        ("Paper","Spock"),
        ("Rock","Lizard"),
        ("Rock","Scissors"),
        ("Lizard","Spock"),
        ("Lizard","Paper"),
        ("Spock","Scissors"),
        ("Spock","Rock"),]

choices=["Rock","Spock","Paper","Lizard","Scissors"]
computer_choice = random.choice(choices)

print('Chose your play:')
print('0 for Rock\n1 for Spock\n2 for Paper\n3 for Lizard\n4 for Scissors')

user_input = int(input('Your play: '))
user_choice = choices[user_input]

if computer_choice == user_choice:
    result = 'Player and computer tie!'
elif (user_choice, computer_choice) in pairs:
    result = 'Player wins!'
else:
    result = "Computer wins!"

print('Player chooses', user_choice)
print('Computer chooses', computer_choice)
print(result)

