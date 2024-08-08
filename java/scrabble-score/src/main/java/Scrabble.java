import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

class Scrabble {
    int score;

    Map<String, Integer> letterScores = Map.ofEntries(Map.entry("A", 1), Map.entry("E", 1),
            Map.entry("I", 1), Map.entry("O", 1), Map.entry("U", 1), Map.entry("L", 1),
            Map.entry("N", 1), Map.entry("R", 1), Map.entry("S", 1), Map.entry("T", 1),
            Map.entry("D", 2), Map.entry("G", 2), Map.entry("B", 3), Map.entry("C", 3),
            Map.entry("M", 3), Map.entry("P", 3), Map.entry("F", 4), Map.entry("H", 4),
            Map.entry("V", 4), Map.entry("W", 4), Map.entry("Y", 4), Map.entry("K", 5),
            Map.entry("J", 8), Map.entry("X", 8), Map.entry("Q", 10), Map.entry("Z", 10));

    Scrabble(String word) {
        if (word.isEmpty()) {
            this.score = 0;
            return;
        }
        ArrayList<String> wordAsArray = new ArrayList<String>(Arrays.asList(word.split("")));
        this.score = wordAsArray.stream().mapToInt(c -> letterScores.get(c.toUpperCase())).sum();
    }

    int getScore() {
        return this.score;
    }

}
