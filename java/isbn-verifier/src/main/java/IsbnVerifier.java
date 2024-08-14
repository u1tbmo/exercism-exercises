import java.util.stream.IntStream;
import java.util.List;

class IsbnVerifier {

    final int ISBN_LENGTH = 10;

    boolean isValid(String stringToVerify) {
        // Check the length of the string
        if (stringToVerify.length() != 10 && stringToVerify.length() != 13) {
            return false;
        }

        // Create a List of Characters filtering invalid characters
        List<Character> filteredString =
                IntStream.range(0, stringToVerify.length()).mapToObj(i -> stringToVerify.charAt(i))
                        .filter(c -> (Character.isDigit(c) | c == 'X')).toList();

        // Recheck the length of the string
        if (filteredString.size() != 10) {
            return false;
        }

        // Iterate over the enumerated filteredString list
        int sum = 0;
        int index = 0;
        while (index < ISBN_LENGTH) {
            Character currentChar = filteredString.get(index);
            if (Character.isDigit(currentChar)) {
                sum += Character.getNumericValue(currentChar) * (ISBN_LENGTH - index);
            } else if (index != ISBN_LENGTH - 1 && currentChar == 'X') {
                return false;
            } else {
                sum += 10;
            }


            index++;
        }

        return sum % 11 == 0;
    }

}

