package oopJava;

/**
 * @author Sean
 */
public class TestRunner {

   public static void run() {

      System.out.println("Auto-marking Exercise 2");
      System.out.println();

      System.out.println("Report:");
      markQ1();
      markQ2();
      markQ3();
      markQ4();
      markQ5();
      markQ6();
      markQ7();
      markQ8();
   }

   private static void markQ1() {
      boolean answer = Exercise2.question1();

      if (answer)
         printQuestionCorrect(1);
      else
         printQuestionIncorrect(1, "Question didn't return true");
   }

   private static void markQ2() {
      int[] nums = Exercise2.question2();
      if (nums == null)
         printQuestionNull(2);
      else if (nums[3] != 6)
         printQuestionIncorrect(2, "Value 6 was not in the fourth space");
      else
         printQuestionCorrect(2);
   }

   private static void markQ3() {
      int[][] nums = Exercise2.question3();

      String errorString = "";
      if (nums == null) {
         printQuestionNull(3);
         return;
      } else if (nums.length != 4 || nums[0].length != 4)
         errorString += "2D array not created with correct length";
      else if (nums[3][0] != 15 || nums[1][2] != -3)
         errorString += "Correct values not found in the array";

      if (!errorString.equals(""))
         printQuestionIncorrect(3, errorString);
      else
         printQuestionCorrect(3);

   }

   private static void markQ4() {
      Object car = Exercise2.question4();

      if (car == null) {
         printQuestionNull(4);
      } else if (car instanceof Car) {
         printQuestionCorrect(4);
      } else {
         printQuestionIncorrect(4, "The method didn't return a Car object");
      }
   }

   private static void markQ5() {
      Object car = Exercise2.question5();

      if (car == null) {
         printQuestionNull(5);
      } else if (car instanceof Car) {
         printQuestionCorrect(5);
      } else {
         printQuestionIncorrect(5, "The method didn't return a Car object");
      }
   }

   private static void markQ6() {
      String correctAnswer = "red";
      String colour = Exercise2.question6();

      if (colour == null) {
         printQuestionNull(6);
      } else if (colour.equals(correctAnswer))
         printQuestionCorrect(6);
      else
         printQuestionIncorrect(6, "\"red\" wasn't returned by getColour()");
   }

   private static void markQ7() {
      String correctAnswer = "black";
      String colour = Exercise2.question7();

      if (colour == null) {
         printQuestionNull(7);
      } else if (colour.equals(correctAnswer)) {
         printQuestionCorrect(7);
      } else {
         printQuestionIncorrect(7, "\"black\" wasn't returned by getColour()");
      }
   }

   private static void markQ8() {
      String correctAnswer = "RED";
      String colour = Exercise2.question8();

      if (colour == null) {
         printQuestionNull(8);
      } else if (colour.equals(correctAnswer)) {
         printQuestionCorrect(8);
      } else {
         printQuestionIncorrect(8, "\"RED\" wasn't returned.");
     }
   }

   private static void printQuestionCorrect(int questionNumber) {
        System.out.println("| Question " + questionNumber + ": correct");
   }

   private static void printQuestionIncorrect(int questionNumber, String reason) {
      System.out.println("| Question " + questionNumber + ": incorrect - " + reason);
   }

   private static void printQuestionNull(int questionNumber) {
      printQuestionIncorrect(questionNumber, "Question returns null");
   }

   /**
    * This is a dummy class so that the code compiles and you can run
    * the test. Question 4 asks you to remove this private class (delete
    * the code)
    */
   private class Car {
      
   }

}
