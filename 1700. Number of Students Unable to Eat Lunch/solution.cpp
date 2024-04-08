class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int n=students.size();
        std::vector<int> arr = {0,0};
        for(int i=0;i<n;i++){
            arr[students[i]]+=1;
        }
        for(int j=0;j<n;j++){
            if(arr[sandwiches[j]]==0){
                break;
            }
            arr[sandwiches[j]]-=1;
        }
        return arr[0]+arr[1];
    }
};