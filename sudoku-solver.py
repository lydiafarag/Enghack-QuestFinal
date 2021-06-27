#9 rows 9 columns. 0 as placeholder
board = [[7,8,0,4,0,0,1,2,0],[6,0,0,0,7,5,0,0,9],[0,0,0,6,0,1,0,7,8],[0,0,7,0,4,0,2,6,0],[0,0,1,0,5,0,9,3,0],[9,0,4,0,6,0,0,0,5],[0,7,0,3,0,0,0,1,2],[1,2,0,0,0,7,4,0,0],[0,4,9,2,0,6,0,0,7]]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo [row][col] = 0
#Check if the current bored is valid
def valid(bo,num,pos):
    #need to check row, collum and square
    #Check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #Check collumn
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] !=i:
            return False
    #What box are we in
    box_x = pos[1] // 3
    box_y = pos[0] //3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x *3 , box_x *3 +3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
#board is divided into 9 squares. use ---- to indicate
def print_board(bo):
    for i in range (len(bo)):
        #Vertical lines: grid lines after every 3 lines to make the 9 squares.
        if i % 3 == 0 and i !=0:
            print("------------------------")
        #goes through second array to do Horizontal lines
        for j in range (len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "") #end means that it doesnt print /n so it doesnt go to the next line

            if j == 8:
                print(bo[i][j])

            else:
                print(str(bo[i][j]) + " ", end="")

print (print_board(board))
#Find an Empty space
def find_empty(bo):
    for i in range (len(bo)):
        #0 indicates an empty space
        for j in range (len(bo[0])):
            if bo[i][j] == 0:
                return(i,j)
    return None

print_board(board)
solve(board)
print("_______________________________________")
print_board(board)
