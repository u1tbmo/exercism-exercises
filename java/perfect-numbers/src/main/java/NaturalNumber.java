class NaturalNumber {
    Classification classification;

    NaturalNumber(int number) {
        if (number <= 0) {
            throw new IllegalArgumentException(
                    "You must supply a natural number (positive integer)");
        }

        int sum = 0;
        for (int i = 1; i < number; i++) {
            if (number % i == 0) {
                sum += i;
            }
        }

        if (sum == number) {
            this.classification = Classification.PERFECT;
        } else if (sum < number) {
            this.classification = Classification.DEFICIENT;
        } else {
            this.classification = Classification.ABUNDANT;
        }
    }

    Classification getClassification() {
        return this.classification;
    }
}
