import tkinter as tk
import random
#BY SOLEOUS AKA Neksha

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("300x200")

        self.number_to_guess = random.randint(1, 100)
        self.guesses = 0

        self.create_widgets()

    def create_widgets(self):
        self.guess_label = tk.Label(self, text="Guess a number between 1 and 100:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(self)
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.guesses += 1

        if guess == self.number_to_guess:
            self.result_label.config(text=f"Correct! It took you {self.guesses} guesses.", fg="green")
            self.number_to_guess = random.randint(1, 100) # generate a new random number
            self.guesses = 0
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high, try again.", fg="red")
        else:
            self.result_label.config(text="Too low, try again.", fg="blue")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.mainloop()

#BY SOLEOUS :D aka Neksha
