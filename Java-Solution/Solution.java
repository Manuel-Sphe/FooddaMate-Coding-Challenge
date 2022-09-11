import java.util.Scanner;
class Solution{
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        System.out.println("Enter A linear eqation to solve");
        String equation = kb.nextLine();

        String [] arr = equation.split("=");

        String left = arr[0], right = arr[1];
        
        Equation obj = new Equation(left, right);
        obj.Eliminate();
    }
}