using System;
using System.Text;

public static class Identifier
{
    public static string Clean(string identifier)
    {
        StringBuilder sb = new StringBuilder(identifier);
        // replaces whitespace with an underscore
        sb.Replace(' ', '_');

        // replaces control characters with the string "CTRL"
        for (int i = 0; i < sb.Length; i++)
        {
            if (Char.IsControl(sb[i]))
            {
                sb.Replace(sb[i].ToString(), "CTRL");
            }
        }

        // converts the string from kebab-case to camelCase
        for (int i = 0; i < sb.Length; i++)
        {
            if (sb[i] == '-')
            {
                sb.Remove(i, 1);
                sb[i] = Char.ToUpper(sb[i]);
            }
        }

        // removes all non-letters from the string except for underscores
        for (int i = 0; i < sb.Length; i++)
        {
            if (!Char.IsLetter(sb[i]) && sb[i] != '_')
            {
                sb.Remove(i, 1);
                i--;
            }
        }

        // removes all lowercase greek letters from the string
        for (int i = 0; i < sb.Length; i++)
        {
            if (sb[i] >= 945 && sb[i] <= 969)
            {
                sb.Remove(i, 1);
                i--;
            }
        }

        return sb.ToString();
    }
}