// Adrian Pailler; 12/11/20; airports //
package ADRIAN;

import javax.swing.*;

public class Q8 {

	public static void main(String[] args) {
		JTextField one = new JTextField();
		JTextField two = new JTextField();
		JTextField three = new JTextField();
		JTextField four = new JTextField();
		JTextField five = new JTextField();
		JTextField six = new JTextField();
		Object [] constants = {
				"Enter starting aiport IATA code:  ",one,
				"Enter starting airport latitude: ",two,
				"Enter starting airport longitude: ",three,
				"Enter ending airport IATA code: ",four,
				"Enter ending airport latitude: ",five,
				"Enter ending airport longitude: ",six
		};
		// creates six inputs//
		JOptionPane.showConfirmDialog(null, constants,"Distance calculator",JOptionPane.INFORMATION_MESSAGE);
		String loca = one.getText();
		String locb = four.getText();
		 	String alpha = two.getText();
		 	String beta = three.getText();
		 	String charlie = five.getText();
		 	String delta = six.getText();
		 	final double r = 6371;
		 	// changed inputs to variables//
		 	double lata = Double.parseDouble(alpha);
			double longa = Double.parseDouble(beta);
			double latb = Double.parseDouble(charlie);
			double longb = Double.parseDouble(delta);
			double d = r*Math.acos((Math.sin(latb))*(Math.sin(lata))+(Math.cos(latb))*(Math.cos(lata))*(Math.cos(longb-longa)));
			JOptionPane.showMessageDialog(null,"The distance between "+loca+" and "+locb+" is: "+d+"km","Distance calculator",JOptionPane.INFORMATION_MESSAGE);	
	}

}
