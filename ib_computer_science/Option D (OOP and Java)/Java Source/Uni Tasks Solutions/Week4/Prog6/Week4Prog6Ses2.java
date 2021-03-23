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
		
		int small, middle, large;	

        String input1 = JOptionPane.showInputDialog("Enter the first number");
        int num1 = Integer.parseInt(input1);
        
        String input2 = JOptionPane.showInputDialog("Enter the second number");
        int num2 = Integer.parseInt(input2);
        
        String input3 = JOptionPane.showInputDialog("Enter the third number");
        int num3 = Integer.parseInt(input3);
        
		if (num1>num2)
	    {
	  	     large = num1;
	   		 small = num2;
	  	}
	  	else
	  	{
	  	     large = num2;
	  	     small = num1;
	  	}
	  	if (num3>large)
	  	{
	  		middle = large;
	  		large = num3;	  	
	  	}
	  	else if (num3<small)
	  	{
	  		middle = small;
	  		small = num3;
	  	}
	  	else 
	  	{
	  		middle = num3;	
	    }
	    { 
	    JOptionPane.showMessageDialog(null,"The Numbers You Entered Were: "+num1+"  "+num2+"  "+num3+"  "+"\n"+"In Acending Order: \n" + small+ "\n" + middle +"\n"+ large);	  
	    }      	        	        	              	
   	 }	
}