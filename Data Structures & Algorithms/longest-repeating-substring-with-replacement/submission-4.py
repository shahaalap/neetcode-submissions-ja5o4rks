class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charcounts = defaultdict(int)
        l, result, maxchar = 0, 0, 0

        for r in range(len(s)):

            charcounts[s[r]] += 1
            maxchar = max(maxchar, charcounts[s[r]])

            while (r - l + 1) - maxchar  > k:
                
                charcounts[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
            

        return result



