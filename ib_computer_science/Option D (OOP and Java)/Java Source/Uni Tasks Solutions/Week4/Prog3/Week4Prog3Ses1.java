/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **
 **  Student ID : 010125                     **
 **  Date       : 20/10/08                   **
 **  Description: Multiple selection program **
 **********************************************/ 

import javax.swing.*;

class Week4Prog2Ses1 
{
  public static void main(String[] args)
  {
  	
  	 String usr = JOptionPane.showInputDialog(null,"Thumb Print OK Y/N",
  								"Input", JOptionPane.QUESTION_MESSAGE);
  	
  	  boolean thumb = false;
      
      if (usr.equals("Y"))
      	thumb = true;
      	
      	
     usr = JOptionPane.showInputDialog(null,"Iris Scan OK Y/N",
  								"Input", JOptionPane.QUESTION_MESSAGE);
  	
  	  boolean iris = false;
      
      if (usr.equals("Y"))
      	iris = true;
      

      
      if (thumb)
      {
      	   if (iris)
      	   {
      	   	System.out.println("Safe Open");
      	   }
      	   else 	 
      	   {
      	    System.out.println("Iris Scan Failed");
      	   }
      }	
      else  
  	  {	
  	       if (iris)
      	   {
      	   	System.out.println("Thumb Scan Failed");
      	   }
      	   else	
      	   {
      	    System.out.println("Thumb and Iris Scan Failed");
      	   }
  	  
  	  
 	  }
  }
}
