import numpy as np


def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)

def get_lead_ind(row):
    lead_ind = 0
    while lead_ind < len(row):
        if row[lead_ind] != 0:
            return lead_ind
        lead_ind += 1
    return lead_ind

def get_row_to_swap(M, start_i):
    min_lead_ind = get_lead_ind(M[start_i])
    res = start_i
    for r in range (start_i, len(M)):
        temp_lead_ind = get_lead_ind(M[r])
        if temp_lead_ind < min_lead_ind:
            min_lead_ind = temp_lead_ind
            res = r
    return res

def add_rows_coefs(r1, c1, r2, c2):
    resL = [0]*max(len(r1),len(r2))
    for i in range(len(resL)):
        resL[i] = r1[i]*c1 + r2[i]*c2
    return resL

def eliminate(M, row_to_sub, best_lead_ind):
    for r in range(row_to_sub+1,len(M)):
        sub_coef = M[r][best_lead_ind] / M[row_to_sub][best_lead_ind]
        M[r] = add_rows_coefs(M[r],1, M[row_to_sub],-sub_coef)

def back_eliminate(M, row_to_sub, best_lead_ind):
    print("row to sub:", row_to_sub)
    for r in range(row_to_sub-1, -1, -1):
        sub_coef = M[r][best_lead_ind] / M[row_to_sub][best_lead_ind]
        M[r] = add_rows_coefs(M[r],1, M[row_to_sub],-sub_coef)

def forward_step(M):
    for r in range(len(M)):
        print("looking at row", r)
        swap_row_ind = get_row_to_swap(M, r)
        tempR = M[r]
        M[r] = M[swap_row_ind]
        M[swap_row_ind] = tempR
        print(f"swapped row {r} with row {swap_row_ind}")
        print_matrix(M)
        print("Eliminate all coefficients on index", get_lead_ind(M[r]))
        eliminate(M,r,get_lead_ind(M[r]))
        print_matrix(M)

def backward_step(M):
    for r in range(len(M)-1, -1, -1):

        zeroFlag = True
        for c in range(len(M[0])):
            if M[r][c] != 0:
                zeroFlag = False
                break;
        if zeroFlag:
            continue
        print("Eliminate all coefficients on index", get_lead_ind(M[r]))
        back_eliminate(M,r,get_lead_ind(M[r]))
        print_matrix(M)
    print("Divide every row by its leading coefficient")
    for r in range (len(M)):
        divisor = M[r][get_lead_ind(M[r])]
        for c in range(len(M[0])):
            M[r][c] = M[r][c]/divisor
    print_matrix(M)

def solveMxb(M, b):
    tempM = []
    for r in range(len(M)):
        tempM.append([0]*(len(M[0])+1))
    for r in range(len(M)):
        for c in range(len(M[0])):
            tempM[r][c] = M[r][c]
        tempM[r][len(M[0])] = b[r]

    forward_step(tempM)
    backward_step(tempM)
    x = []
    for r in range(len(M)):
        x.append(tempM[r][len(M[0])])
    return x

if __name__ == '__main__':
    M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
    #question 1
    print("#1")
    print_matrix(M_listoflists)
    #2
    print("#2")
    print(get_lead_ind([1,2,3,4,5]))
    print(get_lead_ind([0,0,3]))
    print(get_lead_ind([0,0,0,0,0]))
    #3
    print("#3")
    M = [[1,0,1],[0,1,0],[1,0,0]]
    print(get_row_to_swap(M,1))
    #4
    print("#4")
    print(add_rows_coefs([1,2,3,4,5],2,[1,2,1,2,1],10))
    #5
    print("#5")
    M = [[5, 6, 7, 8],[0,0, 1, 1],[0, 0, 5, 2],[0, 0, 7, 0]]
    eliminate(M,1,2)
    print_matrix(M)
    #6,7
    print("#6,7")
    M = [[1, -2, 3, 22],[3, 10, 1, 315],[1, 5, 3, 92]]
    forward_step(M)
    print("This is the resulted M:")
    print_matrix(M)
    print("Backward Step __________________________________________")
    backward_step(M)
    print("This is the resulted M:")
    print_matrix(M)
    #8
    M = [[1,0,0],[0,1,2],[0,0,1]]
    print(solveMxb(M, [1,2,3]))


'''
# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]
'''