// A Color type, which is just an element of the COLORS array
type Color = typeof COLORS[number];

// This function now only accepts a Color
export const colorCode = (color: Color) => {
  return COLORS.indexOf(color);
};

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
