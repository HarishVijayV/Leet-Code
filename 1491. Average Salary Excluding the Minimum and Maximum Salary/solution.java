class Solution {
    public double average(int[] salary) {
        Arrays.sort(salary);
        int sum=0,n=salary.length-1;
        for(int i=1;i<n;i++){
            sum += salary[i];
        }
        double x=(double)sum/(n-1);
        return x;
    }
}