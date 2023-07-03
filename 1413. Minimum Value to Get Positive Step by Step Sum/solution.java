class Solution {
    public int minStartValue(int[] nums) {
        int s=0,n=nums.length,j =1;
        while(s<1){
            s = j;
            for(int i=0;i<n;i++){
                s+=nums[i];
                if(s<1){
                    j++;
                    break;
                }
            }
        }
        return j;
    }
}