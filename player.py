import math
import random

class Player:
    def __init__(self,letter):
        #letter - x si 0
        self.letter = letter

    #urmatoarea miscare
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +'\'s turn. Input move(0-8):')
            #vom verifica daca e o valoare corecta incercand sa o atribuim unui integer
            #daca nu e, vom spue ca e invalid
            #daca patratul respectiv nu e dispobinil in tabel, la fel vom spuna ca este invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Loc indisponibil. Incearca din nou. ')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #alegem prin random
        else:
            #patratul ales in functie de algoritmul minimax
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter #eu
        other_player = 'O' if player =='X' else 'X' #celalaltu jucator

        #prima data, verificam daca miscarea awnterioara este castigatoare
        #acesta este caul de baza
        if state.current_winner == other_player:
            #trebuie sa intoarcem pozitia si scorul deoarece trebuie sa urmarim scorul
            #pentru ca algoritmul minimax sa functioneze
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }

        elif not state.num_empty_squares(): #nici un patrat ramas gol
            return {'position': None, 'score': 0}

        #initializam dictionarele
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #fiecare scor trebuiesa se mareasca
        else:
            best = {'position': None, 'score': math.inf} #fiecare scor trebuie sa se miscoreze

        for possible_move in state.available_moves():
            # se face o micare, se incearca spotul respectiv
            state.make_move(possible_move, player)
            # se apeleaza minimax pentru a simula un joc dupa efectuarea miscarii
            sim_score = self.minimax(state, other_player) # alternam jucatorii
            # se reface miscarea
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #altfel se va incurca in recursiune
            #se actualizeaza dictionarele daca este necesar
            if player ==max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score #inlocuim 'best'
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best