class Solution {
    public int findGCD(int[] nums) {
        Arrays.sort(nums);
        int a,b;
        a=nums[0];
        b=nums[nums.length-1];
        while(true){
            if(a==b){
                return a;
            }
            if(a<b){
                b=b-a;
            }
            if(b<a){
                a=a-b;
            }
        }
    }
}
