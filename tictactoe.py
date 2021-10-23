import re
from game import tictactoe
import os
os.system('clear')

play_game = input('Would you like to play a game of tic tac toe? ')
play_game = bool(re.search('^[yY]', play_game))
if play_game:
    tictactoe.play()
