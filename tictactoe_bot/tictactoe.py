#SISYPHUS


from random import randrange
board = [[1,2,3],[4,5,6],[7,8,9]]
free_fields = []


def display_board():
    return("""
                     +----------+----------+----------+
    |                  |                 |                 |
    |       {}         |        {}      |       {}        |
    |                  |                 |                 |
   +----------+----------+----------+
    |                  |                 |                 |
    |       {}        |       {}        |       {}       |
    |                  |                 |                 |
    +----------+----------+----------+
    |                  |                 |                 |
    |       {}         |      {}        |       {}        |
    |                  |                 |                 |
   +----------+----------+----------+
            """.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]))


def enter_move(move):   
    if victory_for() is None:
        for x in board:
            if move in free_fields and move in x:

                if move <4:             
                    board[0][x.index(move)] = "O"
                
                elif move <7:
                    board[1][x.index(move)] = "O"
                
                elif move>=7:
                    board[2][x.index(move)] = "O"


def make_list_of_free_fields():
    free_fields.clear()
    for x in board:
        for i in x:
            if type(i) is int:
                free_fields.append(i)


def victory_for():
    for x in board:
        for i in range(len(x)):
            
            if x.count("X") == 3:
                return "X"
            
            elif x.count("O") == 3:
                return "O"
            
            elif board[0][2] == board[1][1] == board[2][0] or board[0][0] == board[1][1] == board[2][2]:
                return board[1][1]
           
            elif board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
    
    if len(free_fields)  == 0:
        return "Tie"


def reset_game():
    return [[1,2,3],[4,5,6],[7,8,9]]


def draw_move():
    if len(free_fields)> 0 :
        row = randrange(0,3)
        column = randrange(0,3)
        value = board[row][column]
        if value in free_fields:
            board[row][column] = "X"
        else:
            draw_move()
    else:
        return
