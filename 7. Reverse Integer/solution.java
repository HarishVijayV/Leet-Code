class Solution {
    public int reverse(int x) {
      int s=0;
    while(x!=0){
        if(s>Integer.MAX_VALUE/10||(s==Integer.MAX_VALUE/10&&x%10>7)){
        return 0;
    }
    if(s<Integer.MIN_VALUE/10||(s==Integer.MIN_VALUE/10&&x%10<-8)) {
        return 0;
    }
    s=s*10 +x%10;
    x=x/10;
    }
    return s;
    }
}