def make_good_move(board):
    print("board ki",board)
   

    for zeilen_index, zeil in enumerate(board):
       
        if zeil.count("X") == 2 or zeil.count("O") == 2:
            for zellen_index, zell in enumerate(zeil):
                if zell == " ":
                    return zeilen_index , zellen_index

        return None


def rest_zell(board):
    
    for zeilen_index, zeil in enumerate(board):
        for zellen_index, zell in enumerate(zeil):
                if zell == " ":
                    return zeilen_index , zellen_index



def check_diagonal(board):
    
    diag1 = [(0,0), (1,1), (2,2)]
    values = [board[i][j] for i, j in diag1]

    if (values.count("X") == 2 or  values.count("O") == 2) and values.count(" ") == 1:
        empty_zell = values.index(" ")
        ki_z,ki_s = diag1[empty_zell]
        return  ki_z,ki_s

    
    diag2 = [(0,2), (1,1), (2,0)]
    values = [board[i][j] for i, j in diag2]

    if (values.count("X") == 2 or values.count("O") == 2)  and values.count(" ") == 1:
        empty_zell= values.index(" ")
        ki_z,ki_s = diag2[empty_zell]
        return  ki_z,ki_s

    return None



def KI_move(board) :
    
    if make_good_move(board) is not None :
        ki_z , ki_s =make_good_move(board)
        return ki_z , ki_s 
    if board[1][1]== " ":
        ki_z= 1
        ki_s = 1
        return ki_z , ki_s 
    if check_diagonal(board) is not None :
        ki_z , ki_s = check_diagonal(board)
        return ki_z , ki_s 

    ki_z , ki_s =rest_zell(board)
    return ki_z , ki_s 

#board = [["X"," ","O"],[" ","O"," "],[" "," "," "]]

#print(check_diagonal(board))