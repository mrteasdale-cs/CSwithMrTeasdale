/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **         
 **  Student ID : 010125                     **       
 **  Date       : 23/10/08                   **      
 **  Course     : Computer Forensics F2      **    
 **  Description: Sorts 3 integers into    	 **   
 **                acending order            **	
 **              							 **       
 **********************************************/


import javax.swing.*;

public class Week4Prog6Ses2
{
	 
	 public static void main(String[] args) 
	 {
		
		char small, middle, large;	

        String input1 = JOptionPane.showInputDialog("Enter the first character");
        char char1 = input1.charAt(0);
        
        String input2 = JOptionPane.showInputDialog("Enter the second character");
        char char2 = input2.charAt(0);
        
        String input3 = JOptionPane.showInputDialog("Enter the third character");
        char char3 = input3.charAt(0);
        
		if (char1>char2)
	    {
	  	     large = char1;
	   		 small = char2;
	  	}
	  	else
	  	{
	  	     large = char2;
	  	     small = char1;
	  	}
	  	if (char3>large)
	  	{
	  		middle = large;
	  		large = char3;	  	
	  	}
	  	else if (char3<small)
	  	{
	  		middle = small;
	  		small = char3;
	  	}
	  	else 
	  	{
	  		middle = char3;	
	    }
	    { 
	    JOptionPane.showMessageDialog(null,"The Numbers You Entered Were: "+char1+"  "+char2+"  "+char3+"  "+"\n"+"In Acending Order: \n" + small+ "\n" + middle +"\n"+ large);	  
	    }      	        	        	              	
   	 }	
}