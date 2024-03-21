import random
import time

class GuessingGame:
    def __init__(self):
        self.difficulty_settings = {
            'easy': (1, 100),
            'medium': (1, 200),
            'hard': (1, 500),
        }
        self.difficulty = 'easy'
        self.total_games = 0
        self.total_attempts = 0
        self.total_time_taken = 0.0
        self.set_difficulty()

    def set_difficulty(self):
        print("Select difficulty (easy, medium, hard):")
        while True:
            self.difficulty = input().lower()
            if self.difficulty in self.difficulty_settings:
                break
            print("Invalid difficulty. Choose from easy, medium, hard.")
        self.range_min, self.range_max = self.difficulty_settings[self.difficulty]

    def reset(self):
        self.target_number = random.randint(self.range_min, self.range_max)
        self.attempts = 0
        self.start_time = time.time()

    def provide_hint(self, guess):
        difference = abs(self.target_number - guess)
        if self.difficulty == 'easy':
            if difference > 50:
                return "Ice cold!"
            elif difference > 20:
                return "Cold."
            elif difference > 10:
                return "Warm."
            elif difference > 5:
                return "Hot."
            else:
                return "Very hot!"
        elif self.difficulty == 'medium':
            if difference > 100:
                return "Freezing!"
            elif difference > 50:
                return "Very cold."
            elif difference > 25:
                return "Warmish."
            elif difference > 10:
                return "Quite warm."
            else:
                return "Very warm!"
        else:  # hard
            if difference % 2 == 0:
                return "You're even with me."
            else:
                return "You're odd with me. Think different."

    def play_round(self):
        self.reset()
        print(f"\nGuess the number between {self.range_min} and {self.range_max}.")

        while True:
            try:
                guess = int(input("Your guess: "))
                if guess < self.range_min or guess > self.range_max:
                    print(f"Please enter a valid number between {self.range_min} and {self.range_max}.")
                    continue

                self.attempts += 1

                if guess < self.target_number:
                    print(f"Too low! Hint: {self.provide_hint(guess)}")
                elif guess > self.target_number:
                    print(f"Too high! Hint: {self.provide_hint(guess)}")
                else:
                    time_taken = time.time() - self.start_time
                    print(f"Congratulations! You've guessed it in {self.attempts} attempts and it took you {time_taken:.2f} seconds.")
                    self.total_time_taken += time_taken
                    break
            except ValueError:
                print("That's not a valid number. Please try again.")

    def play(self):
        try:
            while True:
                self.play_round()
                self.total_games += 1
                self.total_attempts += self.attempts

                play_again = input("Play again? (yes/no): ").lower()
                if play_again != "yes":
                    average_time_per_game = self.total_time_taken / self.total_games
                    print(f"\nTotal games played: {self.total_games}, Average attempts per game: {self.total_attempts / self.total_games:.2f}, Average time per game: {average_time_per_game:.2f} seconds")
                    print("Thanks for playing!")
                    break
        except KeyboardInterrupt:
            print("\nGame interrupted. Thanks for playing!")

if __name__ == "__main__":
    game = GuessingGame()
    game.play()
