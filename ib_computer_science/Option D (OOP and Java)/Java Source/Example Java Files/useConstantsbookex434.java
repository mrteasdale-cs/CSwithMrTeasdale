import java.util.Scanner;
public class useConstantsbookex434 {
public static void main (String[]args ) {
	final double Pi=3.1415926535;
	double ratio =0;
	double area=0;
		while(ratio!=999) {
			System.out.println("Enter the ratio of the circle; enter 999 to exit");
			Scanner kb = new Scanner (System.in);
					ratio =kb.nextDouble();
			if (ratio==999) {
				System.out.println("See you");
			}
			else {
				area=Pi*ratio*ratio;
				System.out.println("area=" + area);
			}
	}
			
}
}
