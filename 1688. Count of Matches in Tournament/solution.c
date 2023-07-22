int numberOfMatches(int n){
    int j=0;
    while(n>1){
        if(n%2==0){
            j+=n/2;
            n=n/2;
        }
    else{
        j+=(n-1)/2;
        n=((n-1)/2)+1;
    }
    }
    return j;
}