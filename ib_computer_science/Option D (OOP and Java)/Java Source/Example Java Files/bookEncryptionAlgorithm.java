import java.util.Scanner;
public class bookEncryptionAlgorithm {
public static void main (String[]args) {
int dig_1;
int dig_2;
int dig_3;
int dig_4;
int a;
int temp;
int encrypted;
System.out.println("Please enter a four digit number to be encrypted: ");
Scanner kb = new Scanner(System.in);
a=kb.nextInt();
dig_1=a%10000/1000;
dig_2=a%1000/100;
dig_3=a%100/10;
dig_4=a%10/1;
dig_1=(dig_1+5)%10;
dig_2=(dig_2+5)%10;
dig_3=(dig_3+5)%10;
dig_4=(dig_4+5)%10;
temp=dig_1;
dig_1=dig_4;
dig_4=temp;
temp=dig_2;
dig_2=dig_3;
dig_3=temp;
encrypted=dig_1*1000+dig_2*100+dig_3*10+dig_4;
System.out.println("encrypted number is: ");
System.out.println(encrypted);



}
}
