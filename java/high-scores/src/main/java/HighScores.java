import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class HighScores {
    private List<Integer> highScores;

    public HighScores(List<Integer> highScores) {
        this.highScores = highScores;
    }

    List<Integer> scores() {
        return this.highScores;
    }

    Integer latest() {
        return this.highScores.getLast();
    }

    Integer personalBest() {
        return Collections.max(this.highScores);
    }

    List<Integer> personalTopThree() {
        List<Integer> result = new ArrayList<>();
        List<Integer> sortedHighScores = new ArrayList<>(this.highScores);
        sortedHighScores.sort(Comparator.reverseOrder());
        int length = Math.min(sortedHighScores.size(), 3);
        for (int i = 0; i < length; i++) {
            result.add(sortedHighScores.get(i));
        }
        return result;
    }

}
