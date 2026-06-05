def draw_board() :
    board = []
   
    for _ in range(3) :
        zeile = [" "," "," "]
        board.append(zeile)
    return board 


def board_druck (board):
    print("\n")
    for zeile in board :
        print ("|".join(zeile))
        print("-"*9)
    print("\n")



def check_if_valid(board,zeil,spalte) :

        if board[zeil][spalte]!=" " :

            print("Zell nicht frei !!!!, wähl andere Zeil und Spalte")
            return False
        return True
            





def check_win(board ,spieler) :

    # check zeilen für die current spieler

    for zeil in range(3) :
        
        if board[zeil][0] == board[zeil][1] == board[zeil][2] == spieler :
            return True
        
    # check spalten für die current spieler   

    for spalte in range(3) :
        if board[0][spalte] == board[1][spalte] == board[2][spalte] == spieler :
            return True
        
    
    # check Diagonal für die current spieler  
     
    if board[0][0] == board[1][1] ==board[2][2] or \
       board[0][2] == board[1][1] ==board[2][0] == spieler :
       return True
    
    return False
# 
def full_unenschieden(board) :
   
    return all(all(zell != " " for zell in zeil) for zeil in board)
