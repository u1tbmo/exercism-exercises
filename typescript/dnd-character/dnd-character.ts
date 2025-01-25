export class DnDCharacter {
  static readonly MAX_ROLLS: number = 4;
  hitpoints: number;
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;

  constructor() {
    this.strength = DnDCharacter.generateAbilityScore();
    this.dexterity = DnDCharacter.generateAbilityScore();
    this.constitution = DnDCharacter.generateAbilityScore();
    this.intelligence = DnDCharacter.generateAbilityScore();
    this.wisdom = DnDCharacter.generateAbilityScore();
    this.charisma = DnDCharacter.generateAbilityScore();
    this.hitpoints = 10 + DnDCharacter.getModifierFor(this.constitution);
  }

  public static generateAbilityScore(): number {
    const rolls = [];
    for (let i = 0; i < this.MAX_ROLLS; i++) {
      rolls.push(Math.floor(1 + Math.random() * 6));
    }
    rolls.sort((a, b) => b - a);
    rolls.pop();
    return rolls.reduce((sum, e) => sum + e, 0);
  }

  public static getModifierFor(abilityValue: number): number {
    return Math.floor((abilityValue - 10) / 2);
  }
}
