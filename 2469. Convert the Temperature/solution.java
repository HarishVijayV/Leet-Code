class Solution {
    public double[] convertTemperature(double celsius) {
       double k,f;
       double [] arr=new double[2];
       k=273.15+celsius;
       f=celsius*1.80+32;
       arr[0]=k;
       arr[1]=f;
       return arr;
    }
}