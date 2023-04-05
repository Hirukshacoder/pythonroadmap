


board = ["〰️", "〰️", "〰️",
         "〰️", "〰️", "〰️",
         "〰️", "〰️", "〰️"]


player = "❌"
winner = None 
gameon = True 

def get_board(board):
  print("{}❕{}❕{}".format(board[0], board[1], board[2]))
  print("➖➕➖➕➖")
  print("{}❕{}❕{}".format(board[3], board[4], board[5]))
  print("➖➕➖➕➖")
  print("{}❕{}❕{}".format(board[6], board[7], board[8]))


def playerinput(board):
  global player 
  
  pos = int(input("Enter a number between 1-9: "))
  if pos >= 1 and pos <= 9 and board[pos-1] == "〰️":
    board[pos-1] = player
  else:
    print("Player already landed there!")

def horizontal(board):
  global winner 
  
  if board[0] == board[1] == board[2] and board[0] != "〰️":
      winner = board[0]
      return True  
  elif board[3] == board[4] == board[5] and board[3] != "〰️":
      winner = board[3]
      return True  

      
  elif board[6] == board[7] == board[8] and board[6] != "〰️":
      winner = board[6]
      return True  

def vertical(board):
  global winner 
  
  if board[0] == board[3] == board[6] and board[0] != "〰️":
      winner = board[0]
      return True  
      
  elif board[1] == board[4] == board[7] and board[1] != "〰️":
    winner = board[1]
    return True  
      
  elif board[2] == board[5] == board[8] and board[2] != "〰️":
    winner = board[2]
    return True  

def diagonal(board):
  global winner 
  
  if board[0] == board[4] == board[8] and board[0] != "〰️":
    winner = board[0]
    return True  
      
  elif board[2] == board[4] == board[6] and board[2] != "〰️":
    winner = board[2]
    return True  

def tie(board):
  if "〰️" not in board:
    print("🧛 It's a tie!")
    get_board(board)
    gameon = False 

def win():
  global winner 
  
  if horizontal(board) or diagonal(board) or vertical(board):
    print("Winner is {}".format(winner))

def change_player():
  global player 
  
  if player == "❌":
    player = "⭕"
  else:
    player = "❌"

while gameon:
  
  get_board(board)
  playerinput(board)
  win()
  tie(board)
  change_player()