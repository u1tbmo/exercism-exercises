import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class HandshakeCalculator {

    List<Signal> calculateHandshake(int number) {
        List<Integer> binaryList = new ArrayList<>();
        while (number != 0) {
            int remainder = number % 2;
            number /= 2;
            binaryList.add(0, remainder);
        }

        // Pad the binaryList with zeroes (up to five bits)
        for (int i = binaryList.size(); i < 5; i++) {
            binaryList.add(0, 0);
        }

        // If the size of five is exceeded, remove extras
        while (binaryList.size() != 5) {
            binaryList.remove(0);
        }

        List<Signal> signalList = new ArrayList<>();
        if (binaryList.get(4) == 1) {
            signalList.add(Signal.WINK);
        }
        if (binaryList.get(3) == 1) {
            signalList.add(Signal.DOUBLE_BLINK);
        }
        if (binaryList.get(2) == 1) {
            signalList.add(Signal.CLOSE_YOUR_EYES);
        }
        if (binaryList.get(1) == 1) {
            signalList.add(Signal.JUMP);
        }
        if (binaryList.get(0) == 1) {
            Collections.reverse(signalList);
        }

        return signalList;
    }

}
