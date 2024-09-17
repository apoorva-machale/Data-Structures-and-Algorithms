def Array_problem(A,B):
    a = sum(A) + A.count(0)
    b = sum(B) + B.count(0)
    if a != b and 0 not in (A if a > b else B):
        return -1 # If the condition is true, return -1
    return max(a, b)

A = [2, 5, 0, 1, 1]
B = [2, 1, 0, 0]
result = Array_problem(A, B)
print(result)