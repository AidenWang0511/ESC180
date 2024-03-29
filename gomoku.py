"""
Gomoku Game Project
Author(s): Aiden Wang and Gary Yang.  
Date: Nov. 15, 2022
"""

'''
check if a sqare is within boundary of board
Parameter:
    board - nested 2D list storing the game board
    y - row # of the sqare
    x - column # of the sqare
return True if within board, False otherwise
'''
def is_sq_in_board(board, y, x):
    if y >= len(board) or y < 0 or x >= len(board[0]) or x < 0:
        return False
    return True

'''
check if a sequence is complete
Parameter:
    board - nested 2D list storing the game board
    col - color of sequence to check
    y_start - starting position of seq for row
    x_start - starting position of seq for column
    length - length of sequence to check
    d_y - row direction
    d_x - column direction
return True if sequence is complete given the parameters, False otherwise
'''
def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
    if is_sq_in_board(board, y_start-d_y, x_start-d_x):
        if board[y_start-d_y][x_start-d_x] == col:
            return False
    
    for i in range(length):
        if is_sq_in_board(board, y_start + i*d_y, x_start + i*d_x):
            if board[y_start+i*d_y][x_start+i*d_x] != col:
                return False
        else:
            return False
    
    if is_sq_in_board(board, y_start + length*d_y, x_start + length*d_x):
        if board[y_start + length*d_y][x_start + length*d_x] == col:
            return False
    return True

'''
check if a board is completely empty
Parameter:
    board - nested 2D list storing the game board
return True if the board is completely empty, False otherwise
'''
def is_empty(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != " ":
                return False
    return True

'''
check if a sequence is complete
Parameter:
    board - nested 2D list storing the game board
    y_end - ending position of seq for row
    x_end - ending position of seq for column
    length - length of sequence to check
    d_y - row direction
    d_x - column direction
return OPEN if sequence is not bounded, SEMIOPEN if half bounded, 
       CLOSED if bounded on both side
'''
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    global closed_seq_5
    closed_seq_5 = 0
    color = board[y_end][x_end]
    start_bound = False
    end_bound = False
    if is_sq_in_board(board, y_end-length*d_y, x_end-length*d_x):
        if board[y_end - length*d_y][x_end - length*d_x] == " ":
            start_bound = False
        elif board[y_end - length*d_y][x_end - length*d_x] != color:
            start_bound = True
    else:
        start_bound = True
    if is_sq_in_board(board, y_end + d_y, x_end + d_x):
        if board[y_end + d_y][x_end + d_x] == " ":
            end_bound = False
        elif board[y_end + d_y][x_end + d_x] != color:
            end_bound = True
    else:
        end_bound = True
    
    if start_bound and end_bound:
        if length == 5:
            closed_seq_5 = 1
        return "CLOSED"
    elif start_bound or end_bound:
        return "SEMIOPEN"
    else:
        return "OPEN"

'''
return a tuple with # of open seq and # of semi closed seq given condition
Parameter:
    board - nested 2D list storing the game board
    col - color of sequence to detect
    y_start - starting position of seq for row
    x_start - starting position of seq for column
    length - length of sequence to detect
    d_y - row direction
    d_x - column direction
return a tuple following the description of this function
'''
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    while is_sq_in_board(board, y_start, x_start):
        if is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
            if is_bounded(board, y_start + (length-1)*d_y, x_start \
                + (length-1)*d_x, length, d_y, d_x) == "OPEN":
                open_seq_count += 1
                
            elif is_bounded(board, y_start + (length-1)*d_y, x_start \
                + (length-1)*d_x, length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1
        y_start += d_y
        x_start += d_x
    return open_seq_count, semi_open_seq_count

'''
return a tuple with # of open seq and # of semi closed seq of the entire board
Parameter:
    board - nested 2D list storing the game board
    col - color of sequence to detect
    length - length of sequence to detect
return a tuple following the description of this function
'''
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    
    temp_tulp = detect_row(board, col, 0, 0, length, 1, 0)
    open_seq_count += temp_tulp[0]
    semi_open_seq_count += temp_tulp[1]
    temp_tulp = detect_row(board, col, 0, 0, length, 0, 1)
    open_seq_count += temp_tulp[0]
    semi_open_seq_count += temp_tulp[1]
    temp_tulp = detect_row(board, col, 0, 0, length, 1, 1)
    open_seq_count += temp_tulp[0]
    semi_open_seq_count += temp_tulp[1]
    
    for r in range(1, len(board)):
        temp_tulp = detect_row(board, col, r, 0, length, -1, 1)
        open_seq_count += temp_tulp[0]
        semi_open_seq_count += temp_tulp[1]
        temp_tulp = detect_row(board, col, r, 0, length, 0, 1)
        open_seq_count += temp_tulp[0]
        semi_open_seq_count += temp_tulp[1]
        temp_tulp = detect_row(board, col, r, 0, length, 1, 1)
        open_seq_count += temp_tulp[0]
        semi_open_seq_count += temp_tulp[1]
        
    for c in range(1, len(board[0])):
        temp_tulp = detect_row(board, col, 0, c, length, 1, 0)
        open_seq_count += temp_tulp[0]
        semi_open_seq_count += temp_tulp[1]
        temp_tulp = detect_row(board, col, 0, c, length, 1, 1)
        open_seq_count += temp_tulp[0]
        semi_open_seq_count += temp_tulp[1]
        temp_tulp = detect_row(board, col, len(board)-1, c, length, -1, 1)
        open_seq_count += temp_tulp[0]
        semi_open_seq_count += temp_tulp[1]
        
    return open_seq_count, semi_open_seq_count
    
'''
return a tuple storing the most optimal move for pc to win
        (rely on the score() function)
Parameter:
    board - nested 2D list storing the game board
return a tuple with the most optimal move given the score() function
'''
def search_max(board):
    move_y, move_x, max_score_track = -1, -1, -1
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == " ":
                board[r][c] = "b"
                move_y, move_x, max_score_track = r, c, score(board)
                board[r][c] = " "
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == " ":
                board[r][c] = "b"
                temp_score = score(board)
                if temp_score > max_score_track:
                    move_y, move_x = r, c
                    max_score_track = temp_score
                board[r][c] = " "
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

'''
return whether the current game status is white won, black won, draw, 
        or continue playing
Parameter:
    board - nested 2D list storing the game board
return a string based on curretn status of the game 
'''
def is_win(board):
    global closed_seq_5
    closed_seq_5 = 0
    black = detect_rows(board, "b", 5)
    black_closed_5 = closed_seq_5
    closed_seq_5 = 0
    white = detect_rows(board, "w", 5)
    white_closed_5 = closed_seq_5
    if (black[0] + black[1] + black_closed_5) > 0:
        return "Black won"
    elif (white[0] + white[1] + white_closed_5) > 0:
        return "White won"
    else:
        full_flag = True
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == " ":
                    full_flag = False
        if full_flag:
            return "Draw"
        return  "Continue playing"

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        

def play_gomoku(board_size):
    global closed_seq_5
    closed_seq_5 = 0
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print(is_bounded(board, y_end, x_end, length, d_y, d_x))
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print(detect_row(board, "w", 0,x,length,d_y,d_x))
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, 0, 0, 1, 0, 5, "w")
    board[5][0] = "b"
    print_board(board)
    analysis(board)
    print(is_win(board))
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    play_gomoku(8)
