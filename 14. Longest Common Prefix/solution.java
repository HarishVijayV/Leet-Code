class Solution {
    public String longestCommonPrefix(String[] strs) {
        String a,b,out="";
        int j;
        Arrays.sort(strs);
        a=strs[0];
        b=strs[strs.length-1];
        j=Math.min(a.length(),b.length());
        for(int i=0;i<j;i++){
            if (a.charAt(i)==b.charAt(i)){
                out+=(a.charAt(i));
            }
            else{
                break;
            }    
            
        }
        return out;
    }
}