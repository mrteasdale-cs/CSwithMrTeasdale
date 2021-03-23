// Adrian Pailler; 13/11/20; Clock  work//
package ADRIAN;

import javax.swing.JOptionPane;

public class Q18 {

	public static void main(String[] args) {
		int hr = Integer.parseInt(JOptionPane.showInputDialog(null,"Please input the hour:\n(1-12)"));
	    int min = Integer.parseInt(JOptionPane.showInputDialog(null,"Please input the minutes:\n(0-59)"));
	    //read input and parse in same line//
	    double anghr = hr*30;
	    double angmin = min*6;
	    double diff = anghr+(min*0.5);
	    // gets even movement of both hands//
	    JOptionPane.showMessageDialog(null,"The angle on the hour hand is: "+diff+
	    		"\nThe angle on the minute hand is: "+angmin+
	    		"\nand the time is: "+hr+" hours and "+min+" minutes.");
	}

}
