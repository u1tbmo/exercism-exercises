import java.util.stream.Collectors;
import java.util.HashMap;

class IsogramChecker {

    boolean isIsogram(String phrase) {
        // Initialize a HashMap of letter occurences
        HashMap<Character, Integer> occurences = new HashMap<>();
        for (char ch = 'A'; ch <= 'Z'; ch++) {
            occurences.put(ch, 0);
        }

        // Update the HashMap for every character in the phrase
        phrase.chars().mapToObj(e -> (char) e).filter(e -> Character.isAlphabetic(e))
                .collect(Collectors.toList()).stream().forEach(e -> {
                    char uppercaseChar = Character.toUpperCase(e);
                    occurences.put(uppercaseChar, occurences.get(uppercaseChar) + 1);
                });

        return occurences.values().stream().noneMatch(count -> count > 1);
    }

}
