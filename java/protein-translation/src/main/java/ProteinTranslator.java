import java.util.ArrayList;
import java.util.Map;

class ProteinTranslator {
    Map<String, String> codonToProteinMap = Map.ofEntries(Map.entry("AUG", "Methionine"),
            Map.entry("UUU", "Phenylalanine"), Map.entry("UUC", "Phenylalanine"),
            Map.entry("UUA", "Leucine"), Map.entry("UUG", "Leucine"), Map.entry("UCU", "Serine"),
            Map.entry("UCC", "Serine"), Map.entry("UCA", "Serine"), Map.entry("UCG", "Serine"),
            Map.entry("UAU", "Tyrosine"), Map.entry("UAC", "Tyrosine"),
            Map.entry("UGU", "Cysteine"), Map.entry("UGC", "Cysteine"),
            Map.entry("UGG", "Tryptophan"), Map.entry("UAA", "STOP"), Map.entry("UAG", "STOP"),
            Map.entry("UGA", "STOP"));

    ArrayList<String> translate(String rnaSequence) {
        ArrayList<String> proteins = new ArrayList<String>();
        for (int i = 0; i < rnaSequence.length(); i += 3) {
            if (i + 3 > rnaSequence.length()) {
                throw new IllegalArgumentException("Invalid codon");
            }

            String codon = rnaSequence.substring(i, i + 3);
            String protein = codonToProteinMap.get(codon);

            if (protein == null) {
                throw new IllegalArgumentException("Invalid codon");
            } else if (protein.equals("STOP")) {
                break;
            }

            proteins.add(protein);

        }
        return proteins;
    }
}
