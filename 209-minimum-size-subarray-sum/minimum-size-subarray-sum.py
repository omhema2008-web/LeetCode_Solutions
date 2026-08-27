class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        sum = 0
        maxl = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum>=target :
                maxl = min(maxl,i-j+1)
                sum = sum-nums[j]
                j += 1
        return maxl if maxl != float('inf') else 0 
        