import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class DnDCharacter {
    private static final Random random = new Random();
    private static final int DICE_SIDES = 6;
    private static final int DICE_ROLLS = 4;
    private static final int HITPOINTS_BASE = 10;

    private final int strength;
    private final int dexterity;
    private final int intelligence;
    private final int wisdom;
    private final int charisma;
    private final int constitution;
    private final int hitpoints;

    DnDCharacter() {
        this.strength = ability(rollDice());
        this.dexterity = ability(rollDice());
        this.constitution = ability(rollDice());
        this.intelligence = ability(rollDice());
        this.wisdom = ability(rollDice());
        this.charisma = ability(rollDice());
        this.hitpoints = HITPOINTS_BASE + modifier(this.constitution);
    }

    int ability(List<Integer> scores) {
        int sum = 0;
        int minimum = Integer.MAX_VALUE;
        for (int score : scores) {
            sum += score;
            if (score < minimum) {
                minimum = score;
            }
        }
        return sum - minimum;
    }

    List<Integer> rollDice() {
        List<Integer> diceRolls = new ArrayList<>();
        for (int i = 0; i < DICE_ROLLS; i++) {
            diceRolls.add(random.nextInt(1, DICE_SIDES + 1));
        }
        return diceRolls;
    }

    int modifier(int input) {
        return Math.floorDiv(input - 10, 2);
    }

    int getStrength() {
        return this.strength;
    }

    int getDexterity() {
        return this.dexterity;
    }

    int getConstitution() {
        return this.constitution;
    }

    int getIntelligence() {
        return this.intelligence;
    }

    int getWisdom() {
        return this.wisdom;
    }

    int getCharisma() {
        return this.charisma;
    }

    int getHitpoints() {
        return this.hitpoints;
    }
}
