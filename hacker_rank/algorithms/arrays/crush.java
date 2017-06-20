import java.io.*;
import java.util.*;


public class crush{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n,m,a,b,max;
		n=s.nextInt();
		m=s.nextInt();
		max = 0;

		int[] c = new int[m];
		int[] seq = new int[n];
		int[][] pre_matrix = new int[m][n];

		for (int i=0;i<m ;i++ ) {
			a=s.nextInt();
			b=s.nextInt();
			c[i]=s.nextInt();
			for (int j=a-1;j<b ;j++ ) {
				if(j>=0 && j<=n){
					pre_matrix[i][j] = 1;
					}
				}
			}
		

		for (int i=0; i<n;i++ ) {
			int value = 0;
			for (int j=0; j<m;j++ ) {
				value += pre_matrix[j][i]*c[j];
			}
			if(max < value){
				max = value;
			}			
		}
		System.out.print(max);

	}
}