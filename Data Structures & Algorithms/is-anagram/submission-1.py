class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False

        charset = defaultdict(int)

        for c in s:
            charset[c] += 1
        
        for c in t:
            if c in charset:
                charset[c] -= 1
            else:
                return False

        return not any(charset.values()) != 0