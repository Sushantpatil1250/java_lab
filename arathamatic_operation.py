import java.util.Scanner;

public class arthamatic_ope
{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("enter value a: ");
        int a = s.nextInt();
        System.out.println("enter value b: ");
        int b = s.nextInt();
        int Add = a +b;
        int Mul = a *b;
        int Sub = a -b;
        int Div = a /b;
        int Mod = a %b;
        System.out.println("addition; "+Add);
        System.out.println("multiplication; "+Mul);
        System.out.println("subscription: "+Sub);
        System.out.println("division: "+Div);
        System.out.println("modulus: "+Mod);
    }
}
