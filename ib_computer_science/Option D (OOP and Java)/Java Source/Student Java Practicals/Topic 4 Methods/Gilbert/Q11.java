package work;
import javax.swing.JOptionPane;
import java.util.Random;
public class Q11 {
	public static int betmoney(int point) {
		String sbet = JOptionPane.showInputDialog("You have "+point+" points\nEnter a bet:");
		int bet = Integer.parseInt(sbet);
		return bet;
	}
	public static boolean check(int point, int bet) {
		if (point > bet) {
			return true;
		}
		else {
			JOptionPane.showMessageDialog(null, "You can't bet more than you have");
			return false;
		}
	}
	public static int[] gamble(int bet){
		Random rand = new Random();
		int dice1 = rand.nextInt(6);
		int dice2 = rand.nextInt(6);
		int dicesum = dice1+dice2;
		int[] myarray = new int[] {dice1,dice2,dicesum};
		return myarray;
	}
	public static int gambleresult(int point,int bet) {
		int[] dicelist = gamble(bet);
		if (dicelist[2]%2==0) {
			JOptionPane.showMessageDialog(null, "You rolled "+dicelist[0]+" and a "+dicelist[1]+" for a total of "+" "+dicelist[2]+"\nYou lose!\nYou have "+point+" points left!");
			return point;
		}
		else {
			point = point + bet*2;
			JOptionPane.showMessageDialog(null, "You rolled "+dicelist[0]+" and a "+dicelist[1]+" for a total of "+" "+dicelist[2]+"\nYou win!\nYou have "+point+" points left!");
			return point;
		}

	}
	public static void main(String[] args) {
		JOptionPane.showMessageDialog(null,"Welcome to the Odd/Even game");
		boolean flag = false;
		int point = 1000;
		while(flag==false) {
			int bet = betmoney(point);
			boolean moneycheck = true;
			moneycheck = check(point, bet);
			if (moneycheck==true) {
				point = point - bet;
				point = gambleresult(point,bet);
			}
			int dialogbutton=JOptionPane.YES_NO_OPTION;
			int dialogresult = 	JOptionPane.showConfirmDialog(null, "Do you want to play again?","Gamble",dialogbutton);
			if (dialogresult == 1){
				flag = true;
			}
		}
		JOptionPane.showMessageDialog(null, "Thank you for playing!");
	}

}
