import chess
import chess.pgn
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import random
import os
from classes.boardMindCNN import ChessCNN, board_to_tensor
from classes.boardMindDatasetLoader import ChessPositionDataset
from concurrent.futures import ThreadPoolExecutor
import time
import tqdm

def evaluate(board, model):
    tensor = board_to_tensor(board)
    tensor = tensor.squeeze(1)
    value = model(tensor).item()
    return value

def run_simulation(board, depth, num_simulations, model):
    total_value = 0
    for _ in range(num_simulations):
        current_board = board.copy()
        current_depth = depth
        while not current_board.is_game_over() and current_depth > 0:
            legal_moves = list(current_board.legal_moves)
            index = random.randint(0, len(legal_moves) - 1)
            current_board.push(legal_moves[index])
            current_depth -= 1

        value = evaluate(current_board, model)
        total_value += value

    average_value = total_value / num_simulations
    return average_value

def mcts(board, depth, num_simulations, maximizing_player, model):
    best_move = None
    best_value = float('-inf') if maximizing_player else float('inf')
    unexplored_moves = list(board.legal_moves)

    with ThreadPoolExecutor() as executor:
        results = []
        for move in unexplored_moves:
            board.push(move)
            results.append(executor.submit(run_simulation, board.copy(), depth, num_simulations, model))
            board.pop()

        sorted_moves = [move for move, _ in sorted(zip(unexplored_moves, results), key=lambda x: x[1].result(), reverse=maximizing_player)]

        for move in sorted_moves:
            board.push(move)
            if board.is_checkmate():
                best_move = board.pop()
                return best_move
            value = run_simulation(board.copy(), depth, num_simulations, model)
            board.pop()

            if (maximizing_player and value > best_value) or (not maximizing_player and value < best_value):
                best_move = move
                best_value = value

    return best_move

def get_best_move(board, depth, num_simulations, model):
    maximizing_player = board.turn == chess.WHITE
    best_move = mcts(board, depth, num_simulations, maximizing_player, model)
    return best_move

def train_model(model, trainloader, num_epochs):
    model.train()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(num_epochs):
        running_loss = 0.0
        progress_bar = tqdm.tqdm(trainloader, desc=f"Epoch {epoch+1}/{num_epochs}")
        for inputs, targets in progress_bar:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets.float().unsqueeze(1))
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            progress_bar.set_postfix({"loss": f"{running_loss/len(progress_bar):.6f}"})

    print(f"Training completed.")

def main():
    start_time = time.time()
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'BoardMind.pt')
    model = ChessCNN()
    model.load_state_dict(torch.load(model_path))

    pgn_folder = pgn_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','data', 'external')
    pgn_files = [os.path.join(pgn_folder, file) for file in os.listdir(pgn_folder) if file.endswith(".pgn")]

    dataset = ChessPositionDataset()
    chunk_size = 9216
    num_epochs = 1

    ###
    #Uncomment the following lines to train the model
    #for positions, targets in dataset.load_pgn_files(pgn_files, chunk_size):
        #if not positions:
            #break
        #train_data = list(zip(positions, targets))
        #trainloader = DataLoader(train_data, batch_size=128, shuffle=True)
        #train_model(model, trainloader, num_epochs)
    #torch.save(model.state_dict(), model_path)
    ####

    elapsed_time = time.time() - start_time
    print(f"Dataset loading time: {elapsed_time} seconds")

    board = chess.Board()
    search_depth = 6
    num_simulations = 200

    print(board)

    model.eval()
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            user_move = input("Enter your move: ")
            try:
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Invalid move.")
            except ValueError:
                print("Invalid move format.")
        else:
            print("BoardMind is thinking...")
            best_move = get_best_move(board, search_depth, num_simulations, model)
            board.push(best_move)
            print(f"BoardMind plays: {best_move.uci()}")

        print(board)

    print("Game over.")

if __name__ == "__main__":
    main()
