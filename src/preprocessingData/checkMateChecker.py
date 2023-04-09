import chess.pgn

# Open the PGN file
with open("D:\Documents\LichessDatabase\lichess_db_standard_rated_2013-04.pgn") as pgn_file:
    # Loop through all the games in the PGN file
    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break
        
        # Check if the game ended with a checkmate
        end = game.end()
        if end is not None and end.board().is_checkmate():
            # If the game ended with a checkmate, keep it
            with open("D:\Desktop\ChessCheckMateDatabase\Checkmates4.pgn", "a") as output_file:
                output_file.write(str(game) + "\n\n")