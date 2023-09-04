using System;

public static class PhoneNumber
{
    public static (bool IsNewYork, bool IsFake, string LocalNumber) Analyze(string phoneNumber)
    {
        string[] parts = phoneNumber.Split('-');
        if (parts.Length != 3)
        {
            throw new ArgumentException("Invalid phone number");
        }
        return (parts[0] == "212", parts[1] == "555", parts[2]);
    }

    public static bool IsFake((bool IsNewYork, bool IsFake, string LocalNumber) phoneNumberInfo)
    {
        return phoneNumberInfo.IsFake;
    }
}
