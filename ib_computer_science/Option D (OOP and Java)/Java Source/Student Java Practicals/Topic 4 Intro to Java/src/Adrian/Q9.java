// Adrian Pailler; 12/11/20; school time //
package ADRIAN;

import javax.swing.*;

public class Q9 {

	public static void main(String[] args) {
		JTextField one = new JTextField();
		JTextField two = new JTextField();
		JTextField three = new JTextField();
		JTextField four = new JTextField();
		JTextField five = new JTextField();
		JTextField six = new JTextField();
		Object [] constants = {
				"Enter your birth day:  ",one,
				"Enter your birth month:\n (January is 1 - December is 12) ",two,
				"Enter your birth year:\n (4 digits) ",three,
				"Enter the current day: ",four,
				"Enter current month:\n (January is 1 - December is 12) ",five,
				"Enter current year:\n (4 digits) ",six
		};
		// creates six inputs//
		JOptionPane.showConfirmDialog(null, constants,"school-time calculator",JOptionPane.INFORMATION_MESSAGE);
		String alpha = one.getText();
		String beta = two.getText();
		 	String charlie = three.getText();
		 	String delta = four.getText();
		 	String echo = five.getText();
		 	String fred = six.getText();
		 	// changed inputs to variables//
		 	int bday = Integer.parseInt(alpha);
			int bmn = Integer.parseInt(beta);
			int byr = Integer.parseInt(charlie);
			int cday = Integer.parseInt(delta);
			int cmn = Integer.parseInt(echo);
			int cyr = Integer.parseInt(fred);
			int dschool = (200*((cday/365)+(cyr)+(cmn/12)-(byr)-(bday/365)-(bmn/12)))*6;
			// gets the hours in school//
			int min = dschool*60;
			int sec = min*60;
			// unit conversion//
			JOptionPane.showMessageDialog(null,"The time spent in class is: \n Total Hours: "+dschool+"\n Or \n in minutes: "+min+"\n in seconds"+sec,"School-time calculator",JOptionPane.INFORMATION_MESSAGE);
	}

}
