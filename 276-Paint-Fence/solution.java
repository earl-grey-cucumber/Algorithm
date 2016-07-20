public class Solution {
    public int numWays(int n, int k) {
        if(n == 0 || k == 0) return 0;
        if(n == 1) return k==1 ? 1 : k;
        if(n == 2) return k * k;
        //(n<=0 || k<=0) return 0;
		int t0 = k, t1 = k * k;  //n=0 0, n=1 k ,n=2 k*k AA AB BB BA
	       for (int i = 2; i < n; ++i) {  //base 0
	           int t2 = (k - 1) * (t0 + t1);
	           t0 = t1;
	           t1 = t2;
	    }
	    return t1;

    }
}

 