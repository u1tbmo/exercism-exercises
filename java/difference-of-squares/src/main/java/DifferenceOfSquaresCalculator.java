class DifferenceOfSquaresCalculator {

    int computeSquareOfSumTo(int input) {
        int partialSum = (input * (1 + input)) / 2;
        return partialSum * partialSum;
    }

    int computeSumOfSquaresTo(int input) {
        return (input * (input + 1) * (2 * input + 1)) / 6;
    }

    int computeDifferenceOfSquares(int input) {
        return computeSquareOfSumTo(input) - computeSumOfSquaresTo(input);
    }

}
