import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int numMarbels = Integer.parseInt(input.nextLine());
        int x = 0;
        int y = 1;
        int score = 0;
        int[][] marbels = new int[numMarbels][2];
        for (int i = 1; i <= numMarbels ; i++) {
            String[] marbel = input.nextLine().split("\\s+");
            marbels[i-1] = new int[]{Integer.parseInt(marbel[0]), Integer.parseInt(marbel[1])};
        }
        for (int[] marbel: marbels) {
            int mx = marbel[x];
            int my = marbel[y];
            if(mx == 0 || my == 0 || (marbel[x] == marbel[y])){
                System.out.println("Y");
                return;
            }
            if(!((marbel[x] == 1 && marbel[y] == 2) || (marbel[y] == 1 && marbel[x] == 2))){
                if((mx == 1 && my > 2) || (my ==1 && mx > 2)){
                    score++;
                } else {
                  if(mx > 2){
                      score += 2;
                  }
                  if(my > 2){
                      score += 2;
                  }
                }
            }
        }
        if(score % 2 == 1){
            score++;
        }
        if(score / 2 % 2 == 1){
            System.out.println("N");
        } else {
            System.out.println("Y");
        }
    }
}
