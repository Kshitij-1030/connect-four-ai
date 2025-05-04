import numpy as np

class GameBoard:
    """
    Represents the Connect Four game board and its operations.
    
    Attributes:
        rows (int): Number of rows in the board.
        cols (int): Number of columns in the board.
        grid (np.ndarray): 2D array representing the board state.
                        0 = empty, 1 = player, -1 = AI
    """
    def __init__(self):
        """Initialize an empty 6x7 game board."""
        self.rows: int = 6
        self.cols: int = 7
        self.grid: np.ndarray = np.zeros((self.rows, self.cols), dtype=int)

    def is_valid_move(self, col: int) -> bool:
        """
        Check if a column is a valid move (i.e., not full).
        
        Args:
            col: Column index to check.
        
        Returns:
            True if move is valid, False otherwise.
        """
        return self.grid[0][col] == 0

    def get_valid_moves(self) -> list[int]:
        """
        Get a list of valid columns where a move can be made.
        
        Returns:
            List of column indices with at least one empty cell.
        """
        return [c for c in range(self.cols) if self.is_valid_move(c)]

    def drop_piece(self, col: int, player: int) -> bool:
        """
        Drop a piece into the specified column for the given player.
        
        Args:
            col: Column index where the piece should be dropped.
            player: The player (1 for Human, -1 for AI).
        
        Returns:
            True if piece was successfully dropped, False if column is full.
        """
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return True
        return False

    def check_winner(self, player: int) -> bool:
        """
        Check if the given player has won the game.
        
        Args:
            player: Player ID (1 or -1).
        
        Returns:
            True if the player has four in a row.
        """
        # Horizontal check
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row, col + i] == player for i in range(4)):
                    return True

        # Vertical check
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.grid[row + i, col] == player for i in range(4)):
                    return True

        # Positive diagonal check
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.grid[row + i, col + i] == player for i in range(4)):
                    return True

        # Negative diagonal check
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row - i, col + i] == player for i in range(4)):
                    return True

        return False

    def print_board(self) -> None:
        """
        Print the board with the bottom row at the bottom (for human readability).
        """
        print(np.flip(self.grid, 0))

    def copy(self) -> "GameBoard":
        """
        Create a deep copy of the game board.
        
        Returns:
            A new GameBoard object with the same grid state.
        """
        new_board = GameBoard()
        new_board.grid = np.copy(self.grid)
        return new_board
