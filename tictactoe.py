import math
import copy

# defining variables
X = "X"
O = "O"
EMPTY = None

# implementing functions
# initial_state initializes the board
def initial_state():
    temp = [[None, None, None],
            [None, None, None],
            [None, None, None]]
    return temp

# player returns whose turn next is i.e. X or O
def player(board):
    num_empty = 0
    for x in board:
        for mark in x:
            if mark is None:
                num_empty += 1

    if num_empty%2==0:
        return O
    else:
        return X

# actions gives the available valid moves that can be played
def actions(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                moves.append((i,j))

    if not moves:
        return 0
    else:
        return moves

# result gives the board state after a given move is played
def result(board, move):
    if board[move[0]][move[1]] is not None:
        raise ValueError('Invalid move played.')
    else:
        updatedBoard = copy.deepcopy(board)
        updatedBoard[move[0]][move[1]] = player(board)
        return updatedBoard

# winner returns the winner of the game after terminal is true i.e game is over. If its a tie, it returns none
def winner(board):
    # game_won = False
    possible_wins = []
    col1 = []
    col2 = []
    col3 = []
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[2][0], board[1][1], board[0][2]]

    for row in board:
        possible_wins.append(row)
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])

    possible_wins.append(col1)
    possible_wins.append(col2)
    possible_wins.append(col3)
    possible_wins.append(diag1)
    possible_wins.append(diag2)

    X_wins = [X]*3
    O_wins = [O]*3

    for comb in possible_wins:
        if comb == X_wins:
            return X
        elif comb == O_wins:
            return O

    return None

# terminal returns a bool indicating if game is over or not
def terminal(board):
    if winner(board) is not None:
        return True
    elif actions(board) == 0:
        return True
    else:
        return False

# utility returns the evalution score after the game is over
def utility(board):
    if winner(board)==X:
        return 10
    elif winner(board)==O:
        return -10
    else:
        return 0

# eval_move returns the score of a board position
# minimax along with alpha beta pruning is used here
def eval_move(board, alpha, beta):

    if terminal(board):
        return utility(board)
    else:
        if player(board)==X:
            best_score = -math.inf
            for action in actions(board):
                score = eval_move(result(board, action), alpha, beta)
                best_score = max(best_score, score)
                alpha= max(alpha, best_score)
                if beta<=alpha:
                    break

            return best_score
        else:
            best_score = math.inf
            for action in actions(board):
                score = eval_move(result(board, action), alpha, beta)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta<=alpha:
                    break

            return best_score


# eval_pos returns the scores/utilities of all the possible moves that can be played at a given board state
def eval_pos(board):
    if terminal(board):
        return None
    else:

        scores = []

        for move in actions(board):
            alpha, beta = -math.inf, math.inf
            scores.append(eval_move(result(board, move), alpha, beta))

        return scores

# minimax returns the best move that can be played at a given board state
def minimax(board):
    if terminal(board):
        return None
    else:
        moves_scores = eval_pos(board)
        if player(board)==X:
            # maxEval = -math.inf
            move_idx = moves_scores.index(max(moves_scores))
        else:
            move_idx = moves_scores.index(min(moves_scores))

        return actions(board)[move_idx]

















