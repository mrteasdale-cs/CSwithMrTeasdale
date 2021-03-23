/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **
 **  Student ID : 010125                     **
 **  Date       : 20/10/08                   **
 **  Description:                            **
 **********************************************/ 


import javax.swing.*;


class Week4Prog1Ses1

{
  public static void main(String[] args)
  {
  	
  	String usr = JOptionPane.showInputDialog(null,"Myran",
  								"Input", JOptionPane.QUESTION_MESSAGE);
  	
  	
    int mark = Integer.parseInt(usr);
    if(mark >= 40)
    
    { 
      System.out .println("Mark is greater than 40"); 
      System.out.println("Wey You Passed Lyk!!!"); 
    }

    else if (mark >= 10)
    	{ 
    	  System.out .println("Mark less than 40"); 
   		  System.out.println("failed"); 
   		}
    
   		else if(mark < 10)
   		 
  		{ 
  		  System.out .println("Mark less than 40"); 
   		  System.out.println("failed"); 
  		  System.out .println("You Got Less Than 10 you loser"); 
          System.out.println(":)"); 
        }
    
    System.out.println("Program closing.");

  }
}
