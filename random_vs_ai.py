import csv
import random
from typing import Tuple, Union
from game import GameBoard
from rule_based import minimax_ai

NUM_GAMES = 1000       # Number of games to simulate
DEPTH = 3              # AI difficulty level
OUTPUT_FILE = "random_vs_ai.csv"

def play_game() -> Tuple[Union[int, str], list[Tuple[int, int, list[int]]]]:
    """
    Simulate one game between a random player (player 1) and an AI (player -1).
    
    Returns:
        A tuple containing:
            - The winner (1, -1, or 'draw')
            - A list of tuples representing each move: (player, column, board_state_before_move)
    """
    board = GameBoard()
    current_player = 1  # Random player starts
    move_history: list[Tuple[int, int, list[int]]] = []

    while True:
        valid_moves = board.get_valid_moves()

        if not valid_moves:
            return "draw", move_history

        # Capture board state before move
        board_state_before_move = board.grid.flatten().tolist()

        if current_player == 1:
            move = random.choice(valid_moves)
        else:
            move = minimax_ai(board.grid, depth=DEPTH)

        board.drop_piece(move, current_player)
        move_history.append((current_player, move, board_state_before_move))

        if board.check_winner(current_player):
            return current_player, move_history

        current_player *= -1  # Switch turn

def simulate_games(num_games: int = NUM_GAMES, filename: str = OUTPUT_FILE) -> None:
    """
    Simulate multiple games between a random player and the AI, and save the results to a CSV file.

    Args:
        num_games: Number of games to simulate.
        filename: Name of the output CSV file.
    """
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Game", "Winner", "Move_Num", "Player", "Move", "Board_State"])

        for game_id in range(1, num_games + 1):
            winner, moves = play_game()
            for move_num, (player, move, board_state) in enumerate(moves, 1):
                writer.writerow([game_id, winner, move_num, player, move, board_state])

if __name__ == "__main__":
    simulate_games()