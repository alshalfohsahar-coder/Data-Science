# Zeichnet das Spielbrett in der Konsole.

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


 # Main Function 
       
def tic_tac_toe () :

    print ("************ TIC-TAC-TOE Spiel************ \n")
    board = draw_board()
    
    current = "X"
    spieler_name = " "
    spieler_x= input("Spieler X , Gib deine Name ein ..\n")
    spieler_o = input ("Spieler O , Gib deine Name ein ..\n")
    
    while True :
        board_druck(board)

        if current == "X" :
            spieler_name = spieler_x
        else:
            spieler_name = spieler_o
        try:
            zeil = int(input(f"Spieler {spieler_name} gib Zeil ein (0-2) \n "))
            spalte = int( input(f"Spieler {spieler_name} gib spalte ein (0-2) \n "))

        except ValueError:
            print("Bitte nur  Numbers 0–2.!!!!")
            continue


        if not (0<= zeil <=2 and 0<=  spalte <=2):
            print("Bitte....,Geben  Zeil und Spalte  in range 0-2 ein")
            continue

        if board[zeil][spalte]!=" " :

            print("Zell nicht frei !!!!, wähl andere Zeil und Spalte")
            continue

        board[zeil][spalte] = current
        board_druck(board)

        if check_win(board, current):
           print(f" ** Spieler {spieler_name} hat gewonnen **")
           break
        if full_unenschieden(board) == True and check_win(board, current) == False :
            print ("board ist voll  --> unentschiden")
            break
        # spieler wechsel
        current = "O" if current == "X" else "X"
   

tic_tac_toe ()