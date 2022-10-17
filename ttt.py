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

def num_to_coord(square_num):
    coord = []
    coord[0] = (square_num - 1)/3
    coord[1] = square_num%3 - 1
    return coord

def put_in_board(board, mark, square_num):
    coord = num_to_coord(square_num)
    board[coord[0]][coord[1]] = mark
    return board
    
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
    
    input_counter = 0
    user_input = None
    while input_counter < 9:
        if input_counter%2 == 0:
            user_input = input("Where to place X: ")
        else: 
            user_input = input("Where to place O: ")
        input_counter+=1

    '''
    print("\n\n")
    
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    print_board_and_legend(board)
    '''
    