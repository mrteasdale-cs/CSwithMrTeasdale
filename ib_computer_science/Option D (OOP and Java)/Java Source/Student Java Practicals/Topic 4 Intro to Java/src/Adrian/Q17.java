// Adrian Pailler; 13/11/20; Rock paper scissors//
package ADRIAN;
import javax.swing.*;
public class Q17 {

	public static void main(String[] args) {
		JFrame rps = new JFrame();
		String[] options = new String[3];
		options[0] = new String("Rock");
	    options[1] = new String("Paper");
		options[2] = new String("Scissors");
	int ans =JOptionPane.showOptionDialog(rps.getContentPane(),"Let's play rock-paper-scissors","Rock paper scissors game",0,JOptionPane.INFORMATION_MESSAGE,null,options,null);
		//0 rock;1 paper;2 scissors//
		int AI = (int) (Math.random()*(2-0)+1);
		if(ans==AI) {
			JOptionPane.showMessageDialog(null,"It's a tie\n Your answer: "+options[ans]+"\n  AI's answer:	"+options[AI]);
		}
		else	if(ans==0&&AI==2 || ans==2&&AI==1 || ans==1&&AI==0) {
			JOptionPane.showMessageDialog(null,"You won\n Your answer: "+options[ans]+"\n AI's answer: "+options[AI]);
		}
		else {
			JOptionPane.showMessageDialog(null,"You lost\n Your answer:"+options[ans]+"\n AI's answer: "+options[AI]);
		}
	}
}
