import java.util.*;

public class D {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int wins = 0;
        int car;
        for (int i = 0; i < n; i++) {
            car = input.nextInt();
            switch (car) {
                case 0:
                    wins++;
                    break;
                case 1:
                    break;
                default:
                    wins++;
                    break;
            }

        }
        System.out.println(wins);
    }
}
