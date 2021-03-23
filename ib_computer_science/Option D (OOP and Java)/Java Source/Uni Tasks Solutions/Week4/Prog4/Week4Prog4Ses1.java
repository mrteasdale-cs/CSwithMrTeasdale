/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **
 **  Student ID : 010125                     **
 **  Date       : 20/10/08                   **
 **  Description: Multiple selection program **
 **********************************************/ 

import javax.swing.*;

class Week4Prog4Ses1 
{
  public static void main(String[] args)
  {
  	
  	
  	
  	 String input = JOptionPane.showInputDialog(null,"Enter Value of Property",
  								"Input", JOptionPane.INFORMATION_MESSAGE);
  								
  								
  	 String input2 = JOptionPane.showInputDialog(null,"Enter Age of Property",
  								"Input", JOptionPane.INFORMATION_MESSAGE);
  	
  	  int policy = Integer.parseInt(input);
  	  int age = Integer.parseInt(input2);
      
     
      int normalpolicy = policy/600;
      
      
      
      if (age > 100)
      
      {
      
      	normalpolicy = normalpolicy + 100; 
      	  
      	String ques = JOptionPane.showInputDialog(null,"Has you property suffered subsidence",
  								"HEW", JOptionPane.QUESTION_MESSAGE);
      	
    
      	
      	if (reply = true)

      {
      	JOptionPane.showMessageDialog(null,"Soz ew");
      }
      else 
      {
      	JOptionPane.showMessageDialog(null,"Normal Policy: \t " + normalpolicy);
      }
      
  }
      }
      }
     
      
     
      

      	
      	
     







  

