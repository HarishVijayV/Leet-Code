class Solution {
    public void duplicateZeros(int[] arr) {
        int n=arr.length;
        for(int i=0;i<n;i++){
            if(arr[i]==0){
                for(int j=n-2;j>i;j--){
                    arr[j+1]=arr[j];
                }
                if(i+1==n){
                    break;
                }
            
            arr[i+1]=0;
            i++;
            }
        }
    }
}