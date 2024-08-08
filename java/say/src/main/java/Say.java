public class Say {

    static final String[] ZEROTONINETEEN = {"zero", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen"};

    static final String[] TENS =
            {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    static final String[] DENOMINATIONS = {"hundred", "thousand", "million", "billion"};

    public String say(long number) {

        StringBuilder result = new StringBuilder();

        if (number >= 1_000_000_000_000L || number < 0) {
            throw new IllegalArgumentException(String.valueOf(number));
        }

        // Case 0 to 19
        if (number >= 0 && number < 20) {
            return ZEROTONINETEEN[(int) number];
        }

        // Case 20 to 99
        if (number >= 20 && number < 100) {
            long remainder = number % 10;
            number /= 10;
            result.append(TENS[(int) number]);
            if (remainder != 0) {
                result.append("-").append(say(remainder));
            }
        }

        // Case 100 to 999
        if (number >= 100 && number < 1_000) {
            long remainder = number % 100;
            number /= 100;
            result.append(ZEROTONINETEEN[(int) number]).append(" ").append(DENOMINATIONS[0]);
            if (remainder != 0) {
                result.append(" ").append(say(remainder));
            }
        }

        // Case 1,000 to 999,999
        if (number >= 1_000 && number < 1_000_000) {
            long remainder = number % 1_000;
            number /= 1000;
            result.append(say(number)).append(" ").append(DENOMINATIONS[1]);
            if (remainder != 0) {
                result.append(" ").append(say(remainder));
            }
        }

        // Case 1_000_000 to 999_999_999
        if (number >= 1_000_000 && number < 1_000_000_000) {
            long remainder = number % 1_000_000;
            number /= 1_000_000;
            result.append(say(number)).append(" ").append(DENOMINATIONS[2]);
            if (remainder != 0) {
                result.append(" ").append(say(remainder));
            }
        }

        // Case 1_000_000_000 to 999_999_999_999
        if (number >= 1_000_000_000 && number < 1_000_000_000_000L) {
            long remainder = number % 1_000_000_000;
            number /= 1_000_000_000;
            result.append(say(number)).append(" ").append(DENOMINATIONS[3]);
            if (remainder != 0) {
                result.append(" ").append(say(remainder));
            }
        }

        return result.toString();
    }
}
