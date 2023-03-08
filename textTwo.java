import java.util.Scanner;
public class Program
{
    public static void main(String[] args) {
	   Scanner read = new Scanner(System.in);
           int password = 8819;
          do{
            System.out.println("Write password");
          }
          while(read.nextInt() != password);
	}
}