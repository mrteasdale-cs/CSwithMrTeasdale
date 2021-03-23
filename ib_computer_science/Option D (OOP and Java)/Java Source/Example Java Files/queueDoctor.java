import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class queueDoctor {
    public static void main(String[] args) {
        // Create and initialize a Queue using a LinkedList
        Queue<String> Q = new LinkedList<>();
        Scanner input = new Scanner(System.in);
        
       while(Q.size()<5) {
    	  System.out.println("Add Name");
    	  String  Name = input.nextLine();	
    	  Q.add(Name);
       }
       System.out.println("Names currently in the queue are: " + Q);
       
       while(!(Q.isEmpty())) {
    	   System.out.println("The next person to visit the doctor is: "+ Q.remove());
    	   System.out.println("Add Name");
     	  String  Name = input.nextLine();	     	  
     	  Q.add(Name);
     	 System.out.println("Names currently in the queue are: " + Q);
       }
        
        


}
}