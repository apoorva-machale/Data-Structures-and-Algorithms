class Solution:
    def minimumLength(self, s: str) -> int:
        l=0
        r=len(s)-1
  
        while r > l and s[l] == s[r]:
            check = s[l]
            
            while l <= r and s[l] == check:
                l += 1

            # Delete consecutive occurrences of c from suffix
            while r > l and s[r] == check:
                r -= 1    
               
        return r-l+1   