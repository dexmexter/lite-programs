from random import randint

# In the board the index lists rows first.
board = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]]

for x in range(3):
  board.append(["~"] * 3)

col_convert = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6
, "H": 7, "I": 8, "J": 9
}

def print_board(board):
  row_number = 0
  for row in board:
    if row_number < 10:
      print(" " + str(row_number) + " " + " ".join(row))
      row_number += 1
    else:
      print(str(row_number)+ " " + " ".join(row))
      row_number += 1

print_board(board)

def random_col(board):
  return randint(0, len(board[1]) - 1) # A is col 0
def random_row(board):
  return randint(1, len(board) - 1) # letters are col 0 so this must begin at row 1

ships = {}
def make_ships(n):
  ships_list = []
  for i in range(n):
    new_ship = [random_col(board), random_row(board)]
    
    if new_ship in ships_list:
      return make_ships(n)
    else:
      ships_list.append(new_ship)

  for i in range(n):  
    ships[i] = ships_list[i]

make_ships(3)

def show_ships():
  for i in ships:
    print("Ship: " + str(i))
    print(board[0][ships[i][0]])
    print(ships[i][1])

lives = 5
ships_guessed = 0
show_ships()

while lives > 0:
  while True:
    try:
      guess_col = col_convert[input("Guess Col: ").upper()]
    except KeyError:
      print('\nYour guess does not work, try putting one of the column letters')
      continue
    break
  
  while True:
    try:
      guess_row = int(input("Guess Row: "))
    except ValueError:
      print('\nThat does not work, try putting a number')
      continue
    break

  guess = [guess_col, guess_row]

  show_ships()
  #print_board(board)

  if (guess_row < 1 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
    print("Oops, that's not even in the ocean.")

  elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "!":
    print("You guessed that one already.")

  elif guess in ships.values():
    print("Congratulations! You sunk one of my ships!")
    board[guess_row][guess_col] = "!"
    ships_guessed += 1
    print_board(board)
  
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    lives -= 1
    print_board(board)

  if len(ships) == ships_guessed:
    print("You won! You sunk all of my ships!")
    break
    
  print("You've found %d out of %d ships" %(ships_guessed, len(ships)))
  print("You have " + str(lives) + " lives left")

if lives == 0:
  print("Sorry, you lost.")

print("Play again?")

#TODO: Rewrite to work with other games
#TODO: Create ship class
#TODO: Create ships with different sizes and names
#TODO: Carrier: 5 Battleship: 4 Cruiser: 3 Submarine: 3 Destroyer: 2