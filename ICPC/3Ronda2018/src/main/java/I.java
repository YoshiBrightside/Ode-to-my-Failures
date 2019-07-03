import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class I {
    public static void main(String[] args) {
        // Input
        Scanner input = new Scanner(System.in);

        // N
        String[] nm = input.nextLine().split("\\s+");
        int n = Integer.parseInt(nm[0]);

        // M
        int m = Integer.parseInt(nm[1]);
        boolean[] lamps = new boolean[m];

        // initial lamps
        String[] initLamps = input.nextLine().split("\\s+");
        int on = Integer.parseInt(initLamps[0]);
        if (on == 0) {
            System.out.println(0);
            return;
        }
        for (int i = 1; i <= on; i++) {
            lamps[Integer.parseInt(initLamps[i]) - 1] = true;
        }

        // switches
        boolean[][] switches = new boolean[n][m];
        for (boolean[] s : switches) {
            String[] nums = input.nextLine().split("\\s+");
            int affects = Integer.parseInt(nums[0]);
            for (int i = 1; i <= affects; i++) {
                s[Integer.parseInt(nums[i]) - 1] = true;
            }
        }

        // save states in hash map
        ArrayList<boolean[]> states = new ArrayList<>();
        int count = 0;
        while (true) {
            for (boolean[] s : switches) {
                count++;
                lamps = xorString(lamps, s);
                boolean[] lampss = lamps;
                if (isZero(lampss)) {
                    System.out.println(count);
                    return;
                }
            }
            // at the end of each cycle check if key exists if it does return -1
            states.add(lamps);
            if (inState(lamps, states)) {
                System.out.println(-1);
                return;
            }
        }


    }

    private static boolean inState(boolean[] lamps, ArrayList<boolean[]> states) {
        int ll = lamps.length;
        for (boolean[]state: states) {
            for (int i = 0; i < ll ; i++) {
                if(state[i] != lamps[i])
                    break;
                return true;
            }
        }
        return false;
    }


    private static boolean isZero(boolean[] lamps) {
        for (boolean b : lamps)
            if (b)
                return false;
        return true;
    }

    static boolean[] xorString(boolean[] a, boolean[] b) {
        int la = a.length;
        boolean[] result = new boolean[la];
        for (int i = 0; i < la; i++) {
            result[i] = (!a[i] && b[i]) || (!b[i] && a[i]);
        }
        return result;
    }
}
