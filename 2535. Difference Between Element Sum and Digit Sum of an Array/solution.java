class Solution {
    public int differenceOfSum(int[] nums) {
        int s1=0,s2=0,sum=0;
        for(int i=0;i<nums.length;i++){
            sum += nums[i];
            if(nums[i]<10){
                s1 +=nums[i];
            }
            else{
                while(nums[i]>0){
                s2 +=nums[i]%10;
                nums[i]=nums[i]/10;
                }
            }
        }
        int c=sum-s1-s2;
        if(c>=0){
            return c;
        }
        else{
            return-c;
        }
    }
}