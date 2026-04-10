class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        result = 0
        charset = defaultdict(int)

        def isvalid():
            #max char key
            temp = [(v, k) for k, v in charset.items()]
            temp.sort()

            # count of other keys than max > k
            if sum([v for k,v in charset.items() if k != temp[-1][1]]) <= k:
                return True
            else:
                return False

        for j in range(len(s)):
            c = s[j]
            charset[c] += 1

            while not isvalid():
                charset[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)

        return result



        