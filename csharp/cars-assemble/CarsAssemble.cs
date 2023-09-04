using System;

static class AssemblyLine
{
    private static readonly int ratePerHour = 221;

    public static double SuccessRate(int speed)
    {
        if (speed == 0)
        {
            return 0.0;
        }
        else if (1 <= speed && speed <= 4)
        {
            return 1.0;
        }
        else if (5 <= speed && speed <= 8)
        {
            return 0.9;
        }
        else if (speed == 9)
        {
            return 0.80;
        }
        else if (speed == 10)
        {
            return 0.77;
        }
        else
        {
            throw new ArgumentException("Invalid speed");
        }
    }
    
    public static double ProductionRatePerHour(int speed)
    {
        return ratePerHour * SuccessRate(speed) * speed;
    }

    public static int WorkingItemsPerMinute(int speed)
    {
        return (int)ProductionRatePerHour(speed) / 60;
    }
}
