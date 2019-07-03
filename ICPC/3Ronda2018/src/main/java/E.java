import java.util.Scanner;

public class E {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int count = 0;
        String crib = input.nextLine();
        int cLen = crib.length();
        String word = input.nextLine();
        int wLen = word.length();

        for (int i = 0; i + wLen <= cLen; i++) {
            boolean fit = true;
            for (int j = 0; j < wLen ; j++) {
                if(crib.charAt(i+j)== word.charAt(j)){
                    fit = false;
                    break;
                }

            }
            count += fit ? 1 : 0;
        }

        System.out.println(count);
    }
}
