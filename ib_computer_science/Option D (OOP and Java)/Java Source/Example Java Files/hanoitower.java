import java.util.*;

public class hanoitower {
		int num = 5;
	
		Stack<Integer> SPa = new Stack<Integer>();
		Stack<Integer> SPb = new Stack<Integer>();
		Stack<Integer> SPc = new Stack<Integer>();
		Stack<Integer> SPd = new Stack<Integer>();
		Object[] daa = new Object[10];
		Object[] dbb = new Object[10];
		Object[] dcc = new Object[10];
		Stack[] pegs = {SPa,SPb,SPc,SPd};
		
		int a = 1;
		int b = 2;
		int c = 3;
		Object t = 0;
		int n = 0;
		int m = 0;
		
		String da = "";
		String db = "";
		String dc = "";
		
		String f1 = " ";
		String f2 = " ";
		String f3 = " ";
	
	@SuppressWarnings("unchecked")
	public void move (int n,int a, int b, int c) {
		if (n > 0) {
			move(n-1,a,c,b);
			t = pegs[a].pop();
			pegs[c].push(t);
			
			display();
			move(n-1,b,a,c);
		}
	}
	
	@SuppressWarnings("unchecked")
	public void display() {
		System.out.println("");
		System.out.println("| A | B | C |");
		for (int i=0; i<(num);i++) {
			if (!pegs[1].isEmpty()) {
				daa[i] = pegs[1].pop();
			}
			else {
				daa[i]=null;
			}
			if (!pegs[2].isEmpty()) {
				dbb[i] = pegs[2].pop();
			}
			else {
				dbb[i]=null;
			}
			if (!pegs[3].isEmpty()) {
				dcc[i] = pegs[3].pop();
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
			pegs[1].push(daa[m]);
			pegs[2].push(dbb[m]);
			pegs[3].push(dcc[m]);
		}
	}
	
	//Start point
	public void towerhanoi(int n) {
		
		for (int i=0;i<(n);i++) {
			m = n - i;
			pegs[1].push(m);
		}
		
		display();
		move(n,1,2,3);
	}
public static void main (String[]args) {
	towerhanoi(n);
}
}

