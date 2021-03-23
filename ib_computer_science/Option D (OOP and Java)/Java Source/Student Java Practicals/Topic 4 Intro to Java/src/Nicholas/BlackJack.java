package nicholas1;

import javax.swing.JOptionPane;

public class BlackJack {

	public static void main(String[] args) {
		int condition=0;
		int dealersum=0;
		StringBuilder str = new StringBuilder("");
		StringBuilder strdealer = new StringBuilder("");
		int max=11;
		int dealernumber=0;
		int min=1;
		int range = (max - min) + 1;
		int number3=0;
		int bc=0;
while(bc==0) {
	int number1=(int)(Math.random() * range) + min;
	int number2=(int)(Math.random() * range) + min;
	int numberamount=2;
	str.append(number1+", "+number2+", ");
	int sum=number1+number2;
		while(condition==0) {
			
			String action = JOptionPane.showInputDialog(null, "Welcome to twenty one \n \n Your cards are "+str+" for a total of "+sum+"\n"+"The Dealer has three cards (not showing)\n  What do you want to do?Hit(H) or Stand(S) or Leave(L)?");
			while(dealersum<16) {
				dealernumber=(int)(Math.random() * range) + min;
				strdealer.append(dealernumber+", ");
				dealersum+=dealernumber;
				
			}
			if(action.contains("H")) {
				number3=(int)(Math.random() * range) + min;
				sum+=number3;
				str.append(number3+", ");
				if(sum>21) {
					JOptionPane.showMessageDialog(null, "You loose because your cards add up to "+sum);
					break;
					
				}
				}
			else if(action.contains("S")){
				if(dealersum>sum) {
					if(dealersum>21) {
						JOptionPane.showMessageDialog(null, "You win because dealers cards add up to "+dealersum);
						break;
					}
					else if(dealersum==sum) {
						JOptionPane.showMessageDialog(null, "You win because dealers cards add up to "+dealersum+" and you have the same as the dealer");
						break;
					}
					else {
						
					
					JOptionPane.showMessageDialog(null, "Dealer had "+dealersum+" while you had "+sum+". You loose");
					break;
					
				}
				}
				else {
					JOptionPane.showMessageDialog(null, "Dealer had "+dealersum+" while you had "+sum+". You win");
					break;
				}

			}
			else if(action.contains("L")) {
				System.exit(0);
			}
			

	
		}
		str.setLength(0);
}
}
}
