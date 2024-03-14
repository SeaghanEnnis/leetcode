class Solution {
    public int removeElement(int[] nums, int val) {
        int notRemovedCount = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                nums[notRemovedCount++] = nums[i];
            }
        }
        
        return notRemovedCount;
    }
}

