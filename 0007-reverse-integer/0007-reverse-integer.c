int reverse(int x){
      int s=0;
    while(x!=0){
        if(s>2147483647/10||(s==2147483647/10&&x%10>7)){
        return 0;
    }
    if(s<-2147483648/10||(s==-2147483648/10&&x%10<-8)) {
        return 0;
    }
    s=s*10 +x%10;
    x=x/10;
    }
    return s;
    }
