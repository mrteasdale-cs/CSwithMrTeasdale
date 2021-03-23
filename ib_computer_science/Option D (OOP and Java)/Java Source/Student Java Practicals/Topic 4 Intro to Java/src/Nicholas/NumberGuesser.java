package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class NumberGuesser {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a=0;
		String UserNumber = JOptionPane.showInputDialog(null, "Enter a number from 1-100");
		int number=Integer.parseInt(UserNumber);
		int min=1;
		int max=100;
		int range = (max - min) + 1;
		int counter=0;
		int guess=(int)(Math.random() * range) + min;
		while(a==0) {
			counter+=1;
			String input = JOptionPane.showInputDialog(null, "Is your number "+guess+" . Enter H for higher. Enter C for correct. Enter L for lower.");
			if(input.contains("H")){
				min=guess+1;
			}
			else if(input.contains("L")){
				max=guess-1;
				
			}
			else if(input.contains("C")) {
				JOptionPane.showMessageDialog(null, "It took me "+counter+" tries to get the correct number, which was "+guess);
				break;
			}
			range = (max - min) + 1;
			guess=(int)(Math.random() * range) + min;
			System.out.println("lower than "+max);
			System.out.println("greater than "+min);
			System.out.println("guess is "+guess);
			
		}

	}


}
