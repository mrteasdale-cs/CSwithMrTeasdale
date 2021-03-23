// Adrian Pailler; 13/11/20; Leap year finder//
package ADRIAN;
import javax.swing.*;
public class Q11 {

	public static void main(String[] args) {
		String year = JOptionPane.showInputDialog(null,"Enter a year: ","Leap year finder",JOptionPane.DEFAULT_OPTION);
		int yr = Integer.parseInt(year);
		if(yr%4==0) {
			JOptionPane.showMessageDialog(null,yr+" is a leap year","Leap year finder",JOptionPane.DEFAULT_OPTION);
			}// if yr when divided by 4 has no remainder is leap year//
		else {
			JOptionPane.showMessageDialog(null,yr+" is not a leap year","Leap year finder",JOptionPane.DEFAULT_OPTION);
		}// if there is a remainder not leap year//

	}
}
