class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int c=0;
        for(std::size_t i=0;i<nums.size();i++){
            if(nums[i]!=val){
                nums[c]=nums[i];
                c=c+1;
            }
        } 
        return c;
    }
};