sudoku=[
    [3, 0, 6, 5, 0, 8, 4, 0, 0], 
    [5, 2, 0, 0, 0, 0, 0, 0, 0], 
    [0, 8, 7, 0, 0, 0, 0, 3, 1], 
    [0, 0, 3, 0, 1, 0, 0, 8, 0], 
    [9, 0, 0, 8, 6, 3, 0, 0, 5], 
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 7, 4], 
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
] 

sudoku2=[
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0]
]


def solve_sudoku(board):
    space=find_space(board)
    if space:
        x,y=space
    else:
        return True
    for i in range(1,10):
        if check_valid(board,x,y,i):
            board[y][x]=i
            if solve_sudoku(board):
                return True
            board[y][x]=0
    return False

def print_Board(board):
    for i in range(9):
        for j in range(9):
            if j==2 or j==5:
                print(board[i][j], end=' | ')
            else:
                print(board[i][j], end=' ')
        print()
        if i==2 or i==5:
            print('---------------------')

def find_space(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (j,i)
    return None

def check_valid(board,x,y,num):
    if check_box(board,x,y,num) and check_x(board,x,y,num) and check_y(board,x,y,num):
        return True
    return False
    
def check_x(board,x,y,num):
    for i in range(9):
        if board[y][i]==num and i != x:
            return False
    return True

def check_y(board,x,y,num):
    for i in range(9):
        if board[i][x]==num and i != y:
            return False
    return True

def check_box(board,x,y,num):
    box_x=x//3
    box_y=y//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if board[i][j]==num and (j,i) != (x,y):
                return False
    return True

print("Entered Sudoku: \n")
print_Board(sudoku2)
print()
solve_sudoku(sudoku2)
print("Solved Answer: \n")
print_Board(sudoku2)
print()
