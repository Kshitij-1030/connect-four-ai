import tkinter as tk
from game import GameBoard
from rule_based import minimax_ai

CELL_SIZE = 80
ROWS = 6
COLS = 7

class ConnectFourGUI:
    """
    Graphical user interface for Connect Four using Tkinter.
    
    Attributes:
        root (tk.Tk): The root window.
        board (GameBoard): The game board instance.
        current_player (int): Whose turn it is (1 = human, -1 = AI).
        canvas (tk.Canvas): Canvas for drawing the board.
    """
    def __init__(self, root: tk.Tk):
        """
        Initialize the GUI and game state.

        Args:
            root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Connect Four")
        self.board = GameBoard()
        self.current_player = 1  # Human starts first
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="blue")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_event)
        self.draw_board()

    def draw_board(self) -> None:
        """
        Draw the Connect Four board with all current pieces.
        """
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x0 = c * CELL_SIZE + 10
                y0 = r * CELL_SIZE + 10
                x1 = (c + 1) * CELL_SIZE - 10
                y1 = (r + 1) * CELL_SIZE - 10
                value = self.board.grid[r][c]
                color = "white"
                if value == 1:
                    color = "red"     # Human player
                elif value == -1:
                    color = "yellow"  # AI player
                self.canvas.create_oval(x0, y0, x1, y1, fill=color)

    def click_event(self, event: tk.Event) -> None:
        """
        Handle user click, play human move, then AI response.
        
        Args:
            event: The Tkinter event object containing the click coordinates.
        """
        col = event.x // CELL_SIZE
        if self.board.is_valid_move(col):
            self.board.drop_piece(col, 1)  # Human move
            self.draw_board()

            if self.board.check_winner(1):
                self.display_winner("Player wins!")
                return

        # AI move
        ai_col = minimax_ai(self.board.grid, depth=4)
        if self.board.is_valid_move(ai_col):
            self.board.drop_piece(ai_col, -1)
            self.draw_board()

            if self.board.check_winner(-1):
                self.display_winner("AI wins!")
                return

        # Check for draw
        if len(self.board.get_valid_moves()) == 0:
            self.display_winner("It's a draw!")

    def display_winner(self, message: str) -> None:
        """
        Display a popup window showing the game result.
        
        Args:
            message: The result message to display.
        """
        win_window = tk.Toplevel()
        win_window.title("Game Over")
        label = tk.Label(win_window, text=message, font=("Arial", 20))
        label.pack(pady=20)
        button = tk.Button(win_window, text="OK", command=self.root.quit)
        button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConnectFourGUI(root)
    root.mainloop()