/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **         
 **  Student ID : 010125                     **       
 **  Date       : 23/10/08                   **      
 **  Course     : Computer Forensics F2      **    
 **  Description:Calculates absoulted value  **   
 **     of a given number                    **	
 **              							 **       
 **********************************************/


import javax.swing.JOptionPane;

public class Week4Prog1Ses2
{
   public static void main(String[] args) 
   {
        int num, temp;
        String input;
        
        input = JOptionPane.showInputDialog("Enter a number");
        num = Integer.parseInt(input);
        
        temp = num;
        if (num < 0);
        	temp = - num;
        
        JOptionPane.showMessageDialog(null, "The absolute value of "+ num + " is "+temp);
    }
}
