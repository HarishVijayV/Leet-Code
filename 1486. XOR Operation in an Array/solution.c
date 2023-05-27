int xorOperation(int n, int start){
    int x=0,nn;
    for(int i=0;i<n;i++){
        nn=start+2*i;
         x=x^nn;
    }
    
        return x;
}