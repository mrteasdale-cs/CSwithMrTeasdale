// Adrian Pailler; 14/11/20; card game//
package ADRIAN;

import java.util.*;
import javax.swing.*;

public class Q20 {

	public static void main(String[] args) {
		ArrayList<Integer> set = new ArrayList<Integer>();
		ArrayList<Integer> ai = new ArrayList<Integer>();
		JFrame game = new JFrame();
		String[] options = new String[3];
		options[0] = new String("Hit");
	    options[1] = new String("Stand");
		options[2] = new String("Leave");
		// creates three options//
		
		
		
		for(int i=0;i<3;i++) {
			int deal =  (int) (Math.random()*(10-0)+1);
			ai.add(deal);
		}
			int dealtotal = ai.get(0)+ai.get(1)+ai.get(2);
			// dealer cards//
			
			
			
		for(int a=0;a<2;a++) {
		int user =  (int) (Math.random()*(10-0)+1);
		set.add(user);
		}
		// gets player first 2 cards//
		
		int total = set.get(0)+set.get(1);
	    int ans =JOptionPane.showOptionDialog(game.getContentPane(),"Welcome to Twenty one!\n\nYour cards are :"+set+"\nfor a total of: "+total+"\nThe dealer has three cards (not showing)","Disclaimer: I do not promote gambling",0,JOptionPane.INFORMATION_MESSAGE,null,options,null);
		//0 hit;1 stand;2 leave//
	    int num = 0;
	    int i =2;
	    boolean dealt = false;
	    while(ans==0) {
	    	num =  (int) (Math.random()*(10-0)+1);
	    	set.add(num);
	    	total+=num;
	    	i= i+1;
	    	if(i==5) {
	    		dealt=true;
	    		break;
	    }
		    ans	= JOptionPane.showOptionDialog(game.getContentPane(),"Welcome to Twenty one!\n\nYour cards are :"+set+"\nfor a total of: "+total+"\nThe dealer has three cards (not showing)","Disclaimer: I do not promote gambling",0,JOptionPane.INFORMATION_MESSAGE,null,options,null);
	    }
	 // allows up to 3 hits//
	    if(ans!=2) {
	    
	    			if(total>21&&dealtotal<=21) {
		    		JOptionPane.showMessageDialog(null,"You went bust with "+total+" , dealer has "+dealtotal,"Disclaimer: I do not promote gambling",JOptionPane.INFORMATION_MESSAGE);	 
		    	}
	    			if(dealtotal>total&&dealtotal<=21&&total<21) {
		    		JOptionPane.showMessageDialog(null,"You lose with "+total+" ,dealer had "+dealtotal,"Disclaimer: I do not promote gambling",JOptionPane.INFORMATION_MESSAGE);
		    	}
	    			if(dealtotal==total || total>21&&dealtotal>21) {
		    		JOptionPane.showMessageDialog(null,"You draw with "+total+" ,dealer had "+dealtotal,"Disclaimer: I do not promote gambling",JOptionPane.INFORMATION_MESSAGE);
		    	}
	    			if(dealtotal>21&&total<=21) {
		    		JOptionPane.showMessageDialog(null,"You win with "+total+" ,dealer went bust with "+dealtotal,"Disclaimer: I do not promote gambling",JOptionPane.INFORMATION_MESSAGE);
		    	}
	    			if(total>dealtotal&&total<=21&&dealtotal<21) {
		    		JOptionPane.showMessageDialog(null,"You win with "+total+" ,dealer had "+dealtotal,"Disclaimer: I do not promote gambling",JOptionPane.INFORMATION_MESSAGE);
			  }
	    }
	    }			
	    	}

