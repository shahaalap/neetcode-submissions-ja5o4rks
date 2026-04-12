class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            size = []
            while s[i] != '#':
                size.append(s[i])
                i += 1

            i += 1

            tempstr = []
            maxi = i + int(''.join(size))
            while i < maxi:
                tempstr.append(s[i])
                i += 1
            
            result.append(''.join(tempstr))
        
        return result
