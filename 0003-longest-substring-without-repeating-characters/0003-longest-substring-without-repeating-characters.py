class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        freq = {}
        max_length = 0
        
        for end in range(len(s)):
            right = s[end]
            if right in freq:
                start = max(start, freq[right]+1)
            freq[right] = end
            max_length = max(max_length, end-start+1)
        return max_length
        