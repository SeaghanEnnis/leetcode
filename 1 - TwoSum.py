class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for x in range(len(nums)):
            if target - nums[x] in seen:
                return [x , seen[target - nums[x]] ]
            else:
                seen[nums[x]] = x