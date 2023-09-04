using System;

static class LogLine
{
    // Returns the range of the string logLine starting from the character after ';' until the end of the string.
    // Then it trims the string to remove all leading and trailing whitespace.
    public static string Message(string logLine) => logLine[(logLine.IndexOf(':') + 1)..].Trim();

    // Returns the range starting from index 1 which is always the character after '[' until the character before ']', then converts the string to lowercase.
    // Example: In range [1:3], the 3 is not included in the range.
    public static string LogLevel(string logLine) => logLine[1..logLine.IndexOf(']')].ToLower();

    // Returns a formatted string using the previous two methods.
    public static string Reformat(string logLine) => $"{Message(logLine)} ({LogLevel(logLine)})";
}