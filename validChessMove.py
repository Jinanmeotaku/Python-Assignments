#Given a chess piece, its starting position, and its ending position determine if 
# its a valid chess move.
#For this discussion, choose one of the pieces to write a function 
# for (rook, knight, bishop, king, queen). 

#we can also solve this problem by seperating each piece into its own function 
#and then calling the function based on the piece given as an argument to the main function

#the way we would do that is by using the same exact code for each section
#and taking out the outer if and elif statements 


def validChessMove(piece, start_x, start_y, end_x, end_y):

    if piece == "PAWN":   #pawns can only move forward 
        #pawn on first move can move two spaces
        if start_x == end_x and start_y == 2 and end_y == 4:
            return True
        elif start_x == end_x and start_y + 1 == end_y:
            return True
        else:
            return False
        
    elif piece == "ROOK":   #rooks can move horizontally or vertically
       #rooks can move horizontally
        if start_x == end_x or start_y == end_y:
            return True
        else:
            return False
    elif piece == "KNIGHT":

        if (abs(start_x - end_x) == 2 and abs(start_y - end_y) == 1) or (abs(start_x - end_x) == 1 and abs(start_y - end_y) == 2):
            return True
        else:
            return False
    elif piece == "BISHOP":      #bishops move diagonally
        if abs(start_x - end_x) == abs(start_y - end_y):
            return True
        else:
            return False
    elif piece == "QUEEN":
        if start_x == end_x and start_y == end_y:
            return False
            
        if start_x == end_x or start_y == end_y or abs(start_x - end_x) == abs(start_y - end_y):
            return True
        else:
            return False
    elif piece == "KING":
        if start_x == end_x and start_y == end_y:
            return False
            
        if (abs(start_x - end_x) == 1 or abs(start_x - end_x) == 0) and (abs(start_y - end_y) == 1 or abs(start_y - end_y) == 0):
            return True
        else:
            return False


#Test cases
print(validChessMove( "PAWN", 2, 2, 2, 4))  #True
print(validChessMove("ROOK", 1, 1, 1, 8))  #True
print(validChessMove("KNIGHT", 1, 1, 2, 3))  #True
print(validChessMove("BISHOP", 1, 1, 3, 3))  #True
print(validChessMove("QUEEN", 1, 1, 8, 8))  #True
print(validChessMove("KING", 1, 1, 2, 2))  #True
print(validChessMove("KING", 1, 1, 3, 3))  #False
print(validChessMove("QUEEN", 1, 1, 1, 1))  #False
print(validChessMove("BISHOP", 1, 1, 1, 3))  #False