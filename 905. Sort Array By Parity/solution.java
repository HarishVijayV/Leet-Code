class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int []arr=new int[nums.length];
        int ii=0,j=nums.length-1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2!=0){
                arr[j]=nums[i];
                j--;
            }
            else{
                arr[ii]=nums[i];
                ii++;
            }
        }
        return arr;
    }
}