class Solution {
    public int singleNumber(int[] nums) {
        int count=0;
        Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                count++;
            }
            else{
                if(count<2){
                    return nums[i-1];
                }
                count=0;
            }
        }
        return nums[nums.length-1];
    }
}


