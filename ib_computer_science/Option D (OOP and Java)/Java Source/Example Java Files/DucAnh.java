public class DucAnh{
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String word = sc.nextLine();
    String[] word_a = word.split("");
    System.out.println("Number of letters in your word" + (int) word_a.length);
    int last = (int) word_a.length; 
    System.out.println("There are " + last+ " letters");
    System.out.println(" Last letter: " + word_a[last-1]);
    System.out.println(" First letter: " + word_a[0]);
    int wa=word_a.length;
    double mid = wa;
    //double mid =( int )word_a.length/2;
    System.out.println(" Mid letter: " + word_a[mid]);
    }
}



