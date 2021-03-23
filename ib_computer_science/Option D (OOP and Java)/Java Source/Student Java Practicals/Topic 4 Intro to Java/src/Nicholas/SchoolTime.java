package nicholas1;

import java.util.Scanner;

import javax.swing.JOptionPane;

/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class SchoolTime {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String birthyear = JOptionPane.showInputDialog(null, "What year were you born? (4digits)");
		int birthy = Integer.parseInt(birthyear);
		String birthmonth = JOptionPane.showInputDialog(null, "What month were you born?(1-12)");
		int birthm = Integer.parseInt(birthmonth);
		String birthday = JOptionPane.showInputDialog(null, "What day were you born?");
		int birthd = Integer.parseInt(birthday);
		String CurrentYear=JOptionPane.showInputDialog(null, "What year is it? (4digits)");
		int year=Integer.parseInt(CurrentYear);
		String CurrentMonth=JOptionPane.showInputDialog(null, "What month is it? (1-12)");
		int month=Integer.parseInt(CurrentMonth);
		String CurrentDay=JOptionPane.showInputDialog(null, "What day is it?");
		int day=Integer.parseInt(CurrentDay);
		int yearattendhour=(year-birthy-4)*10*20*6;
		int monthattendhour=(month-birthm)*20*6;
		int dayattendhour=(day-birthd)*6;
		int hours=yearattendhour+monthattendhour+dayattendhour;
		System.out.println("You've spent "+hours+" hours in school");
		
		
		

	}

}
