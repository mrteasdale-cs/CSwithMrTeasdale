// Adrian Pailler; 11/11/20; time calc//
package ADRIAN;

import javax.swing.JOptionPane;

public class Q3 {

	public static void main(String[] args) {
		String time = JOptionPane.showInputDialog(null,"Please enter the total time (in seconds)","Input",JOptionPane.QUESTION_MESSAGE);
		int total = Integer.parseInt(time);
		int hour = total/360;
		int min = (total%120)/60;
		int sec = (total%120)%60;
		// Takes the seconds and divides it firstly converts it into hours. The remainder is converted into min and the remainder of that is the seconds//
		JOptionPane.showMessageDialog(null,"For the total time of: "+total+" seconds, the breakdown is: \n Hours:"+hour+"\n Minutes: "+min+"\n Seconds: "+sec,"Input",JOptionPane.INFORMATION_MESSAGE);
		

	}

}
