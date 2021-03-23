import java.util.Stack;

public class STACKS {

	public static void main(String[] args) {
		//initialise variables/objects
	    int[] LINE = {3,6,8,4,77};
	    Stack S = new Stack();
	    Stack Reverse = new Stack();
	    int counter = 0;
    	System.out.println("Stack BEFORE pushing to stack S: "+S);//some testing

    	//push array to stack
	    for(counter=0;counter<LINE.length;counter++) {
	    	S.push(LINE[counter]);
	    }
    	System.out.println("Stack AFTER pushing to stack S: "+S);//see what the stack contains after the loop

    	//pop values to reverse stack
	    while(!(S.empty())) {
	    	Reverse.push(S.pop());	
	    	System.out.println(S);
	    }
    	System.out.println("Reverse stack: "+Reverse);
	    
	    /*
	    while(!(S.empty())) {
	    	System.out.println(S.pop());
	    }*/
	}

}
