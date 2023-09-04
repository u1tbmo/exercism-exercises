using System;

public static class LogAnalysis 
{
    public static string SubstringAfter(this string logLine, string str) =>
        logLine[(logLine.IndexOf(str) + str.Length)..];

    public static string SubstringBetween(this string logLine, string start, string end) =>
        logLine[(logLine.IndexOf(start) + start.Length)..(logLine.IndexOf(end))];
    
    public static string Message(this string logLine) =>
        SubstringAfter(logLine, ":").Trim();

    public static string LogLevel(this string logLine) =>
        SubstringBetween(logLine, "[", "]");
}