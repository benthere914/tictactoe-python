import os
import re
import ascii

empty = {i: ascii.empty_string for i in range(5)}
cell_1 = empty
cell_2 = empty
cell_3 = empty
cell_4 = empty
cell_5 = empty
cell_6 = empty
cell_7 = empty
cell_8 = empty
cell_9 = empty
cells = {'1': cell_1, '2': cell_2, '3': cell_3, '4': cell_4, '5': cell_5, '6': cell_6, '7': cell_7, '8': cell_8, '9': cell_9}
board = f'''
             1            |2            |3
                          |             |
              {cell_1[0]} | {cell_2[0]} | {cell_3[0]}
              {cell_1[1]} | {cell_2[1]} | {cell_3[1]}
              {cell_1[2]} | {cell_2[2]} | {cell_3[2]}
              {cell_1[3]} | {cell_2[3]} | {cell_3[3]}
              {cell_1[4]} | {cell_2[4]} | {cell_3[4]}
             _____________|_____________|_______________
             4            |5            |6
                          |             |
              {cell_4[0]} | {cell_5[0]} | {cell_6[0]}
              {cell_4[1]} | {cell_5[1]} | {cell_6[1]}
              {cell_4[2]} | {cell_5[2]} | {cell_6[2]}
              {cell_4[3]} | {cell_5[3]} | {cell_6[3]}
              {cell_4[4]} | {cell_5[4]} | {cell_6[4]}
             _____________|_____________|_______________
             7            |8            |9
                          |             |
              {cell_7[0]} | {cell_8[0]} | {cell_9[0]}
              {cell_7[1]} | {cell_8[1]} | {cell_9[1]}
              {cell_7[2]} | {cell_8[2]} | {cell_9[2]}
              {cell_7[3]} | {cell_8[3]} | {cell_9[3]}
              {cell_7[4]} | {cell_8[4]} | {cell_9[4]}
                          |             |
        '''

