import csv

player = [
    {'player_name': 'Magnus Carlsen', 'fide_rating': 2870},
    {'player_name': 'Fabiano Caruana', 'fide_rating': 2822},
    {'player_name': 'Ding Liren', 'fide_rating': 2801}
]

print(player[0].keys())

with open('players.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=player[0].keys())
    writer.writeheader()
    writer.writerows(player)