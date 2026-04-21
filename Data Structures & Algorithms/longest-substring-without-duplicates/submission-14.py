class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        hashOfS = {}
        result = 0

        for j in range(len(s)):
            c = s[j]
            if c in hashOfS and hashOfS[c] >= i:
                i = hashOfS[c] + 1
                
            hashOfS[c] = j
            result = max(result, j - i + 1)

        return result


            