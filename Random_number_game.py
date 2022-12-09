import random
from art_for_randome_game import logo
"""In this game player will enter his name and range of numbers.
After this, game will generate random number and player should guess which
number has been generated. After the correct answer, game show amount of attempts and winner name."""


users_name_list = []

def greeting():
    """This function will greet the player and tell him the rules of the game."""

    print(logo)
    print('''Hello dear players!
The rules of the game are simple - I guess a random number in your range, and you try to guess it.
You can enter the names of several players.
Enjoy!''')


def names():
    """This function asks for player names and writes them to the list of players names.
        Also, function show all names,written by the players.
        Function has the option of 'quit the game', if player don't want to play."""

    while True:
        user_name_input = input('''
Enter user name: ''')
        if user_name_input == '':
            print("""You didn't enter anything in the field!
Do you want to quit the game?
Press 'Enter' to continue or type 'No' to quit: """, end='')
            quit_game_or_not = input()
            print()
            if quit_game_or_not.lower() == 'no':
                break
        else:
            users_name_list.append(user_name_input)
        print('''Do you want to add another one player?
Press 'Enter' to continue or type 'No' to quit: ''', end='')
        add_or_not = input()
        if add_or_not.lower() == 'no':
            if len(users_name_list) >= 1 and user_name_input != '':
                print()
                print('Today will play:')
                player_counter = 1
                for player_name in range(len(users_name_list)):
                    print(f'Player {player_counter} - {users_name_list[player_name]}')
                    player_counter += 1
            break


def game_engine():
    """This function takes in number of max range. Then it start the game and users take turns entering their numbers.
        After correct number function will show name of winner, amount of attempts, generated number and finished
        program."""

    def max_range():
        switch = True
        while switch:
            print()
            print(f'Now {users_name_list[0]} need to enter max of random range: ', end='')
            try:
                user_input_max_range = int(input())
            except ValueError:
                print('Invalid data. Try again.')
                continue
            switch -= 1
            return user_input_max_range

    random_number = random.randint(1, max_range())
    counter_of_amounts = 1
    player_index = 0
    print('Excellent! Now lets start the game!')
    while True:
        def input_number():
            switch = True
            while switch:
                try:
                    user_input = int(input(f'{users_name_list[player_index]}, enter your number: '))
                except ValueError:
                    print('Invalid data. Try again.')
                    continue
                switch -= 1
                return user_input

        if input_number() != random_number:
            print('Was close, but not enough. Lucky next time.')
            counter_of_amounts += 1
            if player_index == len(users_name_list) - 1:
                player_index = 0
            else:
                player_index += 1
        else:
            print(f"""Congratulation!
{users_name_list[player_index]} entered the correct number!
Total number of attempts - {counter_of_amounts}.
Random number - {random_number}.

Thanks for the good game! See you soon!""")
            break


greeting()
names()
game_engine()
