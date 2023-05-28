int countDigits(int num){
      int x,count=0;
        int ori = num;
        while(num>0){
            x=num%10;
            if(ori%x==0){
                count=count+1;
            }
            num/=10;
        }
        return count;
}