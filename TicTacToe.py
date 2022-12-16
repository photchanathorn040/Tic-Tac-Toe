#Tic-Tac-Toe Game
#By Photchanathorn Prombun (พจนธร พรหมบุญ)

#Create board pattarn and show board
def show_board(board):
  print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
  print(f'---+---+---')
  print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
  print(f'---+---+---')
  print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')

#Get XO position from player
#Get two input value for row and column number
def move(player):
  print(f'{player} turn')
  getrow = int(input("Please enter a row number (1-3): "))
  while getrow not in [1,2,3]: #Check the row number
    print("Your entered the wrong number")
    getrow = int(input("Please enter a row number (1-3): "))
  getcol = int(input("Please enter a column number (1-3): "))
  while getcol not in [1,2,3]: #Check the col number
    print("Your entered the wrong number")
    getrow = int(input("Please enter a column number (1-3): "))
  return [getrow, getcol] #Return a list of row/col number

def wcol(board): #Check col win combo
  if board[0][0]==board[1][0]==board[2][0]!=" " or \
  board[1][0]==board[1][1]==board[2][1]!=" " or \
  board[2][0]==board[1][2]==board[2][2]!=" ":
    return True
  else:
    return False

def wrow(board): #Check row win combo
  if board[0][0]==board[0][1]==board[0][2]!=" " or \
  board[1][0]==board[1][1]==board[1][2]!=" " or \
  board[2][0]==board[2][1]==board[2][2]!=" ":
    return True
  else:
    return False

def wdiag(board): #Check diagonal win combo
  if board[0][0]==board[1][1]==board[2][2]!=" " or \
  board[0][2]==board[1][1]==board[2][0]!=" ":
    return True
  else:
    return False
    
def main():
  print("Welcome to Tic-Tac-Toe")
  print("Player X will play first")
  print("Please enter a number of row and column")
  turn = 'X' #Start with player X
  #create blank 2D-list
  board = [[" " for x in range(3)] for y in range(3)]
  count = 0 #count turn number
  show_board(board) #show current board
  loop = True
  while loop:
    pos = move(turn)
    while board[pos[0]-1][pos[1]-1] in ["X", "O"]: #Check available position
      print("This position is occupied")
      print("Please enter new row and column number")
      pos = move(turn)
    board[pos[0]-1][pos[1]-1] = turn
    count+=1
    show_board(board)
    if wrow(board) or wcol(board) or wdiag(board): #Check winning position
      print(f'Player {turn} Win!')
      print("Game Over")
      loop = False
    else:
    #Change player
      if turn == 'X':
        turn = "O"
      else:
        turn = "X"

    if count == 9: #if reaching turn 9 and no position left
      print("Game Over!")
      print("No WINNER in this game")
      loop = False

main()
