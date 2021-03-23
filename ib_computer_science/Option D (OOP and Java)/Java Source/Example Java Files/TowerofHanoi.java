import java.util.*;
public class TowerofHanoi{
	static Stack <Integer>SPa = new Stack<Integer> ();
	static Stack <Integer>SPb = new Stack<Integer> ();
	static Stack <Integer>SPc = new Stack<Integer> ();
	static Stack <Integer>SPd = new Stack<Integer> ();
	static String [] daa = {};
	static String [] dbb = {};
	static String [] dcc = {};
	@SuppressWarnings("rawtypes")
	static Stack PEGS [] = {SPa, SPb, SPc, SPd};
	static int i = 0;
	static int a = 1;
	static int b = 2;
	static int c = 3;
	static int t = 0;
	static int n = 0;
	static int m = 0;
	static String da ="";
	static String db="";
	static String dc ="";
	static int num = 5;
	static String f1 ="";
	static String f2 ="";
	static String f3 ="";
	
	
	
	@SuppressWarnings("unchecked")
	public static void display() {
			System.out.println("");
			System.out.println("| A | B | C |");
			for (int i=0; i<(num);i++) {
				if (!PEGS[1].isEmpty()) {
					daa[i] = (String) PEGS[1].pop();
				}
				else {
					daa[i]=null;
				}
				if (!PEGS[2].isEmpty()) {
					dbb[i] = (String) PEGS[2].pop();
				}
				else {
					dbb[i]=null;
				}
				if (!PEGS[3].isEmpty()) {
					dcc[i] = (String) PEGS[3].pop();
				}
				else {
					dcc[i]=null;
				}
			}
			
			for (int i=0;i<(num);i++) {
				da = String.valueOf(daa[i]);
				db = String.valueOf(dbb[i]);
				dc = String.valueOf(dcc[i]);
				
				f1 = da;
				if (f1 == "null") {
					f1 = "-";
				}
				
				f2 = db;
				if (f2== "null") {
					f2 = "-";
				}
				
				f3 = dc;
				if (f3== "null") {
					f3 = "-";
				}
				
				System.out.println("| "+f1+" | "+f2+" | "+f3+" | ");
			}
			
			for (int i=0;i<(num);i++) {
				m = num-1-i;
				PEGS[1].push(daa[m]);
				PEGS[2].push(dbb[m]);
				PEGS[3].push(dcc[m]);
			}
	}

	@SuppressWarnings("unchecked")
	public static void move (int n,int a, int b, int c) {
		if (n > 0) {
			move(n-1,a,c,b);
			t = (int) PEGS[a].pop();
			PEGS[c].push(t);
			display();
			move(n-1,b,a,c);
		}
	}
			
			
	
	public static void TowerofHanoi(int n) {
			
			for (int i=0;i<(n);i++) {
				m = n - i;
				PEGS[1].push(m);
			}
			
			display();
			move(n,1,2,3);
		}
	public static void main (String[]args) {
		TowerofHanoi(n);
	}
	}
	
	
	
	
	

