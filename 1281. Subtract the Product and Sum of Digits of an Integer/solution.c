int subtractProductAndSum(int n){
    int org,s=0,p=1;
    while(n>0){
        org=n%10;
        s=s+org;
        p=p*org;
        n=n/10;

    }
    return p-s;
}