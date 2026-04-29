import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def partition(i,j):
            pivot = random.randint(i,j)
            nums[i],nums[pivot] = nums[pivot],nums[i]

            orange = i
            for n in range(i + 1, j + 1):
                if nums[n] <= nums[i]:
                    orange += 1
                    nums[n], nums[orange] = nums[orange], nums[n]

            nums[i], nums[orange] = nums[orange],nums[i]
            return orange

        i , j = 0, len(nums) - 1

        while True:
            m = partition(i,j)
            if m == target:
                return nums[m]
            elif m < target:
                i = m + 1
            else:
                j = m - 1