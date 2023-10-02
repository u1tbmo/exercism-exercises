using System;

enum LogLevel
{
    Unknown = 0,
    Trace = 1,
    Debug = 2,
    Info = 4,
    Warning = 5,
    Error = 6,
    Fatal = 42,
}

static class LogLine
{
    public static LogLevel ParseLogLevel(string logLine)
    {
        logLine = logLine[1..4];
        if (logLine == "TRC") {return LogLevel.Trace;}
        if (logLine == "DBG") {return LogLevel.Debug;}
        if (logLine == "INF") {return LogLevel.Info;}
        if (logLine == "WRN") {return LogLevel.Warning;}
        if (logLine == "ERR") {return LogLevel.Error;}
        if (logLine == "FTL") {return LogLevel.Fatal;}
        return LogLevel.Unknown;
    }

    public static string OutputForShortLog(LogLevel logLevel, string message) => $"{(int)logLevel}:{message}";
}
