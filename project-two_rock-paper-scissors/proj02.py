# title:          proj02.py
# description:    CSC-125 Project 2: Rock Paper Scissors
# author:         jmalavasi
# date:           072221
# version:        1.0
# ==============================================================================

# import modules
import random
import collections
import time

# define variables
player_choice = ""
player_common_choice = ""
computer_choice = ""
scorecard = {"player": 0,"tie": 0,"computer": 0}
player_choice_history = []
top_two_choices = {}
valid_choices = ["r", "p", "s", "q"]
valid_plays = ["r", "p", "s"]

# get common choice
def get_player_common_choice():
    if len(player_choice_history) > 1: 
        if len(set(player_choice_history)) > 1:
            top_two_choices = collections.Counter(player_choice_history).most_common(2)
            if top_two_choices[0][1] == top_two_choices[1][1]:
                player_common_choice = 'none'
            else:
                player_common_choice = top_two_choices[0][0]
        else:
            player_common_choice = player_choice_history[0]
    else:
        player_common_choice = "none"
    return player_common_choice

# computer choice
def generate_computer_choice(player_common_choice):
    if player_common_choice == "r":
        computer_choice = 'p'
    elif player_common_choice == "p":
        computer_choice = 's'
    elif player_common_choice == "s":
        computer_choice = 'r'
    else:
        computer_choice = "{}".format((random.choice(['r', 'p', 's'])))
    return computer_choice

# determine winner
def determine_winner(computer_choice, player_choice):
    winner = ''
    print("player picks {} and computer picks {}".format(
        player_choice, computer_choice))
    if computer_choice == player_choice:
        scorecard['tie'] += 1
        print("The round ends in a tie.")
    else:
        if computer_choice == 'r' and player_choice != 'p':
            winner = 'computer'
            scorecard['computer'] += 1
        elif computer_choice == 'p' and player_choice != 's':
            winner = 'computer'
            scorecard['computer'] += 1
        elif computer_choice == 's' and player_choice != 'r':
            winner = 'computer'
            scorecard['computer'] += 1
        else:
            scorecard['player'] += 1
            winner = 'player'
        
        print("The winner is {}".format(winner))

# end game
def end_game():
    # the scorecard
    print("\n\nResults:\nYou won {2} rounds.\nThe computer has won {0} rounds.\nThere were {1} ties.\n".format(scorecard['computer'],scorecard['tie'],scorecard['player']))
    
    # player choice history
    print("Player Choice History:\nRock: {}\nPaper: {}\nScissors: {}".format(player_choice_history.count('r'),player_choice_history.count('p'),player_choice_history.count('s')))
    time.sleep(15)
    exit()

# start game
def start_game():
    keepGoing = True
    while keepGoing:
        #### start round ####
        player_common_choice = get_player_common_choice()
        computer_choice = generate_computer_choice(player_common_choice)

        # prompt
        player_choice = input("The round has begun. Do you choose (r)ock, (p)aper, (s)cissors, or (q)uit?: ").lower()

        # while input is invalid, reprompt
        while player_choice not in valid_choices:
            player_choice = input("Do you choose (r)ock, (p)aper, (s)cissors, or (q)uit?: ")

        # if rps continue game, else quit
        if player_choice in valid_plays:
            player_choice_history.append(player_choice)
            determine_winner(computer_choice, player_choice)
            continue
        else:
            keepGoing = False

    end_game()

start_game()