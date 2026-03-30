class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquares(k):
            result = 0

            while k > 0:
                mod = k % 10
                k //= 10
                result += mod ** 2

            return result
        
        seen = set()

        while n not in seen:
            seen.add(n)
            n = sumofsquares(n)
            if n == 1:
                return True
            
        

        return False


    