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
  	
  	 String usr = JOptionPane.showInputDialog(null,"Myran",
  								"Input", JOptionPane.QUESTION_MESSAGE);
  	
  	  int mark = Integer.parseInt(usr);
  	  
  	  System.out.print("You got a ");
  	  
  	    if(mark > 70)
     
          System.out.println("1st degree");   
      
    	else if (mark >= 60)
    	 
    	  System.out.println("2.2 degree");   		  
    
   		else if(mark >=50)
   		 
  		  System.out.println("2.1 degree"); 
        
        else if(mark >=40)
   		 
  		  System.out.println("3rd degree"); 
        
        else if(mark <40)
   		  
  		  System.out.println("Fail......Your Crap"); 
        
      System.out.println("Program closing.");
      
      
  		
  }
}
