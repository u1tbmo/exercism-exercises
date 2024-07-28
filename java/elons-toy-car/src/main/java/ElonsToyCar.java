public class ElonsToyCar {
    private int batteryLevel = 100;
    private int metersDriven = 0;

    public static ElonsToyCar buy() {
        return new ElonsToyCar();
    }

    public String distanceDisplay() {
        return String.format("Driven %d meters", this.metersDriven);
    }

    public String batteryDisplay() {
        return (this.batteryLevel > 0) ? String.format("Battery at %d%%", this.batteryLevel) : "Battery empty";
    }

    public void drive() {
        if (batteryLevel > 0) {
            batteryLevel--;
            metersDriven += 20;
        }
    }
}
