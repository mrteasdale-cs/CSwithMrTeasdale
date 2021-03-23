import java.util.Scanner;
public class constantPi {
public static void main (String[]args) {
	final double Pi=3.1415926535;
	double radius=0;
	double area=0;
	while(radius!=999) {
		System.out.println("Enter the radius of the circle; enter 999 to exit");
		Scanner kb=new Scanner(System.in);
		radius=kb.nextDouble();
		if(radius==999) {
			System.out.println("Bye");
		}
			else {
				area=Pi*radius*radius;
				System.out.println("Area=" + area);
			}
		}
		
	}
	
}
}
