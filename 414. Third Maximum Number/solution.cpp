class Solution {
public:
    int thirdMax(vector<int>& nums) {
        std::set<int> s(nums.begin(),nums.end());
        std::vector<int> v(s.begin(),s.end());
        std::sort(v.begin(),v.end());
        if(v.size()>=3){
            return v[v.size()-3];
        }
        else{
            return v[v.size()-1];
        }
        
    }
};

