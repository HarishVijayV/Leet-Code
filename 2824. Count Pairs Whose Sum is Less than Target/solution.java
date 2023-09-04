class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int count=0;
        for(int j=0;j<nums.size();j++){
            for(int i=0;i<j;i++){
                if(nums.get(i)+nums.get(j)<target){
                    count++;
                }
            }
        }
        return count;
    }
}