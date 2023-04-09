import chess
import chess.pgn
import torch
import torch.nn as nn

class ChessCNN(nn.Module):
    def __init__(self):
        super(ChessCNN, self).__init__()
        self.conv1 = nn.Conv2d(12, 64, 3, padding=1)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(64, 64, 3, padding=1)
        self.fc1 = nn.Linear(64 * 8 * 8, 256)
        self.fc2 = nn.Linear(256, 1)

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = x.view(-1, 64 * 8 * 8)
        x = self.relu(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        return x


def board_to_tensor(board):
    pieces = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]
    tensor = torch.zeros(12, 8, 8)

    for idx, piece in enumerate(pieces):
        for square in board.pieces(piece, chess.WHITE):
            row, col = divmod(square, 8)
            tensor[idx, row, col] = 1
        for square in board.pieces(piece, chess.BLACK):
            row, col = divmod(square, 8)
            tensor[idx + 6, row, col] = 1
            
    return tensor