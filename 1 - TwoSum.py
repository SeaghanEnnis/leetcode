class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for x in range(len(nums)):
            if target - nums[x] in seen:
                return [x , seen[target - nums[x]] ]
            else:
                seen[nums[x]] = x