const secondsPerEarthYear = 31_557_600;
const secondsPerPlanetYearMap = new Map<string, number>(
  [
    ["mercury", 0.2408467 * secondsPerEarthYear],
    ["venus", 0.61519726 * secondsPerEarthYear],
    ["earth", secondsPerEarthYear],
    ["mars", 1.8808158 * secondsPerEarthYear],
    ["jupiter", 11.862615 * secondsPerEarthYear],
    ["saturn", 29.447498 * secondsPerEarthYear],
    ["uranus", 84.016846 * secondsPerEarthYear],
    ["neptune", 164.79132 * secondsPerEarthYear],
  ],
);

export function age(planet: string, seconds: number): number {
  const secondsPerPlanetYear = secondsPerPlanetYearMap.get(planet);
  if (secondsPerPlanetYear !== undefined) {
    return parseFloat((seconds / secondsPerPlanetYear).toFixed(2));
  }
  throw new Error("Error: Invalid planet.");
}
