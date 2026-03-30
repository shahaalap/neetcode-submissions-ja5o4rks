class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, seen, result = 0, {}, 0

        for r in range(len(s)):

            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            
            result = max(result, r - l + 1)

            
            

        return result