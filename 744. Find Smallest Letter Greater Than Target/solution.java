class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for(int i=0;i<letters.length;i++){
           if(char[i]>target){
               return char[i];
           }
        }
        return char[0];
    }
}