class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        if not s:
            return result

        l, r, n, hashmap = 0, 0, len(s), {}

        for r in range(n):
            if s[r] in hashmap and hashmap[s[r]] >= l:
                l = hashmap[s[r]] + 1
            
            hashmap[s[r]] = r
            result = max(result, (r - l + 1))
        
        return result

