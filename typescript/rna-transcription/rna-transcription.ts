export function toRna(strand: string): string {
  // Create the transcription
  const transcription: Map<string, string> = new Map(
    [["G", "C"], ["C", "G"], ["T", "A"], ["A", "U"]],
  );

  // Iterate over the string and create the resulting transcription
  let transcibedString: string = "";
  for (const char of strand) {
    if (!(transcription.has(char))) {
      throw new Error("Invalid input DNA.");
    }
    transcibedString += transcription.get(char);
  }

  // Return the resulting string
  return transcibedString;
}
