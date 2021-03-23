// Adrian Pailler; 13/11/20; Nitpickie delivery//
package ADRIAN;

import javax.swing.*;

public class Q13 {

	public static void main(String[] args) {
		JTextField one = new JTextField();
		JTextField two = new JTextField();
		JTextField three = new JTextField();
		JTextField four = new JTextField();
		Object [] constants = {
				"Enter the weight of the package in kilograms:  ",one,
				"Enter the length of the package in meters: ",two,
				"Enter the width of the package in meters:",three,
				"Enter height of the package in meters: ",four
		};
		// creates four inputs//
				JOptionPane.showConfirmDialog(null, constants,"Nitpicke delivery service",JOptionPane.INFORMATION_MESSAGE);
				    int kg = Integer.parseInt(one.getText());
				    double length = Double.parseDouble(two.getText());
				 	double width = Double.parseDouble(three.getText());
				 	double height = Double.parseDouble(four.getText());
				 	double size = length*width*height;
				 	// gets the size in cubic meters
				 	if(kg<=27&&size<=0.1) {
				 		//passes through conditions in order until one is met//
				 		JOptionPane.showMessageDialog(null,"Package accepted!\nSee you soon!");
				 	}
				 		if(kg>=27&&size<=0.1) {
				 			JOptionPane.showMessageDialog(null,"Package rejected!\nToo heavy");
				 		}
				 			if(kg>=27&&size>=0.1) {
				 				JOptionPane.showMessageDialog(null,"Package rejected!\nToo heavy and too large");
				 			}
				 			if(kg<=27&&size>=0.1) {
				 				JOptionPane.showMessageDialog(null,"Package rejected!\nToo large");
				 			}
				 		}
	}
