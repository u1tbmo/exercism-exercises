public class Lasagna {
    private static final int EXPECTED_MINUTES_IN_OVEN = 40;
    private static final int PREPARATION_TIME_PER_LAYER = 2;

    // Returns the expected cooking time of the Lasagna
    public int expectedMinutesInOven() {
        return EXPECTED_MINUTES_IN_OVEN;
    }

    // Returns the time in minutes left until the Lasagna is done cooking
    public int remainingMinutesInOven(int minutesElapsedInOven) {
        return expectedMinutesInOven() - minutesElapsedInOven;
    }

    // Returns the preparation time per layer of Lasagna
    public int preparationTimeInMinutes(int layersInLasagna) {
        return PREPARATION_TIME_PER_LAYER * layersInLasagna;
    }

    // Returns the total time elapsed while working on the Lasagna
    // (preparing + cooking)
    public int totalTimeInMinutes(int layersInLasagna, int minutesElapsedInOven) {
        return preparationTimeInMinutes(layersInLasagna) + minutesElapsedInOven;
    }
}
