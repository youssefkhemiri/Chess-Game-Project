from stockfish import Stockfish

stockfish = Stockfish(path="stockfish/stockfish-windows-x86-64-avx2.exe", parameters={"Threads": 2, "Minimum Thinking Time": 30})

stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

print("Welcome to Chess! You're playing as White.")
print("Enter moves in algebraic notation (e.g., 'e2e4', 'd2d4'). Type 'quit' to exit.\n")

while True:
    
    print("Current Board Position:")
    print(stockfish.get_board_visual())
    
    
    user_move = input("Your move: ").strip()
    
    if user_move.lower() == "quit":
        print("Game exited.")
        break

    # Check if user's move is valid
    if stockfish.is_move_correct(user_move):
        # Make user's move
        stockfish.make_moves_from_current_position([user_move])
    else:
        print("Invalid move. Please try again.")
        continue

   
    stockfish_move = stockfish.get_best_move()
    
    # Check if Stockfish has a legal move, otherwise declare victory
    if stockfish_move is None:
        print("Checkmate! You've won the game!")
        break
    
    stockfish.make_moves_from_current_position([stockfish_move])
    
    print(f"Stockfish's move: {stockfish_move}\n")
    
    # Check for game end condition
    if stockfish.get_evaluation()['type'] == 'mate':
        print("Checkmate! Stockfish has won the game.")
        break
