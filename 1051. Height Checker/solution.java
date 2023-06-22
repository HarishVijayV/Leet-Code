class Solution {
    public int heightChecker(int[] heights) {
        int n=heights.length,count=0;
        int [] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=heights[i];
        }
        Arrays.sort(heights);
        for(int i=0;i<n;i++){
            if(arr[i]!=heights[i]){
                count++;
            }
        }
        return count;
    }
}