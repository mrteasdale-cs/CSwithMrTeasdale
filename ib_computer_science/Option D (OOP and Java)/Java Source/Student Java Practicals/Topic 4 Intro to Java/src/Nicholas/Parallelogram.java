package nicholas1;

import java.util.Scanner;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class Parallelogram {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner keyboard = new Scanner (System.in);
		StringBuilder str = new StringBuilder("");
		StringBuilder space = new StringBuilder("");
		String bc = JOptionPane.showInputDialog(null, "Which Character do u want to display");
		String word=JOptionPane.showInputDialog(null, "How many numbers horizontally");
		String horizontal1=JOptionPane.showInputDialog(null, "How many numbers vertically");
		int horizontal=Integer.parseInt(horizontal1);
		
		String Space=" ";
		int vertical= Integer.parseInt(word);
		//String repeated4 = bc.repeat(horizontal);
		//str.append(repeated4);
		//System.out.println(Space.repeat(vertical-1)+repeated4);
		for(int d=2; d<vertical; d++) {
			//String final1 = Space.repeat(horizontal-2);
			//System.out.println(Space.repeat(vertical-d)+bc+final1+bc);
		
		}
					
		
		System.out.println(str);
	}
}
	


