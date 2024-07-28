class Darts {
    int score(double xOfDart, double yOfDart) {
        double hypotenuse = Math.sqrt(Math.pow(xOfDart, 2) + Math.pow(yOfDart, 2));
        return hypotenuse > 10 ? 0 : hypotenuse > 5 ? 1 : hypotenuse > 1 ? 5 : 10;
    }
}
