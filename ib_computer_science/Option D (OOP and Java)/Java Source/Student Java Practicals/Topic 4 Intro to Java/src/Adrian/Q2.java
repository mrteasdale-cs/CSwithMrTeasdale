// Adrian Pailler; 11/11/20; Circles//
package ADRIAN;

import javax.swing.JOptionPane;

public class Q2 {

	public static void main(String[] args) {
		String input = JOptionPane.showInputDialog(null,"Enter the radius of a circle: ","Circle calculator",JOptionPane.QUESTION_MESSAGE);
		double radius = Double.parseDouble(input);
		// Gets the radius and turns it into a double//
		double circum = 2*(3.14*radius);
		double area = Math.PI*(radius*radius);
		double vol = (4* Math.PI/3)*radius*radius*radius;
		JOptionPane.showMessageDialog(null,"The circumference of the circle is: "+circum+"\n The area of the circle is:  "+area+"\n The volume of the circle is: "+vol,"circle calculator",JOptionPane.INFORMATION_MESSAGE);
	}

}
