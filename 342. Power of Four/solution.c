bool isPowerOfFour(int n){
    if(n==0){
        return false;
    }
        double result=log(n)/log(4);
        if(result==round(result)){
            return true;
        }
        return false;
}