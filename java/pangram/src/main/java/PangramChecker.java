import java.util.HashSet;
import java.util.Set;

public class PangramChecker {
    public boolean isPangram(String input) {
        Set<Character> chars = new HashSet<Character>();
        for (char letter : input.toLowerCase().toCharArray()) {
            if (Character.isLetter(letter)) {
                chars.add(letter);
            }
        }
        return chars.size() == 26;
    }
}
