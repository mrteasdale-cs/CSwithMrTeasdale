import java.util.*;
public class printStack {
	public static void main (String[]args) {
		Stack S = new Stack();
		S.push(3);
		S.push(5);
		S.push(7);
		while(!(S.empty())){
			System.out.println(S.pop());
		}
	}

}
