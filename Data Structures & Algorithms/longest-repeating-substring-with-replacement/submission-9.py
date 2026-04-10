class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        result = 0
        charset = defaultdict(int)

        for j in range(len(s)):
            c = s[j]
            charset[c] += 1

            while j - i + 1 - max(charset.values()) > k:
                charset[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)

        return result



        