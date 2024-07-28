class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar> {
    private int speed;
    private int distanceTravelled;
    private int numberOfVictories;

    public ProductionRemoteControlCar() {
        this.speed = 10;
        this.distanceTravelled = 0;
        this.numberOfVictories = 0;
    }

    public void drive() {
        this.distanceTravelled += this.speed;
    }

    public int getDistanceTravelled() {
        return this.distanceTravelled;
    }

    public int getNumberOfVictories() {
        return this.numberOfVictories;
    }

    public void setNumberOfVictories(int numberOfVictories) {
        this.numberOfVictories = numberOfVictories;
    }

    @Override
    public int compareTo(ProductionRemoteControlCar o) {
        return -Integer.compare(this.numberOfVictories, o.numberOfVictories);
    }
}
