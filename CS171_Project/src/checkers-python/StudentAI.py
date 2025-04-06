from random import randint
from BoardClasses import Move
from BoardClasses import Board
from math import inf

class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = 2
        self.opponent = {1: 2, 2: 1}

    def get_move(self, move):
        if len(move) != 0:
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        best_move = moves[0][0]
        move = self.minMax( self.color, 3,  -999999999, best_move, 999999999, best_move)[1]
        #_, move = self.minMax(3, self.board, self.color)[1]

        self.board.make_move(move, self.color)
        return move

    def clone_board(self, original_board):
        new_board = Board(self.col, self.row, self.p)
        new_board.board = [row[:] for row in original_board.board]
        new_board.white_count = original_board.white_count
        new_board.black_count = original_board.black_count
        return new_board

    def minMax(self, player, depth, best_score, best_move, opponent_score, opponent_move):
        if depth == 0:
            return self.heuristic_evaluation(player), best_move

        moves = self.board.get_all_possible_moves(player)

        for move in moves:
            for sub_move in move:
                new_board = self.clone_board(self.board)
                new_board.make_move(sub_move, player)

                if player == self.color:
                    opponent_score, _ = self.minMax(self.opponent[self.color], depth - 1, best_score, best_move, opponent_score, opponent_move)
                    if best_score < opponent_score:
                        best_score = opponent_score
                        best_move = sub_move
                elif player == self.opponent[self.color]:
                    player_score, _ = self.minMax(self.color, depth - 1, best_score, best_move, opponent_score, opponent_move)
                    if opponent_score > best_score:
                        opponent_score = best_score
                        opponent_move = sub_move

                new_board.undo()
        return best_score, best_move


    def heuristic_evaluation(self, player):
        player_value = 0
        opponent_value = 0

        for col in range(self.col):
            for row in range(self.row):
                piece = self.board.board[col][row]
                if piece.get_color() == player:  
                    if piece.is_king:
                        player_value += 2
                    elif row < self.row // 2:  # Player's half of the board
                        player_value += 1.5
                    else:
                        player_value += 1
                elif piece.get_color() == self.opponent[player]:
                    if piece.is_king:
                        opponent_value += 2
                    elif row < self.row // 2:  # Opponent's half of the board
                        opponent_value += 1.5
                    else:
                        opponent_value += 1

        return player_value - opponent_value



if __name__ == "__main__":
    test = StudentAI(8, 8, 3)

    
