class RaindropConverter {

    String convert(int number) {
        String result = new String();
        if (number % 3 == 0) {
            result += "Pling";
        }
        if (number % 5 == 0) {
            result += "Plang";
        }
        if (number % 7 == 0) {
            result += "Plong";
        }
        return (result.isEmpty()) ? String.valueOf(number) : result.toString();
    }

}
