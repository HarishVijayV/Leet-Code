class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> bool = new ArrayList<>();
        int flag=0;
        for(int i=0;i<candies.length;i++){
            for(int j=0;j<candies.length;j++){
                if(candies[i]+extraCandies >= candies[j]){
                    flag=1;
                }
                    else{
                        flag=0;
                        break;
                    }
            }
                    if(flag==1){
                        bool.add(true);
                    }
                    else{
                        bool.add(false);
                    }
        }
        return bool;
    }
}