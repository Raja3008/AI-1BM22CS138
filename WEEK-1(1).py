def print_board(board):
  for row in board:
    print("|".join(row))
    print("-"*5)

def check_winner(board):
  for i in range(3):
    if board[i][0]==board[i][1]==board[i][2]!=" ":
      return board[i][0]
    if board[0][i]==board[1][i]==board[2][i]!=" ":
      return board[0][i]

  if board[0][0]==board[1][1]==board[2][2] !=" ":
    return board[0][0]
  if board[0][2]==board[1][1]==board[2][0] !=" ":
    return board[0][2]

  return None

  def is_full(board):
    return all(cell !="" for row in board for cell in row )

  def tic_tac_toe():
    board=[]
    for _ in range(3):
      row=[]
      for _ in range(3):
        row.append("")
      board.append(row)

    current_player="X"
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, Enter the row (0-2): "))
        col = int(input(f"Player {current_player}, Enter the column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")


tic_tac_toe()