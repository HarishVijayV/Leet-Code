class Solution {
    public boolean checkString(String s) {
        int n= s.length(),flag=0;
        for(int i=0;i<n;i++){
            if(s.charAt(i)=='b'){
                flag=1;
            }
            if(flag==1 && s.charAt(i)=='a' ){
                return false;
            }
        }
        return true;
    }
}