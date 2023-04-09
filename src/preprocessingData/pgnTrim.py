import os

# The directory containing the subdirectories with PGN files
parent_dir = "D:\Downloads\Flank_Unorthodox"

# Loop through each subdirectory
for subdir in os.listdir(parent_dir):
    subdir_path = os.path.join(parent_dir, subdir)

    # Loop through each PGN file in the subdirectory
    for pgn_file in os.listdir(subdir_path):
        if pgn_file.endswith(".pgn"):
            pgn_path = os.path.join(subdir_path, pgn_file)

            # Open the PGN file and read its contents
            with open(pgn_path) as f:
                pgn_data = f.read()

            # Split the contents of the file into individual games
            games = pgn_data.split("\n\n")

            # Only keep the last 200 games
            last_500_games = games[-500:]

            # Update the PGN file to only include the last 200 games
            with open(pgn_path, "w") as f:
                f.write("\n\n".join(last_500_games))

            # Delete the games that are not in the last 200
            with open(pgn_path, "r+") as f:
                f.seek(0)
                f.write("\n\n".join(last_500_games))
                f.truncate()