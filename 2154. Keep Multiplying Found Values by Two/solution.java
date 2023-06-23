class Solution {
    public int findFinalValue(int[] nums, int original) {
        int n=nums.length,k=original;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(k==nums[j]){
                    k*=2;
                }
            }
        }
        return k;
    }
}