def find_letter_case_permutations(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))
    return permutations

permutations = find_letter_case_permutations("ad52c")
print(permutations)