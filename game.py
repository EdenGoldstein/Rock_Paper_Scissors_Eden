'''
this flie contain the Game class, which represents the game logic.
'''

import random


class Game:

    def __init__(self):

        self.computer_score = 0
        self.player_score = 0
        self.player_move = ""
        self.computer_move = ""

    def play_game(self):

        while True:

            player_move = self.get_player_move()
            if player_move == 'q':
                print("Thank you for playing!Goodbye!")
                return
            elif player_move not in ["Rock", "Paper", "Scissors"]:
                print("Please choose one move from - Rock , Paper, Scissors")
                continue
            else:
                computer_move = self.get_computer_move()
                winner = self.determine_winner(player_move, computer_move)
                if winner == "no winner":
                    print(f"There is {winner}")
                else:
                    print(f"The winner is the {winner}")

    def get_player_move(self):

        '''
        Prompts the player to enter their move (Rock, Paper, or Scissors)
        and returns the chosen move.
        '''

        player_move = input(
            "choose your move - Rock, Paper, or Scissors:"
            "choose 'Q' to quit the game"
            )
        return player_move

    def get_computer_move(self):
        '''
        Generates a random move for the computer player
        (Rock, Paper, or Scissors) and returns it.
        '''
        game_options = ["Rock", "Paper", "Scissors"]
        computer_move = random.choice(game_options)
        return computer_move

    def determine_winner(self, player_move, computer_move):

        '''
        Determines the winner based on the game rules and updates the score
        '''
        if player_move == computer_move:
            return "no winner"

        elif player_move == "Scissors":
            if computer_move == "Rock":
                return "computer"
            else:
                return "player"

        elif player_move == "Rock":
            if computer_move == "Paper":
                return "computer"
            else:
                return "player"

        else:
            if computer_move == "Scissors":
                return "computer"
            else:
                return "player"
