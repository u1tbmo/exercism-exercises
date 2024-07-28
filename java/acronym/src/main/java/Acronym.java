class Acronym {
    String value;

    Acronym(String phrase) {
        String cleanPhrase = phrase.replaceAll("['_]", "");
        cleanPhrase = cleanPhrase.replaceAll("[-]", " ");
        cleanPhrase = cleanPhrase.trim();
        cleanPhrase = cleanPhrase.replaceAll(" +", " ");
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < cleanPhrase.length(); i++) {
            if (i == 0) {
                result.append(Character.toUpperCase(cleanPhrase.charAt(i)));
            } else {
                switch (cleanPhrase.charAt(i - 1)) {
                    case ' ':
                    case '-':
                        result.append(Character.toUpperCase(cleanPhrase.charAt(i)));
                        break;
                    default:
                        break;
                }
            }
        }
        this.value = result.toString();
    }

    String get() {
        return this.value;
    }

}
