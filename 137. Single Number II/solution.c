int singleNumber(int* nums, int numsSize){
     int count=0;
        for(int i=0;i<numsSize;i++){
            for(int j=0;j<numsSize;j++){
                if(i!=j){
                     if(nums[i]==nums[j]){
                        count++;
                        }
                    }
                }
             if(count==0){
                 return nums[i];
             }
             count=0;
        }
        return 1;

}