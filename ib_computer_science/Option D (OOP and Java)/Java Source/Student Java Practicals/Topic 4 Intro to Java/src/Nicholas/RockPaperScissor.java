package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class RockPaperScissor {

	public static void main(String[] args) {
		int a =0;
		String comp="";
		String action = JOptionPane.showInputDialog(null, "Rock (R), Paper (P) or Scissors (S)");
		int computer=1+(int)(Math.random()*((3-1)+1));
		int chance=1+(int)(Math.random()*((2-1)+1));
		if(action.contains("R")) {
			 a=1;
			 action="Rock";
			comp="Paper";
		}
		if(action.contains("P")) {
			a=2;
			action="Paper";
			comp="Scissors";
	
		}
		if(action.contains("S")) {
			a=3;
			action="Scissors";
			comp="Rock";
		}
		if(a==computer) {
			JOptionPane.showMessageDialog(null, "You win. You picked "+comp+" and the computer picked "+action);
			
		}
		
		else if(chance==2){
			JOptionPane.showMessageDialog(null, "You lost because the computer picked "+comp+" and you picked "+action);
		}
		else if(chance==1) {
			JOptionPane.showMessageDialog(null, "You draw because the computer picked "+ action+" and you picked "+action );
		}
	
	
		System.out.println(computer+" "+chance);
		// TODO Auto-generated method stub

	}

}
