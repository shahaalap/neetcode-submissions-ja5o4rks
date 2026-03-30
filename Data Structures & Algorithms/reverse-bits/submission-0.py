class Solution:
    def reverseBits(self, n: int) -> int:
        result  = 0

        for i in range(32):
            result = result << 1

            x = (n & 1)
            result += x
            
            n = n >> 1
        
        return result

            