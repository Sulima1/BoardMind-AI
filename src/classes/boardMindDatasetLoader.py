import chess
import chess.pgn
from torch.utils.data import Dataset
from classes.boardMindCNN import board_to_tensor

class ChessPositionDataset(Dataset):
    def __init__(self):
        pass

    def load_pgn_files(self, pgn_files, chunk_size):
        for pgn_file in pgn_files:
            with open(pgn_file) as f:
                chunk_positions = []
                chunk_targets = []
                while True:
                    game = chess.pgn.read_game(f)
                    if game is None:
                        break
                    self._extract_positions_and_targets(game, chunk_positions, chunk_targets)
                    if len(chunk_positions) >= chunk_size:
                        yield chunk_positions[:chunk_size], chunk_targets[:chunk_size]
                        chunk_positions = chunk_positions[chunk_size:]
                        chunk_targets = chunk_targets[chunk_size:]

                if chunk_positions:
                    yield chunk_positions, chunk_targets

    def _extract_positions_and_targets(self, game, positions, targets):
        board = game.board()
        result = self._convert_result_to_value(game.headers["Result"])

        for move in game.mainline_moves():
            board.push(move)
            tensor = board_to_tensor(board)
            positions.append(tensor)
            targets.append(result)

    @staticmethod
    def _convert_result_to_value(result):
        if result == "1-0":
            return 1
        elif result == "0-1":
            return -1
        else:
            return 0