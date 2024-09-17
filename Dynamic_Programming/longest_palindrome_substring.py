def longest_palindrome_substring(string):
    ## Approach using DP - from ends of the string
    n = len(string)
    dp = [[False]*n for _ in range(n)]
    result = [0,0]
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n-1):
        if string[i] == string[i+1]:
            dp[i][i+1] = True
            ans = [i,i+1]
    
    for diff in range(2,n):
        for i in range(n-diff):
            j = i + diff
            if string[i] == string[j] and dp[i+1][j-1]:
                dp[i][j] = True
                ans = [i,j]
    i, j = ans
    return string[i:j+1]
    
    ## Approach of DP - Expand from Centers
    def expand(i,j):
        left = i
        right = j
        while left>=0 and right<len(string) and string[left]==string[right]:
            left -= 1
            right += 1
        return right-left-1
    
    ans = [0,0]
    for i in range(len(string)):
        oddlength = expand(i,i)
        if oddlength > ans[1] - ans[0] + 1:
            dist = oddlength //2
            ans = [i-dist, i+dist]
        evenlength = expand(i,i+1)
        if evenlength > ans[1] - ans[0] + 1:
            dist = (evenlength // 2) - 1
            ans = [i-dist, i+1+dist]
    i,j =ans
    return string[i:j+1]

    ## Approach of DP from centers
    # Below code handles  - where the input is ABC - and output should be None, if we don't want to consider any single letter palindrome
    def funcSubstring(inputStr):
        def expand(left, right):
            while left >= 0 and right < len(inputStr) and inputStr[left] == inputStr[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

    start, end = 0, 0
    for i in range(len(inputStr)):
        # Check for odd-length palindromes
        left, right = expand(i, i)
        if right - left > end - start:
            start, end = left, right

        # Check for even-length palindromes
        left, right = expand(i, i + 1)
        if right - left > end - start:
            start, end = left, right

    # Check if a palindrome of length > 1 was found
    if end - start + 1 > 1:
        return inputStr[start:end+1]
    else:
        return None
    
        

string = "racecar"
result = longest_palindrome_substring(string)
print(result)