class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int l=0,mid;
        int r=arr.length-1;
        while (l<=r){
            mid= (int)((l+r)/2);
            if(arr[mid]>arr[mid+1] && arr[mid]>arr[mid-1]){
                return mid;
            }
            else if (arr[mid+1]>arr[mid]){
                l=mid+1;
            }
            else{
                r=mid-1;
            }
        }
        return -1;
    }
}