import java.time.LocalDate;
import java.time.LocalDateTime;

public class Gigasecond {
    private final static long GIGASECOND = 1_000_000_000;
    LocalDateTime gigasecondLaterDateTime;

    public Gigasecond(LocalDate moment) {
        LocalDateTime momentAsDateTime = moment.atStartOfDay();
        momentAsDateTime = momentAsDateTime.plusSeconds(GIGASECOND);
        this.gigasecondLaterDateTime = momentAsDateTime;
    }

    public Gigasecond(LocalDateTime moment) {
        this.gigasecondLaterDateTime = moment.plusSeconds(GIGASECOND);
    }

    public LocalDateTime getDateTime() {
        return gigasecondLaterDateTime;
    }
}
