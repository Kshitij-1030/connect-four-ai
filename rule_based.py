import math
import random
import numpy as np
from game import GameBoard

# Constants
PLAYER = 1   # Human player
AI = -1      # AI agent
EMPTY = 0

# Scoring constants
FOUR_IN_A_ROW_SCORE = 100
THREE_IN_A_ROW_SCORE = 10
TWO_IN_A_ROW_SCORE = 5
BLOCK_OPPONENT_THREE_SCORE = -80
CENTER_COLUMN_SCORE = 3

def evaluate_window(window: list[int], player: int) -> int:
    """
    Evaluate a window of 4 cells and assign a score for the given player.
    
    Args:
        window: List of 4 integers representing a potential connect-four line.
        player: The player for whom to evaluate (1 for Human, -1 for AI).
    
    Returns:
        Integer score representing advantage in the window.
    """
    score = 0
    opponent = PLAYER if player == AI else AI

    if window.count(player) == 4:
        score += FOUR_IN_A_ROW_SCORE
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += THREE_IN_A_ROW_SCORE
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += TWO_IN_A_ROW_SCORE

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score += BLOCK_OPPONENT_THREE_SCORE

    return score

def score_position(board: GameBoard, player: int) -> int:
    """
    Calculate the score of the board for the given player.
    
    Args:
        board: GameBoard object.
        player: The player (1 or -1).
    
    Returns:
        Integer score evaluating the current board state.
    """
    grid = board.grid
    score = 0

    # Center preference
    center_col = list(grid[:, board.cols // 2])
    score += center_col.count(player) * CENTER_COLUMN_SCORE

    # Horizontal
    for row in range(board.rows):
        for col in range(board.cols - 3):
            window = list(grid[row, col:col+4])
            score += evaluate_window(window, player)

    # Vertical
    for col in range(board.cols):
        for row in range(board.rows - 3):
            window = list(grid[row:row+4, col])
            score += evaluate_window(window, player)

    # Positive diagonal
    for row in range(board.rows - 3):
        for col in range(board.cols - 3):
            window = [grid[row+i][col+i] for i in range(4)]
            score += evaluate_window(window, player)

    # Negative diagonal
    for row in range(3, board.rows):
        for col in range(board.cols - 3):
            window = [grid[row-i][col+i] for i in range(4)]
            score += evaluate_window(window, player)

    return score

def minimax(board: GameBoard, depth: int, alpha: float, beta: float, is_maximizing: bool) -> tuple[int | None, int]:
    """
    Run Minimax algorithm with alpha-beta pruning.
    
    Args:
        board: Current GameBoard object.
        depth: Maximum depth of recursion.
        alpha: Alpha value for pruning.
        beta: Beta value for pruning.
        is_maximizing: True if maximizing player (AI), False if minimizing (Human).
    
    Returns:
        Tuple containing best column and corresponding score.
    """
    valid_moves = board.get_valid_moves()
    is_terminal = board.check_winner(PLAYER) or board.check_winner(AI) or len(valid_moves) == 0

    if depth == 0 or is_terminal:
        if is_terminal:
            if board.check_winner(AI):
                return None, 1000000000
            elif board.check_winner(PLAYER):
                return None, -1000000000
            else:
                return None, 0
        return None, score_position(board, AI)

    best_col = random.choice(valid_moves)

    if is_maximizing:
        max_score = -math.inf
        for col in valid_moves:
            temp = board.copy()
            temp.drop_piece(col, AI)
            _, score = minimax(temp, depth-1, alpha, beta, False)
            if score > max_score:
                max_score, best_col = score, col
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break
        return best_col, max_score
    else:
        min_score = math.inf
        for col in valid_moves:
            temp = board.copy()
            temp.drop_piece(col, PLAYER)
            _, score = minimax(temp, depth-1, alpha, beta, True)
            if score < min_score:
                min_score, best_col = score, col
            beta = min(beta, min_score)
            if alpha >= beta:
                break
        return best_col, min_score

def minimax_ai(board_grid: np.ndarray, depth: int = 4) -> int:
    """
    Wrapper to use Minimax AI from a board grid.

    Args:
        board_grid: 2D numpy array representing the current board state.
        depth: Maximum search depth for the AI.

    Returns:
        Column number selected by AI.
    """
    board = GameBoard()
    board.grid = np.copy(board_grid)
    col, _ = minimax(board, depth, -math.inf, math.inf, True)
    return col