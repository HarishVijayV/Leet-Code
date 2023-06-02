class Solution {
    public boolean isPowerOfThree(int n) {
        int x=0;
        while(x<n/2){
            if (n==Math.pow(3,x)){
                return true;
            }
                x++;
        }
        return false; 
    }
}