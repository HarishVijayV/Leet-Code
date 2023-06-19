class Solution {
    public int largestAltitude(int[] gain) {
        int[] arr=new int[gain.length+1];
        int sum=0,k=-101,max=0;
        for(int i=0;i<gain.length;i++){
            sum += gain[i];
            arr[i+1]=sum;
        }
        for(int i=0;i<arr.length;i++){
            if(arr[i]>k){
                k=arr[i];
                max=arr[i];
            }
        }
        return max;
    }
}