letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary using list comprehension and zip
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Add an entry for blank tile
letter_to_points[" "] = 0

def score_word(word):
    point_total = 0
    for letter in word:
        letter = letter.upper()  # Convert each letter to uppercase
        point_total += letter_to_points.get(letter, 0)  # Add point value, defaulting to 0
    return point_total

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word.upper())
    else:
        print(f"Player {player} not found.")

# Update player_to_words with a new word
play_word("player1", "QUIZ")

# Create an empty dictionary to store points for each player
player_to_points = {}

# Function to update the point totals
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

# Update the point totals
update_point_totals()

# Print the total points for each player
for player, points in player_to_points.items():
    print(f"{player} has {points} points")

# Print the final standings
print("Final standings:", player_to_points)
