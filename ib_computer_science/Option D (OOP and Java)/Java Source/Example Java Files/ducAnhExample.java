import java.util.Stack;
public class ducAnhExample {


static Stack <String> SPa = new Stack<>();
static Stack <String> SPb = new Stack<>();
static Stack <String> SPc = new Stack<>();
static Stack <String> SPd = new Stack<>();
static String[] daa = {};
static String[] dbb = {};
static String[] dcc = {};
static int m;
int t;
int n=0;
static int NUM = 5;
static String da = "";
static String db = "";
static String dc = "";
static String f1="";
static String f2="";
static String f3="";
@SuppressWarnings("rawtypes")
static
Stack [] PEGS = {SPa, SPb, SPc, SPd};

	@SuppressWarnings("unchecked")
	public void TowersofHanoi(int n) {
		for (int I = 0; I < n-1; I++) {
			m = n - I;
			PEGS[1].push(m);
		}
	display();
	move(n,1,2,3);
	}
	public void move(int a, int b, int c, int d) {
		if (n>0) {
			move(n-1,a,b,c);
			t = (int) PEGS[a].pop();
			display();
			move(n-1,b,a,c);
			
		}
		
	}
	@SuppressWarnings({ "unchecked", "unused" })
	public static void display() {
		System.out.println("");
		System.out.println(" A | B | C");
		for(int I = 0; I < NUM-1; I++) {
			Stack<String>daa = (Stack<String>) PEGS[1].pop();
			Stack<String>dbb = (Stack<String>) PEGS[1].pop();
			Stack<String>dcc = (Stack<String>) PEGS[1].pop();
		}
		for (int I = 0; I<NUM-1; I++) {
			da = daa [I];
			db = dbb [I];
			dc = dcc [I];
			f1 = da.toString();
			if (f1 == null) {
				f1="-";
			}
			f2 = db.toString();
			if (f2==null) {
				f2 = "-";
			}
			f3 = dc.toString();
			if (f3==null) {
				f3 = "-";
			}
			System.out.println(" | " + f1 + " | " +f2 + " | " + f3 + " | ");
		}
		for (int I = 0; I<NUM-1; I++) {
			m = NUM-1-I;
			PEGS[1].push(daa[m]);
			PEGS[2].push(daa[m]);
			PEGS[3].push(daa[m]);
			
		}
	}
	public static void main(String[] args) {
		TowersofHanoi(n);
		
	}
	
}



