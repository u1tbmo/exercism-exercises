import java.util.Arrays;

class ResistorColorTrio {
    String label(String[] colors) {
        long colorValue = (long) (value(colors) * Math.pow(10, colorCode(colors[2])));
        int length = String.valueOf(colorValue).length();
        if (length >= 4 && length <= 6) {
            return String.valueOf(colorValue / 1000) + " kiloohms";
        } else if (length >= 7 && length <= 9) {
            return String.valueOf(colorValue / 1_000_000) + " megaohms";
        } else if (length >= 10 && length <= 12) {
            return String.valueOf(colorValue / 1_000_000_000) + " gigaohms";
        }
        return String.valueOf(colorValue) + " ohms";
    }

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
