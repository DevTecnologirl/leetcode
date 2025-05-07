class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       x = 0
       for num in nums:
           x ^= num
       for i in range(len(nums)+1):
           x ^= 1
       return x