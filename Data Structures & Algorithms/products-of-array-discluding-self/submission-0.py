class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre , post = [1] * len(nums), [1] * len(nums)

        prepostfixvalue = 1
        for i in range(len(nums)):
            pre[i] = prepostfixvalue * nums[i]
            prepostfixvalue = pre[i]

        prepostfixvalue = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = prepostfixvalue * nums[i]
            prepostfixvalue = post[i]

        result = []

        for i in range(len(nums)):
            preindex = i - 1
            postindex = i + 1

            if preindex == -1: 
                result.append(1 * post[postindex])
            elif postindex == len(nums):
                result.append(pre[preindex] * 1)
            else:
                result.append(pre[preindex] * post[postindex])
            
        return result