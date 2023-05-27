class Solution {
    public boolean isPalindrome(int x) {
        int org=x;
        int rev=0;
        if(x<0){
            return false;
        }
        else{
            while (x > 0) {
                int digit=x%10;
                rev=rev*10+digit;
                x=x/10;
            }
        }
        if(rev==org){
            return true;
        }
        return false;

    }
}