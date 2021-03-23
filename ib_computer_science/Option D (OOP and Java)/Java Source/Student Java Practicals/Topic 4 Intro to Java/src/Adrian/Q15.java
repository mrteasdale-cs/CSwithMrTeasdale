// Adrian Pailler; 13/11/20; class grades//
package ADRIAN;
import java.util.*;
import javax.swing.*;

public class Q15 {

	public static void main(String[] args) {
		ArrayList<Double> grades = new ArrayList<Double>();
		ArrayList<Double> fail = new ArrayList<Double>();
		// creates two arrays with double values//
		for(int counter = 0;counter<20;counter++) {
			double stu= Double.parseDouble(JOptionPane.showInputDialog(null,"Enter your grade"));
			if(stu>100 || stu<0) {
				JOptionPane.showMessageDialog(null,"Invalid entry. Try again");
				break;
				// break if invalid score//
			}
			if(stu<50) {
				fail.add(stu);
			}
			grades.add(stu);
			// sorts the scores into both arrays
			}
		double sum = grades.get(0)+grades.get(1)+grades.get(2)+grades.get(3)+grades.get(4)+grades.get(5)+grades.get(6)+grades.get(7)+grades.get(8)+grades.get(9)+grades.get(10)+grades.get(11)+grades.get(12)+grades.get(13)+grades.get(14)+grades.get(15)+grades.get(16)+grades.get(17)+grades.get(18)+grades.get(19);
		//adds all elements//
		double avg = sum%20;
		int pass = grades.size()-fail.size();
		// subtracts all students by failed//
		int disapointments = fail.size();
		JOptionPane.showMessageDialog(null,"Out of 20  students," +pass+" passed and "+disapointments+" failed. The average score was "+avg+"%");
	}
	}

