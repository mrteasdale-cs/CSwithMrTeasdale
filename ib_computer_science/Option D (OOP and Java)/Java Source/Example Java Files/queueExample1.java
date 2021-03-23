import java.util.LinkedList;
import java.util.Queue;

public class queueExample1{
public static void main (String[]args) {
	//Create queue and linked list
	Queue<String> Q = new LinkedList<>();
	//adding items in queue
	Q.add("Martin");
	Q.add("Diane");
	Q.add("James");
	Q.add("Peter");
	System.out.println("Names in queue: "+ Q);
	while(!(Q.isEmpty())) {
		System.out.println(Q.remove());
		System.out.println("The items in the queue are:  " + Q);
	}
	
	
}
}