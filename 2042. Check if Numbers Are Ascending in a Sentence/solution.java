class Solution {
    public boolean areNumbersAscending(String s) {
        int val=-1;
        for(String a : s.split(" ")){
            try{
                if(Integer.parseInt(a)>val){
                val=Integer.parseInt(a);
            }
            else{
                return false;
            }}
            catch(NumberFormatException e){
                continue;
            }
        }
        return true;
    }
}
