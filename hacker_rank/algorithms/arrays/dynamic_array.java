import java.io.*;
import java.util.*;

public class dynamic_array{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n,q;
		n = s.nextInt();
		q = s.nextInt();

		ArrayList<ArrayList<Integer>> seqList = new ArrayList<ArrayList<Integer>>();
		for (int i=0;i<n ;i++ ){
			ArrayList<Integer> list = new ArrayList<Integer>();
			seqList.add(list);
		}

		int x,y,z;
		int lastAnswer = 0;

		for (int i=0;i<q ;i++){
			x = s.nextInt();
			y = s.nextInt();
			z = s.nextInt();

			if(x == 1){
				seqList.get((y^lastAnswer)%n).add(z);
			} else if(x == 2){
				int index = seqList.get((y^lastAnswer)%n).size();
				lastAnswer = seqList.get((y^lastAnswer)%n).get(z%index);
				System.out.println(lastAnswer);
			}
		}
		
	}
}