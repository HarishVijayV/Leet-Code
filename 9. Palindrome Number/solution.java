class Solution {
    public boolean isPalindrome(int x) {
        int org=x;
        int reve=0;
        if(x<0){
            return false;
        }
        else{
            while (x > 0) {
                int digit=x%10;
                reve=reve*10+digit;
                x=x/10;
            }
        }
        if(reve==org){
            return true;
        }
        return false;
    }
}