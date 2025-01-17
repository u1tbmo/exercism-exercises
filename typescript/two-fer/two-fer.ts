export function twoFer(name: string = ""): string {
  return `One for ${name.length === 0 ? "you" : name}, one for me.`;
}
