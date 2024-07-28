class NeedForSpeed {
    public final int speed;
    public final int batteryDrain;
    public int batteryLevel;
    private int distanceDriven;

    NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
        this.distanceDriven = 0;
        this.batteryLevel = 100;
    }

    public boolean batteryDrained() {
        return this.batteryLevel - this.batteryDrain < 0;
    }

    public int distanceDriven() {
        return this.distanceDriven;
    }

    public void drive() {
        if (!batteryDrained()) {
            this.distanceDriven += speed;
            this.batteryLevel -= batteryDrain;
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }
}


class RaceTrack {
    private int distance;

    RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean canFinishRace(NeedForSpeed car) {
        return car.batteryLevel / car.batteryDrain * car.speed >= distance;
    }
}
