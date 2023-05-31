class Solution {
    public int[] shuffle(int[] nums, int n) {
        int i=0,j=0;
      int []array=new int[nums.length];
      while(j<n){
          array[i]=nums[j];
          i=i+2;
          j++;
          
      }
      i=1;
      j=n;
      while(i<nums.length){
          array[i]=nums[j];
          i=i+2;
          j++;
      }

      return array;
    }
}