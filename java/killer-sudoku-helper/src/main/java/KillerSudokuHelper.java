import java.util.ArrayList;
import java.util.List;

public class KillerSudokuHelper {
    private static List<Integer> sudokuNumbers = new ArrayList<>();
    static {
        for (int i = 1; i <= 9; i++) {
            sudokuNumbers.add(i);
        }
    }

    List<List<Integer>> combinationsInCage(Integer cageSum, Integer cageSize,
            List<Integer> exclude) {

        List<List<Integer>> result = new ArrayList<>();
        List<List<Integer>> combinations = generateCombinations(cageSize, 1, 9);

        for (List<Integer> combination : combinations) {
            if (combination.stream().noneMatch(exclude::contains)
                    && combination.stream().mapToInt(Integer::intValue).sum() == cageSum) {
                result.add(combination);
            }
        }

        return result;
    }

    List<List<Integer>> combinationsInCage(Integer cageSum, Integer cageSize) {

        List<List<Integer>> result = new ArrayList<>();
        List<List<Integer>> combinations = generateCombinations(cageSize, 1, 9);

        for (List<Integer> combination : combinations) {
            if (combination.stream().mapToInt(Integer::intValue).sum() == cageSum) {
                result.add(combination);
            }
        }

        return result;
    }

    List<List<Integer>> generateCombinations(int n, int start, int end) {

        List<List<Integer>> result = new ArrayList<>();

        // Base Case: No more digits to choose
        if (n == 0) {
            result.add(new ArrayList<>());
            return result;
        }

        // Recursive Case: Generate combinations for each digit from start to end, generating all
        // possible combinations of the next n-1 digits
        for (int i = start; i <= end; i++) {
            List<List<Integer>> subCombinations = generateCombinations(n - 1, i + 1, end);
            for (List<Integer> subCombination : subCombinations) {
                subCombination.add(0, i);
                result.add(subCombination);
            }
        }

        return result;
    }

}
