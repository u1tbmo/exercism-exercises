import java.util.List;
import java.util.ArrayList;

class KindergartenGarden {
    private String gardenRow1;
    private String gardenRow2;
    
    KindergartenGarden(String garden) {
        String[] g = garden.split("\n");
        this.gardenRow1 = g[0];
        this.gardenRow2 = g[1];
    }

    List<Plant> getPlantsOfStudent(String student) {
        int place = (student.charAt(0) - 'A') * 2;
        List<Plant> plants = new ArrayList<>();
        plants.add(Plant.getPlant(gardenRow1.charAt(place)));
        plants.add(Plant.getPlant(gardenRow1.charAt(place + 1)));
        plants.add(Plant.getPlant(gardenRow2.charAt(place)));
        plants.add(Plant.getPlant(gardenRow2.charAt(place + 1)));
        return plants;
    }

}
