using System;

public static class TelemetryBuffer
{
    public static byte[] ToBuffer(long reading)
    {
        byte[] buffer = new byte[9];
        byte[] bytes = BitConverter.GetBytes(reading);

        if (reading >= int.MinValue && reading < short.MinValue)
        {
            buffer[0] = (byte)(256 - 4);
        }
        else if (reading >= short.MinValue && reading < 0)
        {
            buffer[0] = (byte)(256 - 2);
        }
        else if (reading >= 0 && reading <= ushort.MaxValue)
        {
            buffer[0] = 2;
        }
        else if (reading > ushort.MaxValue && reading <= int.MaxValue)
        {
            buffer[0] = (byte)(256 - 4);
        }
        else if (reading > int.MaxValue && reading <= uint.MaxValue)
        {
            buffer[0] = 4;
        }
        else
        {
            buffer[0] = (byte)(256 - 8);
        }

        int bytesToCopy;
        if (buffer[0] < 8)
        {
            bytesToCopy = buffer[0];
        }
        else
        {
            bytesToCopy = buffer[0] - 256;
        }
        bytesToCopy = Math.Abs(bytesToCopy);

        Array.Copy(bytes, 0, buffer, 1, bytesToCopy);
        return buffer;
    }
    public static long FromBuffer(byte[] buffer)
    {
        if (buffer[0] == 256 - 8)
        {
            return BitConverter.ToInt64(buffer, 1);
        }
        else if (buffer[0] == 256 - 4)
        {
            return BitConverter.ToInt32(buffer, 1);
        }
        else if (buffer[0] == 256 - 2)
        {
            return BitConverter.ToInt16(buffer, 1);
        }
        else if (buffer[0] == 002)
        {
            return BitConverter.ToUInt16(buffer, 1);
        }
        else if (buffer[0] == 004)
        {
            return BitConverter.ToUInt32(buffer, 1);
        }
        else
        {
            return 0;
        }
    }
}

