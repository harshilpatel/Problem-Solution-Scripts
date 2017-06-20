import java.io.*;
import java.util.*;

public class left_rot{

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n,d;
		n = s.nextInt();
		d = s.nextInt();

		int[] seq = new int[n];
		for (int i=0;i<n ;i++ ) {
			seq[(i+n-d)%n] = s.nextInt();
		}
		for (int i=0;i<n ;i++ ) {
			System.out.print(seq[i] + " ");
		}

	}

}