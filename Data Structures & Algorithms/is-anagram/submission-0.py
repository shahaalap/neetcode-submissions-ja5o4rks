class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        keys = {}
        for x in s:
            if x in keys:
                keys[x] = keys[x] + 1
            else:
                keys[x] = 1


        for y in t:
            if y in keys:
                keys[y] = keys[y] - 1
            else:
                return False

        
        for v in keys.values():
            if v != 0:
                return False

        return True


            