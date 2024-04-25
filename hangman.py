import tkinter as tk
from tkinter import font
from tkinter import messagebox
from random import randint


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("The Hangman")
        self.resizable(0, 0)

        self._font = font.Font(family="Ubuntu", size="24")
        self._tries = 6

        self._create_board()

    def _create_board(self) -> None:
        self.frame = tk.Frame(self)

        self.label = tk.Label(self.frame,
                              text="The Hangman",
                              font=self._font)

        self.canvas = tk.Canvas(self.frame,
                                bg="#FFFFFF",
                                height=300,
                                width=300)
        
        self.animal = self.get_word()
        self.format_word = ""
        print(self.animal)

        for _ in self.animal:
            self.format_word = self.format_word + "_ "

        self.word = tk.Label(self.frame,
                             text=self.format_word,
                             font=self._font)

        self.frame.pack(fill=tk.X)
        self.label.pack()
        self.canvas.pack()
        self.word.pack()

    def _game_logic(self, letter: str) -> None:
        print(letter.capitalize())

        if letter.capitalize() in self.animal:
            self.label.config(text="OK")
        else:
            self.label.config(text="Try again")
            self._tries -= 1

        if self._tries == 5:
            self.canvas.create_oval(118.3, 38.3, 181.6, 101.6, width=3)
        elif self._tries == 4:
            self.canvas.create_line(150, 101.6, 150, 191.6, width=3)
        elif self._tries == 3:
            self.canvas.create_line(150, 101.6, 180, 171.6, width=3)
        elif self._tries == 2:
            self.canvas.create_line(150, 101.6, 120, 171.6, width=3)
        elif self._tries == 1:
            self.canvas.create_line(150, 191.6, 180, 271.6, width=3)
        elif self._tries == 0:
            self.canvas.create_line(150, 191.6, 120, 271.6, width=3)
            messagebox.showinfo("You lose", "The word was " + self.animal)

    def get_word(self) -> str:
        self.animals = [
            'CAT',
            'COW',
            'DOG',
            'DONKEY',
            'DUCK',
            'GOAT',
            'GOOSE',
            'HEN',
            'HORSE',
            'PIG',
            'SHEEP',
            'TURKEY',
            'ARMADILLO',
            'ELEPHANT',
            'GIANT PANDA',
            'GIRAFFE',
            'LION',
            'MONKEY',
            'TURTLE',
            'ZEBRA',
            'COUGAR',
            'DOLPHIN',
            'EMU',
            'EAGLE',
            'KANGAROO',
            'LEOPARD',
            'MOOSE',
            'RHINOCEROS',
            'SNAKE',
            'TIGER',
            'WHALE',
            'ANEMONE',
            'CRAB',
            'CUTTLEFISH',
            'EEL',
            'JELLYFISH',
            'OCTOPUS',
            'OYSTER',
            'SHARK',
            'SHRIMP',
            'TUNA',]

        self.idx = randint(0, len(self.animals)-1)
        return self.animals[self.idx]
    
    def keypress(self, event) -> None:
        self._game_logic(event.char)


def main() -> None:
    app = Window()
    app.bind("<Key>", app.keypress)
    app.mainloop()


if __name__ == '__main__':
    main()
