// Adrian Pailler; 12/11/20; Math is life! //
package ADRIAN;
import javax.swing.*;
public class Q5 {

	public static void main(String[] args) {
		JTextField one = new JTextField(5);
		JTextField two = new JTextField(5);
		JTextField three = new JTextField(5);	
		Object [] constants = {
				"Input constant a: ",one,
				"Input constant b: ",two,
				"Input constant c: ",three
		};
		// creates three inputs one,two,three//
		JOptionPane.showConfirmDialog(null, constants,"Please enter the values",JOptionPane.INFORMATION_MESSAGE);
		 	String alpha = one.getText();
		 	String beta = two.getText();
		 	String charlie = three.getText();
		 	// changed inputs to variables//
		 	double a = Double.parseDouble(alpha);
		 	double b = Double.parseDouble(beta);
		 	double c = Double.parseDouble(charlie);
		 	//Start of calc section//
		 	double deter = (b*b)-(4*(a*c));
		 	double sqrt = Math.sqrt(deter);
		 	// split into + and -//
		 	double pos = -b+sqrt;
		 	double neg = -b-sqrt;
		 	double posans = pos/(2*a);
		 	double negans = neg/(2*a);
		 	// end of calc section//
		 	JOptionPane.showMessageDialog(null,"For the values: \n a= "+a+"\n b= "+b+"\n c= "+c+"\n The positive root is: "+posans+"\n The negative root is: "+negans);
		 	

	}

}
