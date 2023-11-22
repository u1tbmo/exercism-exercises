STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses: int = 9
        self.status: str = STATUS_ONGOING
        self.word_list: list[str] = list(word)
        self.masked_word_list: list[str] = ["_"] * len(word)

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        guessed_correctly: bool = False
        for index, c in enumerate(self.word_list):
            if c == char:
                self.masked_word_list[index] = char
                self.word_list[index] = "#"
                guessed_correctly = True
        if not guessed_correctly:
            self.remaining_guesses -= 1

        if "_" in self.masked_word_list and self.remaining_guesses == -1:
            self.status = STATUS_LOSE
        if "_" not in self.masked_word_list:
            self.status = STATUS_WIN

    def get_masked_word(self):
        return "".join(self.masked_word_list)

    def get_status(self):
        return self.status


game = Hangman("aaa")
for ch in "bcdefghij":
    game.guess(ch)
    print(game.remaining_guesses)
    print(game.get_status())
    print(game.get_masked_word())
game.guess("a")
# self.assertEqual(game.remaining_guesses, 0)
# self.assertEqual(game.get_status(), hangman.STATUS_WIN)
# self.assertEqual(game.get_masked_word(), "aaa")
print(game.remaining_guesses)
print(game.get_status())
print(game.get_masked_word())
