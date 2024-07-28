class RnaTranscription {

    String transcribe(String dnaStrand) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < dnaStrand.length(); i++) {
            switch (dnaStrand.charAt(i)) {
                case 'G':
                    result.append("C");
                    break;
                case 'C':
                    result.append("G");
                    break;
                case 'T':
                    result.append("A");
                    break;
                case 'A':
                    result.append("U");
                    break;
            }
        }
        return result.toString();
    }

}
