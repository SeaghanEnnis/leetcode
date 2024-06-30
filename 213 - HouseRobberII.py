class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        odd,even=0,0
        for i in nums:
            temp=max(i+odd,even)
            odd=even
            even=temp
        return even