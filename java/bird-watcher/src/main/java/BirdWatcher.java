class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return new int[] { 0, 2, 5, 3, 7, 8, 4 };
    }

    public int getToday() {
        return this.birdsPerDay[6];
    }

    public void incrementTodaysCount() {
        ++this.birdsPerDay[6];
    }

    public boolean hasDayWithoutBirds() {
        for (int birdCount : this.birdsPerDay) {
            if (birdCount == 0) {
                return true;
            }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;
        int length = numberOfDays <= 7 ? numberOfDays : 7;
        for (int i = 0; i < length; i++) {
            count += this.birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int count = 0;
        for (int birdCount : this.birdsPerDay) {
            if (birdCount >= 5) {
                count++;
            }
        }
        return count;
    }
}
