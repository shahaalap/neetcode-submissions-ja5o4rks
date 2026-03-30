class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        kyes = {}
        output = False

        for x in nums:
            if x in kyes:
                output = True
                break
            else:
                kyes[x] = x
        
        return output
        