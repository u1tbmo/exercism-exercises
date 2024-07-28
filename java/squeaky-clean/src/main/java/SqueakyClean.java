class SqueakyClean {

    static String clean(String identifier) {
        StringBuilder result = new StringBuilder();
        int length = identifier.length();

        for (int i = 0; i < length; i++) {
            char currentChar = identifier.charAt(i);
            if (currentChar == '-') {
                if (i + 1 < length) {
                    result.append(Character.toUpperCase(identifier.charAt(i + 1)));
                }
                i++;
            } else {
                Character charToAppend = convertChar(currentChar);
                if (charToAppend != null) {
                    result.append(charToAppend);
                }
            }
        }
        return result.toString();
    }

    private static Character convertChar(char character) {
        switch (character) {
            case ' ':
                return '_';
            case '4':
                return 'a';
            case '3':
                return 'e';
            case '0':
                return 'o';
            case '1':
                return 'l';
            case '7':
                return 't';
            default:
                if (Character.isLetter(character)) {
                    return character;
                }
                break;
        }
        return null;
    }
}
