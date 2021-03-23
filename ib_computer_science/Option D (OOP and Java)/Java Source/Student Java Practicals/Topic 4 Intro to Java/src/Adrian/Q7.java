// Adrian Pailler; 12/11/20; Humidex //
package ADRIAN;

import javax.swing.*;

public class Q7 {

	public static void main(String[] args) {
		JTextField dew = new JTextField(5);
		JTextField air = new JTextField(5);	
		Object [] constants = {
				"Enter the Dew Point(D):  ",dew,
				"Enter the air temperature(T): ",air
		};
		// creates three inputs one,two,three//
		JOptionPane.showConfirmDialog(null, constants,"Humidex calculator",JOptionPane.INFORMATION_MESSAGE);
		 	String a = dew.getText();
		 	String b = air.getText();
		 	// changed inputs to variables//
		 	double d = Double.parseDouble(a);
		 	double t = Double.parseDouble(b);
		 	double r = 6.11*(java.lang.Math.exp(5417.7530*((1/273.16)-(1/(273.16+d)))));
		 	double h = (0.5555)*(r-10.0);
		 	double hum = t+h;
		 	JOptionPane.showMessageDialog(null,"The humidex is: "+hum,"Humidex calculator",JOptionPane.INFORMATION_MESSAGE);
	}

}
