    class Solution {
        public int smallestEvenMultiple(int n) {
        if (n==1){
            return 2;
        }
        for(int i=1;i<=n/2;i++){
        for(int j=1; j<=n;j++) {
                if (n*i==2*j){
                
                return n*i;    
        } 
        else{
            continue;
        }
        
        }
        
        }
        return 6;
    }
    }