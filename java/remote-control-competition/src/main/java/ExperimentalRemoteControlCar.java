public class ExperimentalRemoteControlCar implements RemoteControlCar {
    private int speed;
    private int distanceTravelled;

    public ExperimentalRemoteControlCar() {
        this.speed = 20;
        this.distanceTravelled = 0;
    }

    public void drive() {
        this.distanceTravelled += speed;
    }

    public int getDistanceTravelled() {
        return this.distanceTravelled;
    }
}
