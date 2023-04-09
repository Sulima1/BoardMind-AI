[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/YCTbQ0qx)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10625718&assignment_repo_type=AssignmentRepo)
Project Instructions
==============================

This repo contains the instructions for a machine learning project.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for describing highlights for using this ML project.
    ├── data
    │   └── external       <- Data from third party sources. (Chess game sample PGNs)
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │   └── README.md      <- Youtube Video Link
    │   └── final_project_report <- final report .pdf format and supporting files
    │   └── presentation   <-  final power point presentation 
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
       ├── classes           
       │   └── boardMindCNN.py <- Contains Convulutional Neural Network and tensor conversion
       |   └── boardMindDatasetLoader.py <- Dataloader constructed to load pgns, to be used in main
       │          
       ├── preprocessing data      <- Scripts help with pre-processing the data
       │   └── pgnTrim.py               <- Trims large PGN files into smaller sizes
       │   └── pgnMove.py               <- Helpful functions to move around PGN files
       │   └── checkMateChecker.py      <- Appends PGNs to another file containing valid games ending in checkmate
       │
       ├── models         <- Pytorch file containing the trained model
       │   └── BoardMind.pt
       │
       └── visualization  <- Python script to run the chess AI and play against as white against black
           └── main.py     

# BoardMind
A competitive chess engine created using deep learning techniques

created by 
Matthew Borkowski 201588010
Philip Virdo 201749430

# Required
- Built on Python ver. 3.10.10 64-bit

- chess ver. 1.9.4
- torch ver. 2.0.0

# Abstract
Our machine learning final project aims to design and develop a cutting-edge chess engine, BoardMind, which leverages machine learning techniques to play chess effectively. The primary objectives are to teach the engine chess intricacies and train it for high-level comprehension and skill. The methodology will involve deep learning and decision tree methods.

The project includes data collection, feature engineering, model development, training, evaluation, and iterative improvement. We will gather historical chess games, preprocess the data to extract relevant features, and explore deep learning architectures (CNNs and RNNs) alongside decision tree methods (Alpha-Beta pruning and MCTS). The model will be trained using supervised learning techniques and possibly reinforcement learning through self-play.

BoardMind's performance will be evaluated against existing chess engines and human players, using metrics like the ELO rating system, win-loss ratios, and game quality. Evaluation results will inform iterative refinements to improve the model's architecture, hyper parameters, and training data.

Upon completion, BoardMind is expected to be a sophisticated chess engine demonstrating high comprehension and skill in playing chess. This project will contribute to AI research in strategy games and provide valuable insights into machine learning algorithms' capabilities.

# How To Train the Model
In the main.py in the src folder, there is a section of commented code that when the comments are removed, will train the model on the next run. 

# How To Play
After running the main.py with the training lines commented out or after training a board will appear asking for you to enter a move.

The notation for moving pieces is based on a coordinate system where the x axis ranges from 'a' to 'h' and a y axis that ranges from 1 to 8. Entering a move starts with the current position of the piece you wish followed by the position you wish the peice to go to as long as that is a legal move or else you will be promoted to enter again. For special moves like castling, you must enter the king's current position and then its position after the castle, for example to castle king's side as white you must enter 'e1g1'. For promoting your pawns after they reach the end of the board you must enter the desired promotion piece in the move line, for example to promote a pawn to a queen you must enter 'e7e8q'. Below is an example of moving a pawn from position e2 to e4: 

And continue to play! Good Luck!
