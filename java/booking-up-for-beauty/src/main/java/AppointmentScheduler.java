import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

class AppointmentScheduler {
    public LocalDateTime schedule(String appointmentDateDescription) {
        DateTimeFormatter parser = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
        return LocalDateTime.parse(appointmentDateDescription, parser);
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        return appointmentDate.isBefore(LocalDateTime.now());
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        LocalTime time = appointmentDate.toLocalTime();
        LocalTime afternoonStart = LocalTime.of(12, 0);
        LocalTime afternoonEnd = LocalTime.of(18, 0);
        return (time.isAfter(afternoonStart) || time.equals(afternoonStart))
                && time.isBefore(afternoonEnd);
    }

    public String getDescription(LocalDateTime appointmentDate) {
        DateTimeFormatter datePrinter = DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy,");
        DateTimeFormatter timePrinter = DateTimeFormatter.ofPattern("h:mm a");
        String dateString = datePrinter.format(appointmentDate);
        String timeString = timePrinter.format(appointmentDate).toUpperCase();
        return String.format("You have an appointment on %s at %s.", dateString, timeString);
    }

    public LocalDate getAnniversaryDate() {
        return LocalDate.of(LocalDate.now().getYear(), 9, 15);
    }
}
