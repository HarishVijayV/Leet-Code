class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int n=arr.length,i=0;
        while(i<n-2){
            if(arr[i]%2!=0 && arr[i+1]%2!=0 && arr[i+2]%2!=0){
                return true;
                }
            i++;
        }
    return false;
    }
}