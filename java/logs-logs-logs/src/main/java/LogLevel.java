public enum LogLevel {
    UNKNOWN("UNK", 0),
    TRACE("TRC", 1),
    DEBUG("DBG", 2),
    INFO("INF", 4),
    WARNING("WRN", 5),
    ERROR("ERR", 6),
    FATAL("FTL", 42);

    private final String level;
    private final int number;

    LogLevel(String level, int number) {
        this.level = level;
        this.number = number;
    }

    public String getLevel() {
        return this.level;
    }

    public int getNumber() {
        return this.number;
    }
}
