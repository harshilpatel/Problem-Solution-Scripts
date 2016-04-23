// #java
// # Author: harshil912@gmail.com
// # Click - o - mania
// # https://www.hackerrank.com/challenges/click-o-mania
import java.io.*;
import java.util.*;
public class clickomania{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int x = s.nextInt();
		int y = s.nextInt();
		int color = s.nextInt();
		char grid[][] = new char[x][y];
		for(int i=0; i<x;i++){
			String str = s.next();
			for(int j = 0;j <y ;j++) {
			  grid[i][j] = str.charAt(j);
			}
		}
		nextmove(x,y,color,grid);
	}

	public static void nextmove(int x,int y,int color,char grid[]){
		int x_connected = 0
		int y_connected = 0
		for (int i=0;i<color ;i++ ) {
			for (int j=0;j<x ;j++ ) {
				for (int k=0;k<y;k++ ) {
			
				}
			}
		}

	}

	public static void check_if_neighbours(int i,int j, char grid[],int x, int y){

	}
}