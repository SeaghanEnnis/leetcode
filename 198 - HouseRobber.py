class Solution:
    def rob(self, nums: List[int]) -> int:
        odd,even=0,0
        for i in nums:
            temp=max(i+odd,even)
            odd=even
            even=temp
        return even