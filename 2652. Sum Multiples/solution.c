int sumOfMultiples(int n){
    int sum=0;
    for(int i=1;i<=n;i++){
        if (i%3==0||i%5==0||i%7==0){
           // if (!(i%15==0||i%35==0||i%21==0)){
                sum=sum+i;
            }
        }
 return sum;
    }
   
// }