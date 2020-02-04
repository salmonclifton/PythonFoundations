WAYS_TO_WIN = ((0, 1, 2),
               (3, 4, 5),
               (6, 7, 8),
               (0, 3, 6),
               (1, 4, 7),
               (2, 5, 8),
               (0, 4, 8),
               (2, 4, 6))

for row in WAYS_TO_WIN:
   print (row[0], row[1], row[2])
   print(row)


"""
    if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
        winner = board[row[0]]
        return winner """