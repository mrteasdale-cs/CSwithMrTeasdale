package basicjava;

import java.util.Scanner;


public class basicJavaMethod {
    int num = 6;
    int guesses = 0;
    Scanner sc = new Scanner(System.in);
    
    
    String result(){
    
    String output="";
    String won="";
    System.out.println("I'm thinking of a number between 1 and 10.\nSee if you can guess the number!");
    int guess = sc.nextInt();
    
    while(true){
        
        if (num==guess){
            won="Well done! it was "+num;
            break;
        }
        System.out.println("Incorrect, try again...");
        guess = sc.nextInt();
        guesses++;
    }
    output = "You took "+guesses+" number of guesses";
    return won+output;
        
    }
    
    
}
