package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class NecklaceProblem {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String UserNumber1 = JOptionPane.showInputDialog(null, "Enter your first 1 digit number");
		String UserNumber2 = JOptionPane.showInputDialog(null, "Enter your second 1 digit number");
		int num1=Integer.parseInt(UserNumber1);
		int num2=Integer.parseInt(UserNumber2);
		int a=0;
		int counter=2;
		int sum=0;
		int printnumber=0;
		System.out.println("Your first number was "+UserNumber1);
		System.out.println("Your second number was "+UserNumber2);
		System.out.print(num1+", ");
		System.out.print(num2+", ");
		while(printnumber!=Integer.parseInt(UserNumber2)) {
		sum=num1+num2;
		String SumString=Integer.toString(sum);
		if(SumString.length()==2) {
			String digit2=Character.toString(SumString.charAt(1));
			printnumber=Integer.parseInt(digit2);
		}
		else {
			printnumber=sum;
		}
		System.out.print(printnumber+", ");
		num1=num2;
		num2=printnumber;
		counter+=1;
		
		
		

	}
		System.out.println("This took "+counter+" steps.");

}
}
