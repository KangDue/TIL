package tutorials.numberstring;

import java.io.File;
import java.util.Scanner;
public class number {
    public static void main(String[] args) {
        try {
            File file = new File("input.txt");
            Scanner sc = new Scanner(file);
            while (sc.hasNextInt()) {
                System.out.println(sc.nextInt());
            }
            sc.close();
        } catch (Exception e) {
            System.out.println(1111111);
        }
    }
}
