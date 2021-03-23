import java.util.Stack;
public class stackExample{
	public static void main (String[]args) {
		Stack <String> stackOfCards = new Stack<>();
		//Push items to the stack
		stackOfCards.push("Jack");
		stackOfCards.push("Queen");
		stackOfCards.push("King");
		stackOfCards.push("Ace");
		System.out.println("Stack => " + stackOfCards);
		System.out.println();
//popping items from the stack
		String cardAtTop = stackOfCards.pop();
		System.out.println("Stack.pop() = >" + cardAtTop);
		System.out.println("Current Stack =>" + stackOfCards);
		System.out.println();
		
		//get the item at the top of the stack
		cardAtTop = stackOfCards.peek();
		System.out.println("Stack.peek() =>" + cardAtTop);
		System.out.println("Current Stack =>" + stackOfCards);
		//int index = stackOfCards.search("King");
		//System.out.println(index);
		
		
		
	}
}