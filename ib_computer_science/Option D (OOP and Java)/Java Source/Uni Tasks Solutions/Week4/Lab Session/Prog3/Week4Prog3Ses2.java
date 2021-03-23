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

public class Week4Prog3Ses2
{
	 
	 public static void main(String[] args) 
	 {
	
	    //int num1, num2;
        //String input1, input2;
        
        String input1 = JOptionPane.showInputDialog("Enter the first number");
        int num1 = Integer.parseInt(input1);
        
        String input2 = JOptionPane.showInputDialog("Enter the second number");
        int num2 = Integer.parseInt(input2);
        
        if (num1 < num2)
        {
       		JOptionPane.showMessageDialog(null,"Number 1  : " + num1 + "\n" + "Number 2  : " + num2 + "\n" + "The Second Number " + 
       		"is Bigger than the First Number ");   	
        } 	
        if (num1 > num2)
        {
       		JOptionPane.showMessageDialog(null,"Number 1  : " + num1 + "\n" + "Number 2  : " + num2 + "\n" + "The First Number " + 
       		"is Bigger than the Second Number ");   	
        }	          
        if (num1 == num2)
        {
       		JOptionPane.showMessageDialog(null,"Number 1  : " + num1 + "\n" + "Number 2  : " + num2 + "\n" + "The Numbers " + 
       		"are Equal my Friend!!! ");   	
        }	               	        	        	        	              	
   	 }	
}