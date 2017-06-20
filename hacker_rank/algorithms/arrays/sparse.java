import java.io.*;
import java.util.*;

class sparse{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		Hashtable<String, Integer> seq = new Hashtable<String, Integer>();
		int n = s.nextInt();
		for (int i=0;i<n ;i++ ) {
			String newValue = s.nextLine();
			if(seq.contains(newValue)){
				seq.put(newValue, seq.get(newValue) + 1);
			} else{
				seq.put(newValue, 1);
			}
		}
		int d = s.nextInt();
		for (int i=0;i<d ;i++ ) {
			String valueToCheck = s.nextLine();
			if(seq.get(valueToCheck) != null){
				System.out.println(seq.get(valueToCheck));
			}else{
				System.out.println(0);
			}
		}
	}
}