import java.util.*;
public class specificProblemAlgorithm {
	public static void main (String[]args) {
	int th= 0;
	int tl = 0;
	int ah = 0;
	int al = 0;
	String [] citynames = new String [4];
	int []hightemp = new int[4];
	int []lowtemp = new int [4];
	
	int i =0;
	
	for (i = 0; i<citynames.length;i++) {
		System.out.println("Please enter the names of the city");
		Scanner kb = new Scanner(System.in);
		citynames[i]=kb.nextLine();
		System.out.println("please enter the high temp of the city");
		hightemp[i]=kb.nextInt();
		System.out.println("please enter the low temp of the city");
		lowtemp[i]=kb.nextInt();
		th=th+hightemp[i];
		tl=tl+lowtemp[i];
		
	}
	ah=th/4;
	al=tl/4;
	
	System.out.println("Cities above average high");
	for (i=0;i<citynames.length;i++) {
		if(hightemp[i]>ah) {
			System.out.print(citynames[i] + "+" + " " );
			
			
		}
	}
		System.out.println("Cities below average high");
		for (i=0;i<citynames.length;i++) {
			if(lowtemp[i]<al) {
				System.out.print(citynames[i] + "+" + " " );
			}
	}
	}
	
	}
	
	
	
