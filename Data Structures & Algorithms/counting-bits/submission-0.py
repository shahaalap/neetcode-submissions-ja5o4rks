class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countbit(n):
            result = 0

            while n > 0:
                if n & 1:
                    result += 1
                n = n >> 1
            
            return result

        finalresult = []
        for i in range(n + 1):
            finalresult.append(countbit(i))
        
        return finalresult