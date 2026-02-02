import java.util.Scanner;

public class fact
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a number:");
        int fact = 1;
        int a = sc.nextInt();
        for (int i = 1 ; i<=a ; i++ )
        {
            fact =fact *i;
        }

        System.out.println("factorial of a" + fact);
    }
}
