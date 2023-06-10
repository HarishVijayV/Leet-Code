class Solution {
    public boolean isPowerOfFour(int n) {
        double result=Math.log(n)/Math.log(4);
        if(result==Math.round(result)){
            return true;
        }
        return false;
    }
}
