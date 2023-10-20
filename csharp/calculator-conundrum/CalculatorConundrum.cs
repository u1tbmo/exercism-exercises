using System;

public static class SimpleCalculator
{
    public static string Calculate(int operand1, int operand2, string operation)
    {
        if (operation == "+")
        {
            var sum = operand1 + operand2;
            return $"{operand1} + {operand2} = {sum}";
        }
        else if (operation == "*")
        {
            var product = operand1 * operand2;
            return $"{operand1} * {operand2} = {product}";
        }
        else if (operation == "/")
        {
            float quotient;
            try
            {
                quotient = operand1 / operand2;
            }
            catch (DivideByZeroException)
            {
                return "Division by zero is not allowed.";
            }
            return $"{operand1} / {operand2} = {quotient}";
        }
        else
        {
            if (operation == string.Empty)
            {
                throw new ArgumentException("Operation cannot be empty");
            }
            else if(operation == null)
            {
                throw new ArgumentNullException("Operation cannot be null");
            }
            else
            {
                throw new ArgumentOutOfRangeException($"Operation {operation} is not supported");
            }
        }
    }
}
