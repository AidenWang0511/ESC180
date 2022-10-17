'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

from asyncio import new_event_loop
import random

def initialize():
    global gameover_flag
    gameover_flag = false

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def is_row_all_marks(board, row_i, mark):
    counter = 0
    for i in board[row_i]:
        if i == mark:
            counter += 1
    if counter == 3:
        return True
    else:
        return False

def is_col_all_marks(board, col_i, mark):
    counter = 0
    for i in range(len(board)):
        if board[i][col_i] == mark:
            counter += 1
    if counter == 3:
        return True
    else:
        return False

def is_win(board, mark):
    row = False
    col = False
    diagonal = False
    diag_counter = 0
    for i in range(3):
        if is_row_all_marks(board, i, mark):
            row = True
        if is_col_all_marks(board, i, mark):
            col = True
        if board[i][i] == mark:
            diag_counter += 1
    if diag_counter == 3:
        diagonal = True
    
    diagonal_counter = 0
    for i in range(3):
        if board[i][3-1-i] == mark:
            diagonal_counter += 1
    if diagonal_counter == 3:
        diagonal = True
        
    if (not row) and (not col) and (not diagonal):
        return False
    else:
        return True

def nxt_step_win(board, mark):
    for i in get_free_squares(board):
        board[i[0]][i[1]] = mark
        if is_win(board, mark):
            return
        else:
            board[i[0]][i[1]] = ' '
    return make_random_move(board, 'O')
    
    
def make_random_move(board, mark):
    free_L = get_free_squares(board)
    rand_num = (int(len(free_L) * random.random()))
    board[free_L[rand_num][0]][free_L[rand_num][1]] = mark
    return board

def num_to_coord(square_num):
    coord = []
    coord.append(int((square_num - 1)/3))
    coord.append((square_num-1)%3)
    return coord

def put_in_board(board, mark, square_num):
    coord = num_to_coord(square_num)
    board[coord[0]][coord[1]] = mark
    return board
    
def get_free_squares(board):
    free_sq_L = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_sq_L.append([i,j])
    return free_sq_L
    
def get_nums(L):
    new_L = []
    for i in L:
        new_L.append(i[1])
    return new_L

def lookup(L, num):
    for i in  L:
        if i[1] == num:
            return i[0]
    return None
    
if __name__ == '__main__':
    '''
    #problem 1
    L = [["CIV", 92],["180", 98],["103", 99],["194", 95]]
    print(L[2][1])

    #problem 2
    print(get_nums(L))

    #problem 3
    print(lookup(L, 99))
    '''

    board = make_empty_board()
    print_board_and_legend(board)
    
    '''
    5b test
    for i in range (9):
        if i%2 == 0:
            make_random_move(board, 'X')
        else:
            make_random_move(board, 'O')
        print_board_and_legend(board)
        print("\n\n")
    '''
    
    draw_flag = True
    while get_free_squares(board):
        user_input = input("Where to place X: ")
        put_in_board(board, 'X', int(user_input))
        print("\n\n")
        print_board_and_legend(board)
        if(is_win(board, 'X')):
            print("You Win!")
            draw_flag = False
            break
        #make_random_move(board, 'O')
        nxt_step_win(board, 'O')
        print("\n\n PC's Move:'")
        print_board_and_legend(board)
        if(is_win(board, 'O')):
            print("PC Win!")
            draw_flag = False
            break
    if draw_flag:
        print("Draw")
        
    
    '''
    draw_flag = True
    input_counter = 0
    user_input = None
    while input_counter < 9:
        if input_counter%2 == 0:
            user_input = input("Where to place X: ")
            put_in_board(board, 'X', int(user_input))
            print("\n\n")
            print_board_and_legend(board)
            if(is_win(board, 'X')):
                print("X Win!")
                draw_flag = False
                break
        else: 
            user_input = input("Where to place O: ")
            put_in_board(board, 'O', int(user_input))
            print("\n\n")
            print_board_and_legend(board)
            if(is_win(board, 'O')):
                print("O Win!")
                draw_flag = False
                break
        input_counter+=1
    if draw_flag:
        print("Draw")
    '''
    
    
    