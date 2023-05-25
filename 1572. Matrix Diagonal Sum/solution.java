class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int temp1;
        String temp2;
        for(int i=0;i<heights.length-1;i++){
            if(heights[i]<heights[i+1]){
                temp1= heights[i];
                temp2= names[i];
                heights[i]=heights[i+1];
                names[i]=names[i+1];
                heights[i+1]=temp1;
                names[i+1]=temp2;
            }
        }
        return names;
    }
}