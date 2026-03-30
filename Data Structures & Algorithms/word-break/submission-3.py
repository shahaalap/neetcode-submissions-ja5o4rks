class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        worddic = set(wordDict)
        mem = {}
        def dfs(i):
            if i in mem:
                return mem[i]

            if i == len(s):
                mem[i] = True
                return True
                
            j = i
            while j < len(s):
                if s[i: j + 1] in worddic:
                    if dfs(j + 1):
                        mem[j + 1] = True
                        return True

                j += 1

            mem[i] = False
            return False

        return dfs(0)
                

