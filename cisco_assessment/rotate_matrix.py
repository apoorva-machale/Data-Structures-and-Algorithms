### cisco assessment question - rotate matrix - 90 degree
def funcRotate(inputMat):
    rows = len(inputMat)
    for i in range(rows):
        for j in range(i+1, rows):
            inputMat[j][i], inputMat[i][j] = inputMat[i][j], inputMat[j][i]
    
    for i in range(rows):
        for j in range(rows //2):
            inputMat[i][j], inputMat[i][-j-1] = inputMat[i][-j-1], inputMat[i][j]
    #inputMat - [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    #convert inputMat to get as a desired output matrix 
    result = ""
    for sublist in inputMat:
        result += "".join(str(element) for element in sublist) + "\n"
        return result.rstrip()
    
# main function given in the question - they take input as map but to further solve the problem - they convet into list
def main():
    matrix = []
    r, c = map(int, input().split())
    for index in range(r):
        matrix.append(list(map(int, input().split())))
    result = funcRotate(matrix)
    print(result)
    
""" 
Input 
1 2 3
4 5 6
7 8 9

output
7 4 1 
8 5 2
9 6 3
"""