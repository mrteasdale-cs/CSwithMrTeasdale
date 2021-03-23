package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class Lotto649 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String NumberDraws = JOptionPane.showInputDialog(null, "How many draws?");
		StringBuilder str1 = new StringBuilder("");
		int max=49;
		int min=1;
		int range = (max - min) + 1;
		int draws=Integer.parseInt(NumberDraws);
		int a[] = new int [draws];
		for(int i=0;i<draws;i++) {
			StringBuilder str = new StringBuilder("");
			for(int b=0;b<6;b++) {
				str.append(Integer.toString((int)(Math.random() * range) + min)+", ");
	
			}
			/**
			 * appends 6 numbers to string which are split by comma
			 */
			str1.append(str+"\n");
		}
		/**
		 * appends all strings from previous output to new string
		 */
		JOptionPane.showMessageDialog(null, "Your numbers: \n"+str1);
		
		

	}

}
