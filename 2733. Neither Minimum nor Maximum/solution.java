class Solution {
    public int findNonMinOrMax(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length-1;
        for(int i=1;i<n;i++){
            if(nums[i]!=nums[0] && nums[i]!=nums[n]){
                return nums[i];
            }
        }
        return -1;
    }
}