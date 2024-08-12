import java.util.HashMap;

class SpaceAge {
    double ageInSeconds;
    HashMap<String, Double> planetFactors = new HashMap<>() {
        {
            put("mercury", 7600521.6);
            put("venus", 19414080.0);
            put("earth", 31556952.0);
            put("mars", 59356800.0);
            put("jupiter", 374222560.0);
            put("saturn", 929596608.0);
            put("uranus", 2651486400.0);
            put("neptune", 5200418592.0);
        }
    };


    SpaceAge(double seconds) {
        this.ageInSeconds = seconds;
    }

    double getSeconds() {
        return this.ageInSeconds;
    }

    double calculateAge(String planet) {
        return ageInSeconds / planetFactors.get(planet);
    }


    double onEarth() {
        return calculateAge("earth");
    }

    double onMercury() {
        return calculateAge("mercury");
    }

    double onVenus() {
        return calculateAge("venus");
    }

    double onMars() {
        return calculateAge("mars");
    }

    double onJupiter() {
        return calculateAge("jupiter");
    }

    double onSaturn() {
        return calculateAge("saturn");
    }

    double onUranus() {
        return calculateAge("uranus");
    }

    double onNeptune() {
        return calculateAge("neptune");
    }

}
