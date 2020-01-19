class Solution {
	public long solution(int w,int h) {
        long wl = (long)w;
        long hl = (long)h;
		long answer = wl * hl - (wl + hl - GCD(wl,hl));
		return answer;
	}
    
   private long GCD(long a,long b) 
   { 
       if (b==0) { return a; } 
       return GCD(b,a%b);
   }
}