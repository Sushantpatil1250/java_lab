import java.util.Scanner;

public class swap
{
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        int temp;
        System.out.println("enater a numbre a :");
        int a  = sc.nextInt();
        System.out.println("enater a numbre b :");
        int b = sc.nextInt();
        System.out.println("before swap a :" + a);
        System.out.println("before swap b :" + b);
        temp = a;
        a = b;
        b = temp;
        System.out.println("after swap a :" + a);
        System.out.println("after swap b :" + b);


    }
}
