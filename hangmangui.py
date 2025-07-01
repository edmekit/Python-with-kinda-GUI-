import random, tkinter as tk

err = 0
progress = ["_" for i in len(word)]
hangman = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

#funcs
def start_game():
    words = [
    "python", "banana", "window", "guitar", "planet",
    "orange", "rocket", "flower", "castle", "jungle",
    "pencil", "rabbit", "cloud", "bridge", "forest",
    "dragon", "camera", "pirate", "wizard", "island"]
    word = random.choice(words)
    man.config(text=f"{hangman[err]}\n {" ".join(progress)}")

def guesser():
    enter_guess.delete(0,tk.END)
    guessers = enter_guess.get()
    #icqntfoucus bro




window = tk.Tk()
window.title("Hangman")
window.geometry("800x600")
start = tk.Button(window, text="Start game", width=10, command=start_game)
start.grid(row=0, column=0, padx=5, pady=5)
man = tk.Label(window, text="hey", width=20, height=10)
man.grid(row=1, column=0, padx=5, pady=5,columnspan=2)
enter_guess = tk.Entry(window, width=5)
enter_guess.grid(row=2, column=0, padx=5, pady=5)
guess = tk.Button(window, text="guess", width=5)
guess.grid(row=2, column=1, padx=5, pady=5)







window.mainloop()