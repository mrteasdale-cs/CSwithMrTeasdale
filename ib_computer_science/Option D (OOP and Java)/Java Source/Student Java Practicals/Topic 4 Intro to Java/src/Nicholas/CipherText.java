package nicholas1

;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 * This program allows the user to enter a key between one and 10 and encrypt and decrypt messages using it.
 */
public class CipherText {

	public static void main(String[] args) {
		String final1="";
		// TODO Auto-generated method stub
		String action = JOptionPane.showInputDialog(null, "Encrypt(E), Decrypt(D), or Out(O)?");
		String alphabet="- ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,qazwsxedcrfvtgbyhnujmikolp123456789*;:_";
		String keys = JOptionPane.showInputDialog(null, "Enter the key (between 1 and 10)");
		StringBuilder str = new StringBuilder("");
		int key=Integer.parseInt(keys);
		if(action.contains("E")) {
			String message = JOptionPane.showInputDialog(null, "Enter your message here");
			String MessageCaps=message.toUpperCase();
			for(int i=0;i<MessageCaps.length();i++) {
				if(key<11) {
				if(alphabet.contains(Character.toString(MessageCaps.charAt(i)))) {
					int Alph=alphabet.indexOf(MessageCaps.charAt(i));
					str.append(alphabet.charAt(Alph*2+key-2));
					}
				/**
				 * This goes through each character in the message and returns the index in the string alphabet of it.
				 * Then it appends the index gone through a encryption equation so it'll append a different index.
				 */
				}
				else {
						JOptionPane.showMessageDialog(null, "Please enter a key in the range 1-10");
					}
				/**
				 * If key is greater than 10 program breaks. User specifically asked for key in range 1-10.
				 */
			}
		}
		if(action.contains("D")){
			String dmessage = JOptionPane.showInputDialog(null, "Enter your message here");
			String dmessagecaps=dmessage.toUpperCase();
			for(int b=0;b<dmessagecaps.length();b++) {
				if(key<11) {
				if(alphabet.contains(Character.toString(dmessage.charAt(b)))) {
					int Alphb=alphabet.indexOf(dmessage.charAt(b));
						str.append(alphabet.charAt((Alphb-key+2)/2));
					}
				/**
				 * Encrypted UserMessage is entered and returns the index of each character that is present in the strign alphabet.
				 * Reverse encodes through solving math equation for variable Alph
				 */
				}
				else {
						JOptionPane.showMessageDialog(null, "Please enter a key in the range 1-10");
					}
					}
			}
		if(action.contains("O")){
			System.out.println("Bye!");
			}
			System.out.println("The enrcypted message is: "+str);
			}
	}




