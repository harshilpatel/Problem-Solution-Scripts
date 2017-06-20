import java.io.*;
import java.util.*;


public class crush{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		long n,m,a,b,c,max;

		n=s.nextInt();
		m=s.nextInt();
		max = 0;

		int[] seq = new int[n];

		for (int i=0;i<m ;i++ ) {
			a=s.nextInt();
			b=s.nextInt();
			c=s.nextInt();
			for (int j=a-1;j<b ;j++ ) {
				if(j>0 && j<n){
					seq[j] += c;
					if (seq[j]>max) {
						seq[j] = max;
					}
				}
			}
		}

		System.out.print(max);

	}
}