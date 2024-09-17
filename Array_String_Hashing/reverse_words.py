def reverseWords(s):
    s = s + " "  # extra spacing for indicating end of a string
    stack = []
    word = ""        
    i = 0
    while i < len(s):
        if s[i] == " ":
            stack.append(word)
            word = ""
        elif s[i] != " ":
            word += s[i]
        i += 1
            
    new = ""
    while stack:
        eachWord = stack.pop()
        if eachWord:
            new = new + " " + eachWord
    return new[1:]

result = reverseWords("   hello world   ")
print(result)