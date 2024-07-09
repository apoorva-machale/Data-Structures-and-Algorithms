def checkPermutation(s1: str, s2: str):
        start, matched = 0, 0
        mp ={}
        for chr in s1:
            if chr not in mp:
                mp[chr] = 0
            mp[chr]+=1
        
        for end in range(len(s2)):
            right = s2[end]
            if right in mp:
                mp[right] -= 1
                if mp[right] == 0:
                    matched += 1
            if matched == len(mp):
                return True
            
            if end>= len(s1)-1:
                left = s2[start]
                start += 1
                if left in mp:
                    if mp[left]==0:
                        matched -= 1
                    mp[left]+=1
        return False
result = checkPermutation("ab","eidbaooo")
print(result)