class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindrome(word):
            left=0
            right=len(word)-1
            while(left<=right):
                if word[left]!=word[right]:
                    return 0
                left+=1
                right-=1
            return 1
        
        for word in words:
            if palindrome(word):
                return word
        return ""