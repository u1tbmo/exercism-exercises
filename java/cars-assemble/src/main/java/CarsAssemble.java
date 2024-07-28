public class CarsAssemble {
    private static int carsProducedPerHour = 221;

    private double productionSuccessRate(int speed) {
        if (speed >= 1 && speed <= 4) {
            return 1.0;
        } else if (speed >= 5 && speed <= 8) {
            return 0.9;
        } else if (speed == 9) {
            return 0.8;
        } else {
            return 0.77;
        }
    }

    public double productionRatePerHour(int speed) {
        return carsProducedPerHour * speed * productionSuccessRate(speed);
    }

    public int workingItemsPerMinute(int speed) {
        return (int) (productionRatePerHour(speed) / 60);
    }
}
