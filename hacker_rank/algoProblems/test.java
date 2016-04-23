import java.io.*;
import java.util.*;

class test{
	public static void main(String[] args) {
		ArrayList listOfItems = new ArrayList();
		Scanner s = new Scanner(System.in);
		// int pages = s.nextInt();
		// int book = s.nextInt();
		// int problems[] = new int[pages];
		int limit = s.nextInt();
		for(int i=0;i<limit;i++){
			listOfItems.add(i,i);
		}
		for(int i=0;i<listOfItems.size();i++){
			System.out.print(listOfItems.get(i) + ", ");
		}
		System.out.println("Thanks");
	}
}