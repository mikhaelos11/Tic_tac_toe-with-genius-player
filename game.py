from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # utilizam o singura lista pentru a reprezenta un tabel 3x3
        self.current_winner = None  # pentru a sti cine este castigatorul

    def print_board(self):
        # construim randurile
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (ne spune ce numar corespunde fiecarui patrat)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        '''
        moves = []
        for(i, x) in enumerate(self.board):
            #['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
        '''

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # daca miscarea e valida, se executa(asignam literei un patrat)
        # apoi returnam true. daca este invalid, returnam false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # castiga pentru 3 elemente intr-un rand din tabel. trebuie sa le verificam pe toate
        # prima data verificam randurile
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # verificam coloanele
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # verificam diagonalele
        # doar daca patratul are indicele un numar par(0, 2, 4, 6, 8)
        # acestea sunt singurele miscari posibile pentru a castiga pe diagonala
        if square % 2 == 0:
            diagonala1 = [self.board[i] for i in [0, 4, 8]]  # diagonala principala
            if all([spot == letter for spot in diagonala1]):
                return True
            diagonala2 = [self.board[i] for i in [2, 4, 6]]  # diagonala secundara
            if all([spot == letter for spot in diagonala2]):
                return True
        # daca nici o verificare nu intoarce true
        return False

def play(game, x_player, o_player, print_game=True):
    # intoarce castigatorul jocului, sau None pentru egal
    if print_game:
        game.print_board_nums()
    letter = 'X'  # litera de inceput
    # itereaza cat time jocul are patrate libere
    # castigatorul va fi playerul care iese din bucla
    while game.empty_squares():
        # primeste miscarea de la cel mai apropiat jucator
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ')  # pentru a lasa un rand gol

            if game.current_winner:
                if print_game:
                    print(letter + ' castiga!')
                return letter

            # dupa ce efectuam miscarea, trebuie sa alternam literele
            letter = 'O' if letter == 'X' else 'X'
        if print_game:
            time.sleep(0.8)

    if print_game:
        print(' Este egalitate!')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1):
        x_player = HumanPlayer('X')
        o_player = GeniusComputerPlayer('O')
        p = TicTacToe()
        result = play(p, x_player, o_player, print_game=True)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After - iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} ties')

    
    
    
