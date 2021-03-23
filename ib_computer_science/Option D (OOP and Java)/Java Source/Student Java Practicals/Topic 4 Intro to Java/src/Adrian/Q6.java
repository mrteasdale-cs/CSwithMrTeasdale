// Adrian Pailler; 12/11/20; Final V calc //
package ADRIAN;

import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class Q6 {

	public static void main(String[] args) {
		JTextField one = new JTextField(5);
		JTextField two = new JTextField(5);
		JTextField three = new JTextField(5);	
		Object [] constants = {
				"Enter initial velocity (m/s):  ",one,
				"Enter acceleration (m/s^2): ",two,
				"Enter distance (m): ",three
		};
		// creates three inputs one,two,three//
		JOptionPane.showConfirmDialog(null, constants,"Final V calculator",JOptionPane.INFORMATION_MESSAGE);
		 	String alpha = one.getText();
		 	String beta = two.getText();
		 	String charlie = three.getText();
		 	// changed inputs to variables//
		 	double v = Double.parseDouble(alpha);
		 	double a = Double.parseDouble(beta);
		 	double d = Double.parseDouble(charlie);
		 	double fv = Math.sqrt((v*v)+(2*(a*d)));
		 	// calculation//
		 	JOptionPane.showMessageDialog(null,"The finaly velocity is: "+fv+"m/s");

	}

}
