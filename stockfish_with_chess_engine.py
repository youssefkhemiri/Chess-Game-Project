import chess
import chess.engine

class PlayAgainstStockfish:
    def __init__(self, stockfish_path, skill_level=10):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        self.engine.configure({"Skill Level": skill_level})  # Set the engine's skill level

    def display_board(self):
        """Display the current board."""
        print(self.board)

    def get_user_move(self):
        """Prompt the user for a move in UCI format."""
        while True:
            move_input = input("Your move (in UCI format, e.g., e2e4): ").strip()
            try:
                move = chess.Move.from_uci(move_input)
                if move in self.board.legal_moves:
                    return move
                else:
                    print("Illegal move. Please try again.")
            except ValueError:
                print("Invalid format. Use UCI notation, e.g., 'e2e4'.")

    def play_game(self):
        """Play a game against Stockfish."""
        print("Starting a new game against Stockfish!")
        print("You are playing as White.")

        while not self.board.is_game_over():
            # Display board
            self.display_board()

            # Player's move
            user_move = self.get_user_move()
            self.board.push(user_move)

            # Check if game ended after the user's move
            if self.board.is_game_over():
                break

            # Stockfish's move
            print("\nStockfish is thinking...")
            stockfish_move = self.engine.play(self.board, chess.engine.Limit(time=1.0)).move
            self.board.push(stockfish_move)
            print(f"Stockfish plays: {stockfish_move}\n")

        # Game over, print the result
        self.display_board()
        result = self.board.result()
        print(f"Game over! Result: {result}")

    def close_engine(self):
        """Close the Stockfish engine."""
        self.engine.quit()

# Set the path to your Stockfish executable
stockfish_path = "stockfish/stockfish-windows-x86-64-avx2.exe"
game = PlayAgainstStockfish(stockfish_path, skill_level=10)
game.play_game()
game.close_engine()
