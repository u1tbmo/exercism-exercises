public class SalaryCalculator {
    private static final double BASE_SALARY = 1000.0;
    private static final double SALARY_CAP = 2000.0;

    public double salaryMultiplier(int daysSkipped) {
        return daysSkipped < 5 ? 1.0 : 0.85;
    }

    public int bonusMultiplier(int productsSold) {
        return productsSold >= 20 ? 13 : 10;
    }

    public double bonusForProductsSold(int productsSold) {
        return productsSold * bonusMultiplier(productsSold);
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        double result = salaryMultiplier(daysSkipped) * BASE_SALARY + bonusForProductsSold(productsSold);
        return result <= SALARY_CAP ? result : SALARY_CAP;
    }
}
