package oopJava;

/**
 * @author Sean
 */

class Car {
	
	Car() {
		
	}
	
}

public class Exercise2 {

   /**
    * IMPORTANT: Make sure you read through the worksheet (at least up to the start
    * of the Exercises, as this contains some information about what you need to do,
    * and the correct syntax
    */

   /**
    * QUESTION 1
    *
    * Below this comment, you will need to create your own method! Check the worksheet
    * for more information, but here is some of the info:
    *    - The method has to be public and static
    *    - The return type should be boolean
    *    - It should be called question1
    *    - Return true
    */
	public static boolean question1() {
		return true;
	}
   

   /**
    * QUESTION 2
    *
    * Replace 'return null;' with your own code!
    *
    * This question asks you to:
    *    - Create a new int array with space for 10 items, and
    *    - Place the value '6' in the fourth space (remember this is index 3!)
    *    - Return the array.
    */
   public static int[] question2() {

      return null;
   }

   /**
    * QUESTION 3
    *
    * Replace 'return null;' with your code
    *
    * This question asks you to:
    *    - Create a new 2D int array with space for 4x4 items
    *    - Place the value 15 at position 3,0
    *    - Place the value -3 at position 1,2
    */
   public static int[][] question3() {

      return null;
   }

   /**
    * QUESTION 4:
    *
    * Replace 'return null;' with your code. In the worksheet you can
    * find the explanation for why this question return type is Object.
    *
    * This question asks you to:
    *    - Create a new class called Car
    *    - Write a constructor in the Car class, but don't put
    *      any code between the brackets
    *    - In this method:
    *       - Create a new Car object
    *       - Return the Car object
    *
    */
   public static Object question4() {
	   Car car = new Car();
	   return car;
   }

   /**
    * QUESTION 5:
    *
    * Replace 'return null;' with your code
    *
    * In the Car class:
    *    - Create a new constructor method, but this time include
    *      a 'String colour' parameter
    *       - This lets us pass information to the object
    *
    * In this method:
    *    - Create a new Car object, passing in a String containing a colour
    *    - Return the Car object
    */
   public static Object question5() {

      return null;
   }

   /**
    * QUESTION 6:
    *
    * Replace 'return null;' with your code
    *
    * In the Car class:
    *    - Create a new String field called 'colour'
    *    - Assign the new colour field to the parameter from the Car constructor
    *       - You can do this by writing 'this.colour = colour;'
    *    - Create a new method called getColour()
    *       - It should return the String held in the colour field
    *
    * In this method:
    *    - Create a new Car object, passing in the String "red"
    *    - Return the value you get by calling 'getColour()' on your new Car object
    */
   public static String question6() {

      return null;
   }

   /**
    * QUESTION 7:
    *
    * Replace 'return null;' with your code
    *
    * In the Car class:
    *    - Create a method called setColour that takes a String parameter (you can call it what you like)
    *    - Inside the method, assign the value of the String parameter to the field called colour
    *
    * In this method:
    *    - Create a car object, passing it the String "red" (you could copy this line from the previous method)
    *    - Call your newly created setColour method on the car object, passing in "black"
    *    - Return the value of calling getColour() on the car object
    */
   public static String question7() {

      return null;
   }

   /**
    * QUESTION 8:
    *
    * Replace 'return null;' with your code
    * 
    * This question is a bit more involved, so you will want to
    * make sure you check the worksheet for information.
   *
    * In the Car class:
    *    - Create a new enum called something like ColourType
    *       - There is info on the syntax in the worksheet
    *       - You can add any colours you want, but make sure to include 'RED'
    *    - In the constructor method that takes a String argument, change the
    *      String argument to your enum
    *       - You'll need to change your field to be of the same type as
    *         the enum
    *    - You'll also need to change the parameter in the setColour method
    *    - And also the return type of getColour
    *
    * In this method:
    *    - Create a new Car object, passing in the 'RED' value from your enum
    *    - Create a new variable, and assign it to the return value of calling
    *      'getColour' on the object
    *    - Return the value of calling 'toString(); on that variable
    *       - There is more info on this in the worksheet
    * 
    */
   public static String question8() {
      return null;
   }

   /**
    * When you run the program, this class is executed, and runs the tests
    */
   public static void main(String[] args) {
      TestRunner.run();
   }
}


