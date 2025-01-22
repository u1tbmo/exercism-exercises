// A Color type, which is just an element of the COLORS array
type Color = typeof COLORS[number];

// This function now only accepts a Color
export const colorCode = (color: Color) => {
  return COLORS.indexOf(color);
};

// A const color tuple
export const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
] as const;

// A map of the metric conversions
const METRIC_SYSTEM = new Map<number, string>([
  [1_000_000_000, "giga"],
  [1_000_000, "mega"],
  [1_000, "kilo"],
  [1, ""],
]);

export function decodedResistorValue(colors: [Color, Color, ...Color[]]) {
  const ohms: number = parseInt(
    colors.slice(0, 2).map(colorCode).join("") +
      "0".repeat(colorCode(colors[2])),
  );

  // 0 ohms is the minimum value
  if (ohms === 0) {
    return `${ohms} ohms`;
  }

  // Iterate over the map to check for the best prefix
  for (const [value, prefix] of METRIC_SYSTEM) {
    if (ohms / value >= 1) {
      return `${ohms / value} ${prefix}ohms`;
    }
  }
}
