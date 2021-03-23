// Adrian Pailler; 12/11/20; Larry burger//
package ADRIAN;

import javax.swing.*;
// * since using textfields//
public class Q4 {

	public static void main(String[] args) {
		JTextField burger = new JTextField(5);
		JTextField fries = new JTextField(5);
		JTextField sodas = new JTextField(5);	
		// Declaring of the 3 text fields that will feature in the option panel
		Object [] larry = {
				"Burgers: ", burger,
				"Fries: ", fries,
				"sodas: ", sodas
				};
		// Larry is the component which creates the three input sections and therefore I added the three variables into the object array I want them//
		JOptionPane.showConfirmDialog(null, larry, "Please enter order ",JOptionPane.INFORMATION_MESSAGE);
		String a = burger.getText();
		String b = fries.getText();
		String c = sodas.getText();
		// gets the values from the inputs//
		double Pa = Double.parseDouble(a);
		double Pb = Double.parseDouble(b);
		double Pc = Double.parseDouble(c);
		double brg = Pa*1.49;
		double frs = Pb*0.89;
		double sd = Pc*0.99;
		double sum = brg+frs+sd;
		double tax = sum*1.13;
		// does all the necessary calculations//
		String input = JOptionPane.showInputDialog(null, "Enter the cash tendered: ", "Payment", JOptionPane.INFORMATION_MESSAGE);
		double cash = Double.parseDouble(input);
		double chng = cash-tax;
		JOptionPane.showMessageDialog(null, "Your order is: \n Burgers: "+a+" \n Fries: "+b+" \n Sodas: "+c+" \n Cash tendered: "+cash+" \n Sub-Total: "+sum+" \n Total: "+tax+" \n Change: "+chng);
		
		
		}
		
		
		

	}
