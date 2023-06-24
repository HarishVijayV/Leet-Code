class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n=image.length,temp;
        int [][]arr=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr[i][j]=image[i][n-1-j];
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(arr[i][j]==0){
                    arr[i][j]=1;
                }
                else{
                    arr[i][j]=0;

                }
            }
        }
        return arr;
    }
}