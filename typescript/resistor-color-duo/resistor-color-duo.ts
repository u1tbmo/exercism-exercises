// A Color type, which is just an element of the COLORS array
type Color = typeof COLORS[number];

// This function now only accepts a Color
export const colorCode = (color: Color) => {
  return COLORS.indexOf(color);
};

// This function accepts a tuple of colors with at least two Colors
export function decodedValue(colors: [Color, Color, ...Color[]]) {
  const result = colors.slice(0, 2).map(colorCode).join("");
  return parseInt(result);
}

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
