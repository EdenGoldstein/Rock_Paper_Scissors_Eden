import pytest
from game import Game


def test_get_computer_move():

    game = Game()
    returned_computer_move = game.get_computer_move()
    assert returned_computer_move in ["Rock", "Paper", "Scissors"]


def test_determine_winner():

    game = Game()
    returned_winner = game.determine_winner("Rock", "Paper")
    assert returned_winner in ["computer", "player", "no winner"]
