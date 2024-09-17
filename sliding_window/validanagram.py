def validanagram(t: str, s: str):
    mp = {}
    if len(s) != len(t):
        return False
        
    for chr in s:
        if chr not in mp:
            mp[chr] = 0
        mp[chr] += 1 
    
    for chr in t:
        if chr in mp:
            mp[chr] -= 1
            if mp[chr] < 0:
                return False
        else:
            return False
    return True
    
result = validanagram("a","ab")
print(result)
        