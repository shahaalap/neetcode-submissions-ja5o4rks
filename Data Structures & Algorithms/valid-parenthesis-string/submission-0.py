class Solution:
    def checkValidString(self, s: str) -> bool:
        low , high = 0, 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:
                low -= 1 #consider as )
                high +=1 #consider as (
            
            if low < 0: #covers when * are considered to be closing character which can be ignored
                low = 0
            
            if high < 0: #covers when we have a log of closing characters for which we dont have enough opening chracters despite of considering all * as opening
                return False

        return low == 0 # covers rest of the case like )( where you have pending low for which closing never was accounted for
        
