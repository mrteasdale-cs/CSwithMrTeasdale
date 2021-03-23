// Adrian Pailler; 14/11/20; SIN//
package ADRIAN;
import javax.swing.*;
public class Q19 {

	public static void main(String[] args) {
		String SIN =JOptionPane.showInputDialog(null,"Enter SIN number:\n (9 digits) ");
		int a = Integer.parseInt(SIN.substring(0,1));
		int b = Integer.parseInt(SIN.substring(1,2));
		int c = Integer.parseInt(SIN.substring(2,3));
		int d = Integer.parseInt(SIN.substring(3,4));
		int e = Integer.parseInt(SIN.substring(4,5));
		int f = Integer.parseInt(SIN.substring(5,6));
		int g = Integer.parseInt(SIN.substring(6,7));
		int h = Integer.parseInt(SIN.substring(7,8));
		int i = Integer.parseInt(SIN.substring(8,9));
		// gets the num of each position//
		int sum = ((b*2)+(d*2)+(f*2)+(h*2))+(a+c+e+g+i);
		if(sum%10==0) {
			//sum has no remainder when divided by 10//
			JOptionPane.showMessageDialog(null,"Your SIN number is valid");
		}
		else {
			JOptionPane.showMessageDialog(null,"Your SIN number is invalid");
		}
	}
}
