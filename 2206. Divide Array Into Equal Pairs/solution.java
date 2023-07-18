class Solution {
    public boolean divideArray(int[] nums) {
        Arrays.sort(nums);
        for(int i=0;i<=nums.length-2;i=i+2){
            if(nums[i]!=nums[i+1]){
                return false;
            }
        }
        return true;
    }
}