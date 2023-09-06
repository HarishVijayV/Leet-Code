int searchInsert(int* nums, int numsSize, int target){
     int F=0,L=numsSize-1;
        while(F<=L){
            int mid=(F+L)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if( nums[mid] < target ){
                F=mid+1;
            }
            else{
                L=mid-1;
            }
        }
        return F;
}