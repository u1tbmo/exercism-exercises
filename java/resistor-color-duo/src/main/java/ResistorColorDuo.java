import java.util.Arrays;

class ResistorColorDuo {
    private final int COLOR_QUANTITY = 2;

    int value(String[] colors) {
        int sum = 0;
        int exponent = 0;
        for (int i = COLOR_QUANTITY - 1; i >= 0; i--) {
            sum += colorCode(colors[i]) * Math.pow(10, exponent);
            exponent++;
        }
        return sum;
    }

    int colorCode(String color) {
        return Arrays.asList(colors()).indexOf(color);
    }

    String[] colors() {
        return new String[] {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet",
                "grey", "white"};
    }
}
