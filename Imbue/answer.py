# 1. find closest * from (0,0) then start
def expected_length(field, k):
    # first construct a matrix from the list
    length = len(field)
    #creating empty matrix
    matrix = [["" for column in range(length)] for row in range(length)]
    print(matrix)   
    #creating matrix with the field elements
    for row in range(field):
        ch=0
        length_row = len(row)
        while ch<length_row:
            matrix[row][ch] = row[ch]
            ch+=1
    print(matrix)       
        
    # mat_row = length(matrix)
    # mat_col = length(matrix[0])
    # for row in range(mat_row):
    #     for col in range(mat_col):
    #         if matrix[row][col] == "*"

field = ["*#..#",".#*#.","*...*"]
k = 2
expected_length(field, k)
    