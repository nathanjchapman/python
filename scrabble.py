letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

letter_to_points = {l:p for l, p in zip(letters, points)}
letter_to_points[" "] = 0
player_to_points = {}

def score_word(word):
	point_total = 0
	for l in word:
		if l in letter_to_points:
			point_total += letter_to_points[l.upper()]
	return point_total

def update_point_total():
	for player, words in player_to_words.items():
		player_points = 0
		for word in words:
			player_points += score_word(word)
		player_to_points[player] = player_points

def play_word(player, word):
	player_to_words[player].append(word)
	update_point_total()


update_point_total()
print(player_to_points)

play_word("wordNerd", "sTop")
print(player_to_points)
