/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **         
 **  Student ID : 010125                     **       
 **  Date       : 23/10/08                   **      
 **  Course     : Computer Forensics F2      **    
 **  Description:   **   
 **                                **	
 **              							 **       
 **********************************************/


import javax.swing.JOptionPane;

public class Week4Prog4Ses2
{
	 
	 public static void main(String[] args) 
	 {
	
		int temp;
	
        String input1 = JOptionPane.showInputDialog("Enter the first number");
        int num1 = Integer.parseInt(input1);
        
        String input2 = JOptionPane.showInputDialog("Enter the second number");
        int num2 = Integer.parseInt(input2);
	
	temp = num1;
	num1 = num2;
	num2 = temp;

		{
  			JOptionPane.showMessageDialog(null,"Number 1 is : " + num1);
		}
       	{
  			JOptionPane.showMessageDialog(null,"Number 2 is : " + num2);
		}
       	    
       	        	        	        	              	
   	 }	
}