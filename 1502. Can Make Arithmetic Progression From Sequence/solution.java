    class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        int temp,flag=0;
        Arrays.sort(arr);
        flag=arr[1]-arr[0];
        int i=1;
        while(i<arr.length-1){
            if(arr[i+1]-arr[i]==flag){
                i=i+1;
            }
            else{
                return false;
            }
        }
        return true;
    }
    }