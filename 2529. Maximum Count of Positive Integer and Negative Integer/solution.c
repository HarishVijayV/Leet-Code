int maximumCount(int* nums, int numsSize){
     int pos=0,neg=0;
        for(int i=0;i<numsSize;i++){
            if(nums[i]<0){
                neg++;
            }
            else if(nums[i]>0){
                pos++;
            }
        }
        if(neg>pos){
            return neg;
        }
        return pos;
}