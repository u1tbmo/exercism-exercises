class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {

        int length = (int) (Math.log10(numberToCheck) + 1);
        int sum = 0;
        int temp = numberToCheck;

        while (temp != 0) {
            int digit = temp % 10;
            sum += Math.pow(digit, length);
            temp /= 10;
        }

        return sum == numberToCheck;
    }

}