class Game:
    def __init__(self, board, cells, ex_mark, circle, logo):
        self.board = [None for i in range(10)]
        self.winner = None
        self.board = board
        self.cells = cells
        self.ex_mark = ex_mark
        self.circle = circle
        self.logo = logo
        self.message = 'default'
        self.reset = False

    def play(self):
        os.system('clear')
        self.render()
        self.set_up()
        self.flow()

    def set_up(self):
        character = ''
        while not character or not bool(re.search('^[xXoO0]$', character)):
            if len(character):
                print('That was an invalid option.')
            character = input('Which character would you like to be x or o? ')
        if bool(re.search('^[xX]', character)):
            self.choice = self.ex_mark
            self.pc = self.circle
        if bool(re.search('^[oO0]', character)):
            self.choice = self.circle
            self.pc = self.ex_mark

    def make_choice(self):
        selection = ''
        while not selection or not bool(re.search('^[0123456789]$', selection)):
            if len(str(selection)):
                print('That was not a valid location. Please choose one of the available cells.')
            selection = input(f'Where would you like to place down your selection? ')
        self.cells[selection] = self.choice

    def computer_choice(self):
        # check if pc has a missing spot

        if self.missing_spot(self.pc):
            return
        # check if person has a missing spot
        elif self.missing_spot(self.choice):
            return

        # check if pc has 2 missing spots
        elif self.missing_spots():
            return

        # left overs
        else:
            self.left_overs()
            return

    def missing_spot(self, check):
        for i in range(1,4):
            a = False
            b = False
            c = False

            if self.cells[str(i)] == empty:
                a = True
            if self.cells[str(i + 3)] == self.cells[str(i + 6)]:
                b = True
            if self.cells[str(i + 3)] == check:
                c = True
            if a and b and c:
                self.cells[str(i)] = self.pc
                return True

            a = False
            b = False
            c = False

            if self.cells[str(i + 3)] == empty:
                a = True
            if self.cells[str(i)] == self.cells[str(i + 6)]:
                b = True
            if self.cells[str(i)] == check:
                c = True
            if a and b and c:
                self.cells[str(i + 3)] = self.pc
                return True

            a = False
            b = False
            c = False

            if self.cells[str(i + 6)] == empty:
                a = True
            if self.cells[str(i)] == self.cells[str(i + 3)]:
                b = True
            if self.cells[str(i)] == check:
                c = True
            if a and b and c:
                self.cells[str(i + 6)] = self.pc
                return True

        for i in range(1,8,3):
            a = False
            b = False
            c = False

            if self.cells[str(i)] == empty:
                a = True
            if self.cells[str(i + 1)] == self.cells[str(i + 2)]:
                b = True
            if self.cells[str(i + 1)] == check:
                c = True
            if a and b and c:
                self.cells[str(i)] = self.pc
                return True

            a = False
            b = False
            c = False

            if self.cells[str(i + 1)] == empty:
                a = True
            if self.cells[str(i)] == self.cells[str(i + 2)]:
                b = True
            if self.cells[str(i)] == check:
                c = True
            if a and b and c:
                self.cells[str(i + 1)] = self.pc
                return True

            a = False
            b = False
            c = False

            if self.cells[str(i + 2)] == empty:
                a = True
            if self.cells[str(i)] == self.cells[str(i + 1)]:
                b = True
            if self.cells[str(i + 1)] == check:
                c = True
            if a and b and c:
                self.cells[str(i + 2)] = self.pc
                return True

        a = False
        b = False
        c = False

        if self.cells[str(1)] == empty:
            a = True
        if self.cells[str(5)] == self.cells[str(9)]:
            b = True
        if self.cells[str(5)] == check:
            c = True
        if a and b and c:
            self.cells[str(1)] = self.pc
            return True

        a = False
        b = False
        c = False

        if self.cells[str(5)] == empty:
            a = True
        if self.cells[str(1)] == self.cells[str(9)]:
            b = True
        if self.cells[str(1)] == check:
            c = True
        if a and b and c:
            self.cells[str(5)] = self.pc
            return True

        a = False
        b = False
        c = False

        if self.cells[str(9)] == empty:
            a = True
        if self.cells[str(1)] == self.cells[str(5)]:
            b = True
        if self.cells[str(1)] == check:
            c = True
        if a and b and c:
            self.cells[str(9)] = self.pc
            return True

        a = False
        b = False
        c = False

        if self.cells[str(3)] == empty:
            a = True
        if self.cells[str(5)] == self.cells[str(7)]:
            b = True
        if self.cells[str(5)] == check:
            c = True
        if a and b and c:
            self.cells[str(3)] = self.pc
            return True

        a = False
        b = False
        c = False

        if self.cells[str(5)] == empty:
            a = True
        if self.cells[str(3)] == self.cells[str(7)]:
            b = True
        if self.cells[str(3)] == check:
            c = True
        if a and b and c:
            self.cells[str(5)] = self.pc
            return True

        a = False
        b = False
        c = False

        if self.cells[str(7)] == empty:
            a = True
        if self.cells[str(3)] == self.cells[str(5)]:
            b = True
        if self.cells[str(3)] == check:
            c = True
        if a and b and c:
            self.cells[str(7)] = self.pc
            return True

    def missing_spots(self):
        for i in range(1,4):
            a = False
            b = False
            c = False
            if self.cells[str(i)] == self.pc:
                a = True
            if self.cells[str(i + 3)] == empty:
                b = True
            if self.cells[str(i + 3)] == self.cells[str(i + 6)]:
                c = True
            if a and b and c:
                self.cells[str(i + 3)] = self.pc
                return True

            a = False
            b = False
            c = False
            if self.cells[str(i + 3)] == self.pc:
                a = True
            if self.cells[str(i)] == empty:
                b = True
            if self.cells[str(i)] == self.cells[str(i + 6)]:
                c = True
            if a and b and c:
                self.cells[str(i)] = self.pc
                return True

            a = False
            b = False
            c = False
            if self.cells[str(i + 6)] == self.pc:
                a = True
            if self.cells[str(i)] == empty:
                b = True
            if self.cells[str(i)] == self.cells[str(i + 3)]:
                c = True
            if a and b and c:
                self.cells[str(i + 3)] = self.pc
                return True

        for i in range(1,8, 3):
            a = False
            b = False
            c = False
            d = False
            if self.cells[str(i)] == self.pc:
                a = True
            if self.cells[str(i + 1)] == empty:
                b = True
            if self.cells[str(i + 1)] == self.cells[str(i + 2)]:
                c = True
            if a and b and c:
                self.cells[str(i + 1)] = self.pc
                return True

            a = False
            b = False
            c = False
            d = False
            if self.cells[str(i + 1)] == self.pc:
                a = True
            if self.cells[str(i)] == empty:
                b = True
            if self.cells[str(i)] == self.cells[str(i + 2)]:
                c = True
            if a and b and c:
                self.cells[str(i)] = self.pc
                return True

            a = False
            b = False
            c = False
            d = False
            if self.cells[str(i + 2)] == self.pc:
                a = True
            if self.cells[str(i)] == empty:
                b = True
            if self.cells[str(i)] == self.cells[str(i + 1)]:
                c = True
            if a and b and c:
                self.cells[str(i + 1)] = self.pc
                return True

        a = False
        b = False
        c = False
        if self.cells[str(1)] == self.pc:
            a = True
        if self.cells[str(5)] == empty:
            b = True
        if self.cells[str(5)] == self.cells[str(9)]:
            c = True
        if a and b and c:
            self.cells[str(5)] = self.pc
            return True

        a = False
        b = False
        c = False
        if self.cells[str(5)] == self.pc:
            a = True
        if self.cells[str(1)] == empty:
            b = True
        if self.cells[str(1)] == self.cells[str(9)]:
            c = True
        if a and b and c:
            self.cells[str(1)] = self.pc
            return True

        a = False
        b = False
        c = False
        if self.cells[str(9)] == self.pc:
            a = True
        if self.cells[str(1)] == empty:
            b = True
        if self.cells[str(1)] == self.cells[str(5)]:
            c = True
        if a and b and c:
            self.cells[str(5)] = self.pc
            return True

        a = False
        b = False
        c = False
        if self.cells[str(3)] == self.pc:
            a = True
        if self.cells[str(5)] == empty:
            b = True
        if self.cells[str(5)] == self.cells[str(7)]:
            c = True
        if a and b and c:
            self.cells[str(5)] = self.pc
            return True

        a = False
        b = False
        c = False
        if self.cells[str(5)] == self.pc:
            a = True
        if self.cells[str(3)] == empty:
            b = True
        if self.cells[str(3)] == self.cells[str(7)]:
            c = True
        if a and b and c:
            self.cells[str(3)] = self.pc
            return True

        a = False
        b = False
        c = False
        if self.cells[str(7)] == self.pc:
            a = True
        if self.cells[str(3)] == empty:
            b = True
        if self.cells[str(3)] == self.cells[str(5)]:
            c = True
        if a and b and c:
            self.cells[str(5)] = self.pc
            return True

    def left_overs(self):
        if self.cells[str(1)] == empty:
            self.cells[str(1)] = self.pc
        elif self.cells[str(3)] == empty:
            self.cells[str(3)] = self.pc
        elif self.cells[str(7)] == empty:
            self.cells[str(7)] = self.pc
        elif self.cells[str(9)] == empty:
            self.cells[str(9)] = self.pc
        elif self.cells[str(5)] == empty:
            self.cells[str(5)] = self.pc
        elif self.cells[str(2)] == empty:
            self.cells[str(2)] = self.pc
        elif self.cells[str(4)] == empty:
            self.cells[str(4)] = self.pc
        elif self.cells[str(6)] == empty:
            self.cells[str(6)] = self.pc
        elif self.cells[str(8)] == empty:
            self.cells[str(8)] = self.pc

    def render(self, extra=''):
        os.system('clear')
        print(self.logo)
        if hasattr(self, 'choice'):
            self.make_board()
            print(self.board)

    def flow(self):
        index = 0
        while not self.winner and not self.reset:
            self.render()
            if index % 2 == 0:
                self.make_choice()
            else:
                self.computer_choice()
            if self.check_winner():
                break
            if self.check_reset():
                break
            index += 1
        self.render()
        self.end_of_game()

    def check_winner(self):
        for i in range(1, 8, 3):
            if self.cells[str(i)] == self.cells[str(i + 1)]:
                if self.cells[str(i)] == self.cells[str(i + 2)]:
                    if self.cells[str(i)] != empty:
                        return self.set_winner(i)

        for i in range(1, 4):
            if self.cells[str(i)] == self.cells[str(i + 3)] == self.cells[str(i + 6)] != empty:
                return self.set_winner(i)

        if self.cells[str(1)] == self.cells[str(5)] == self.cells[str(9)] != empty:
            return self.set_winner(1)

        if self.cells[str(3)] == self.cells[str(5)] == self.cells[str(7)] != empty:
            return self.set_winner(3)

    def check_reset(self):
        all_full = bool(all([False if cell == empty else cell for i, cell in self.cells.items()]))
        if all_full:
            self.reset = True
            return True

    def set_winner(self, value):
        if self.cells[str(value)] == self.choice:
            self.winner = 'You'
        elif self.cells[str(value)] == self.pc:
            self.winner = 'The Pc'

    def end_of_game(self):
        print(self.reset, self.winner)
        if self.reset:
            print('You had a tie.')
            self.reset_game()

        elif self.winner:
            if self.winner == 'You':
                print('Congratulations!! You won the game!')
            else:
                print('Better luck next time. You lost the game.')
            self.reset_game()

    def reset_game(self):
        response = ''
        while not response or not bool(re.search('^[yYnN]', response)):
            if len(response):
                print('That was an invalid option.')
            response = input('Would you like to play again?')
        if bool(re.search('^[yY]', response)):
            for i, cell in self.cells.items():
                self.cells[str(i)] = empty
            self.choice = None
            self.winner = None
            self.reset = False
            return self.play()
        if bool(re.search('^[nN]', response)):
            print('Goodbye...')

    def make_board(self):
        self.board = f'''
             1            |2            |3
                          |             |
              {self.cells['1'][0]} | {self.cells['2'][0]} | {self.cells['3'][0]}
              {self.cells['1'][1]} | {self.cells['2'][1]} | {self.cells['3'][1]}
              {self.cells['1'][2]} | {self.cells['2'][2]} | {self.cells['3'][2]}
              {self.cells['1'][3]} | {self.cells['2'][3]} | {self.cells['3'][3]}
              {self.cells['1'][4]} | {self.cells['2'][4]} | {self.cells['3'][4]}
             _____________|_____________|_______________
             4            |5            |6
                          |             |
              {self.cells['4'][0]} | {self.cells['5'][0]} | {self.cells['6'][0]}
              {self.cells['4'][1]} | {self.cells['5'][1]} | {self.cells['6'][1]}
              {self.cells['4'][2]} | {self.cells['5'][2]} | {self.cells['6'][2]}
              {self.cells['4'][3]} | {self.cells['5'][3]} | {self.cells['6'][3]}
              {self.cells['4'][4]} | {self.cells['5'][4]} | {self.cells['6'][4]}
             _____________|_____________|_______________
             7            |8            |9
                          |             |
              {self.cells['7'][0]} | {self.cells['8'][0]} | {self.cells['9'][0]}
              {self.cells['7'][1]} | {self.cells['8'][1]} | {self.cells['9'][1]}
              {self.cells['7'][2]} | {self.cells['8'][2]} | {self.cells['9'][2]}
              {self.cells['7'][3]} | {self.cells['8'][3]} | {self.cells['9'][3]}
              {self.cells['7'][4]} | {self.cells['8'][4]} | {self.cells['9'][4]}
                          |             |
        '''

tictactoe = Game(board, cells, ascii.ex_mark, ascii.circle, ascii.logo)
