import java.util.ArrayList;

public class EliudsEggs {
    public int eggCount(int number) {
        // Convert number to binary
        ArrayList<Character> binaryList = new ArrayList<>();
        while (number != 0) {
            int remainder = number % 2;
            number /= 2;
            binaryList.add(Character.forDigit(remainder, 10));
        }

        // Count the actual number of eggs
        int eggs = (int) binaryList.stream().filter(e -> e.equals('1')).count();

        return eggs;
    }
}
