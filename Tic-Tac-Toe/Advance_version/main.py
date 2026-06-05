import board as bm 
import KI


def tic_tac_toe () :

    print ("************ TIC-TAC-TOE Spiel************ \n")
    board = bm.draw_board()
    
    current = "X"
    spieler_x= input("Spieler X , Gib deine Name ein ..\n")
            
    while True :

        bm.board_druck(board)

        
        if current == "X":
            try:
                    zeil = int(input(f"Spieler {spieler_x} gib Zeil ein (0-2) \n "))
                    spalte = int( input(f"Spieler {spieler_x} gib spalte ein (0-2) \n "))

            except ValueError:
                    print("Bitte nur  Numbers 0–2.!!!!")
                    

                
            if not (0<= zeil <=2 and 0<=  spalte <=2):
                print("Bitte....,Geben  Zeil und Spalte  in range 0-2 ein")
                continue
            
            if bm.check_if_valid(board,zeil,spalte) == True :
                 board[zeil][spalte] = current


        elif current == "O" :
            ki_z , ki_s =KI.KI_move(board) 
            if bm.check_if_valid(board,ki_z,ki_s) == True :             
                board[ki_z][ki_s] = current

        bm.board_druck(board)

        if bm.check_win(board, current):
            print(f" ** Spieler {current} hat gewonnen **")
            break
        if bm.full_unenschieden(board) == True and bm.check_win(board, current) == False :
            print ("board ist voll  --> unentschiden")
            break
        # spieler wechsel
        current = "O" if current == "X" else "X"
   

tic_tac_toe ()