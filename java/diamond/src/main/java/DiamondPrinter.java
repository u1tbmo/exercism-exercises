import java.util.ArrayList;
import java.util.List;

class DiamondPrinter {
    final String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    List<String> printToList(char a) {

        // Initialize a result ArrayList
        List<String> result = new ArrayList<>();

        // Special Case: 'A'
        if (a == 'A') {
            result.add("A");
            return result;
        }

        // Initialize the number of spaces outside and inside the diamond
        int qtyOutsideSpaces = 0;
        int qtyInsideSpaces = (alphabet.indexOf(a) - 1) * 2 + 1;

        // Construct the center row of the diamond
        result.add(a + repeatSpaces(qtyInsideSpaces) + a);

        for (int i = alphabet.indexOf(a); i > 0; i--) {
            // Update spaces
            qtyOutsideSpaces += 1;
            qtyInsideSpaces -= 2;
            String outsideSpaces = repeatSpaces(qtyOutsideSpaces);
            String insideSpaces = repeatSpaces(qtyInsideSpaces);

            // Get the previous letter to a in the alphabet
            char letter = alphabet.charAt(i - 1);

            // Constructing the rows until we reach the start and end points of the diamond
            String rowResult = new String();
            if (letter != 'A') {
                rowResult += outsideSpaces + letter + insideSpaces + letter + outsideSpaces;
                result.add(0, rowResult);
                result.add(rowResult);
            } else {
                rowResult = outsideSpaces + letter + outsideSpaces;
                result.add(0, rowResult);
                result.add(rowResult);
            }
        }


        return result;
    }

    private String repeatSpaces(int repetitions) {
        String result = new String();
        for (int i = 0; i < repetitions; i++) {
            result += " ";
        }
        return result;
    }

}
