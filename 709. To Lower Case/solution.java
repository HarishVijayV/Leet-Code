class Solution {
    public String toLowerCase(String s) {
        String c="";
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if('A'<=ch && ch<='Z'){
                c+=(char)(ch+32);
            }
            else{
                c+=(char)ch;
            }
        }
        return c;
    }
}