public class LogLine {
    private final String log;

    public LogLine(String log) {
        this.log = log;
    }

    public LogLevel getLogLevel() {
        String logLevel = this.log.substring(
                this.log.indexOf('[') + 1,
                this.log.indexOf(']')).trim();
        for (LogLevel lvl : LogLevel.values()) {
            if (lvl.getLevel().equals(logLevel)) {
                return lvl;
            }
        }
        return LogLevel.UNKNOWN;
    }

    public String getOutputForShortLog() {
        return String.format("%d:%s",
                this.getLogLevel().getNumber(),
                this.log.split(":")[1].trim());
    }
}
