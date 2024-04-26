import tkinter as tk
from tkinter import font
from tkinter import messagebox
from random import randint
from re import match


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("The Hangman")
        self.resizable(0, 0)

        self._font = font.Font(family="Ubuntu", size="24")
        self._tries: int = 6
        self._animal: str = self.get_word()

        self._create_board()
        self._draw_scenario()
        self._add_word()

    def _create_board(self) -> None:
        self.frame = tk.Frame(self)

        self.label = tk.Label(self.frame,
                              text="The Hangman",
                              font=self._font)

        self.canvas = tk.Canvas(self.frame,
                                bg="#FFFFFF",
                                height=300,
                                width=300)

        self.frame.pack(fill=tk.X)
        self.label.pack()
        self.canvas.pack()

    def _draw_scenario(self) -> None:
        self.canvas.delete("all")
        self.canvas.create_line(150, 38.3, 150, 8.3, width=5)
        self.canvas.create_line(150, 8.3, 60, 8.3, width=5)
        self.canvas.create_line(60, 8.3, 60, 290, width=5)
        self.canvas.create_line(60, 290, 240, 290, width=5)

    def _add_word(self):
        self.format_word: str = ""

        for _ in self._animal:
            self.format_word = self.format_word + "_ "

        self.word = tk.Label(self.frame,
                             text=self.format_word,
                             font=self._font)

        self.word.pack()

    def _game_logic(self, letter: str) -> None:
        self.check_char(letter)

        guess: list = self.word.cget("text").split()
        temp: list = []
        aux: str = ""
        retry: bool = False

        if letter.capitalize() in self._animal:
            for idx in range(len(self._animal)):
                if self._animal[idx] == letter.capitalize():
                    guess[idx] = letter.capitalize()

            for idx in range(len(guess)):
                temp.append(guess[idx])
                temp.append(" ")

            for idx in range(len(temp)):
                aux += temp[idx]

            self.word.config(text=aux)
            self.label.config(text="OK")
        else:
            self.label.config(text="Try again")
            self._tries -= 1

        if self.word.cget("text").find("_") == -1:
            retry = messagebox.askyesno(
                "You won", "Congratulations! \nDo you want to play again?")
            self._play_again(retry)

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
            retry = messagebox.askyesno(
                "You lose", "The word was " + self._animal + "\nDo you want to play again?")
            self._play_again(retry)

    def _play_again(self, result):
        if result:
            self._tries = 6
            self._animal: str = self.get_word()
            self._draw_scenario()
            self.word.destroy()
            self._add_word()
        else:
            self.destroy()

    def check_char(self, s):
        try:
            if not bool(match('^[a-zA-Z]*$', s)):
                raise ValueError
        except ValueError:
            messagebox.showwarning(message="Write only letters")

    def get_word(self) -> str:
        self.animals = [
            'ANT',
            'BEE',
            'BEETLE',
            'BUTTERFLY',
            'CICADA',
            'CRICKET',
            'DRAGONFLY',
            'FIREFLY',
            'GRASSHOPPER',
            'HORNET',
            'LADYBUG',
            'MANTIS',
            'MOSQUITO',
            'WASP',
            'TERMITES',
            'TERMITE',
            'FLY',
            'HOUSEFLY',
            'DRAGONFLY',
            'DROSOPHILA',
            'HORSEFLY',
            'MOSQUITO',
            'BLOWFLY',
            'LACEWING',
            'MAYFLY',
            'COCKROACH',
            'TERMITES',
            'TERMITE',
            'LICE',
            'FLEA',
            'TICK',
            'SPIDERS',
            'TARANTULA',
            'SCORPION',
            'CENTIPEDE',
            'MILLIPEDE',
            'SILVERFISH',
            'EARWIG',
            'MOTH',
            'CATERPILLAR',
            'SLUG',
            'SNAIL',
            'CLAM',
            'WORM',
            'LEECH',
            'PLANARIAN',
            'EARTHWORM',
            'FLATWORM',
            'TAPEWORM',
            'ROUNDWORM',
            'NEMATODE',
            'HOOKWORM',
            'PINWORM',
            'BLOODWORM',
            'LION',
            'TIGER',
            'BEAR',
            'ELEPHANT',
            'GIRAFFE',
            'ZEBRA',
            'HIPPOPOTAMUS',
            'GORILLA',
            'CHIMPANZEE',
            'MONKEY',
            'KANGAROO',
            'KOALA',
            'PLATYPUS',
            'WOMBAT',
            'RACCOON',
            'SKUNK',
            'OPOSSUM',
            'ARMADILLO',
            'PORCUPINE',
            'HEDGEHOG',
            'BADGER',
            'OTTER',
            'WEASEL',
            'FERRET',
            'MARTEN',
            'MUSKRAT',
            'MINK',
            'FOX',
            'WOLF',
            'COYOTE',
            'BOBCAT',
            'LYNX',
            'COUGAR',
            'PANTHER',
            'JAGUAR',
            'LEOPARD',
            'CHEETAH',
            'DEER',
            'MOOSE',
            'ELK',
            'CARIBOU',
            'BISON',
            'BUFFALO',
            'ANTELOPE',
            'GAZELLE',
            'WARTHOG',
            'HYENA',
            'MEERKAT',
            'LEMUR',
            'SLOTH',
            'ANTEATER',
            'AARDVARK',
            'BAT',
            'SQUIRREL',
            'CHIPMUNK',
            'BEAVER',
            'MUSKRAT',
            'RAT',
            'MOUSE',
            'RABBIT',
            'HARE',
            'COYPU',
            'NUTRIA',
            'CAPYBARA',
            'PORCUPINE',
            'PANGOLIN',
            'MOLE',
            'SHREW',
            'VOLE',
            'LEMMING',
            'JERBOA',
            'GOPHER',
            'MARMOT',
            'MUSKOX',
            'YAK',
            'LLAMA',
            'ALPACA',
            'VICUNA',
            'GUANACO',
            'TAPIR',
            'PECCARY',
            'MANATEE',
            'DOLPHIN',
            'PORPOISE',
            'WHALE',
            'SEAL',
            'WALRUS',
            'OTTER',
            'NARWHAL',
            'BELUGA',
            'SPARROW',
            'FINCH',
            'PIGEON',
            'DOVE',
            'PELICAN',
            'SWAN',
            'GOOSE',
            'DUCK',
            'OSPREY',
            'HAWK',
            'EAGLE',
            'FALCON',
            'VULTURE',
            'OWL',
            'PUFFIN',
            'PARROT',
            'MACAW',
            'COCKATOO',
            'TOUCAN',
            'LOON',
            'GULL',
            'SEAGULL',
            'HERON',
            'EGRET',
            'IBIS',
            'STORK',
            'CRANES',
            'TURKEY',
            'CHICKEN',
            'QUAIL',
            'PHEASANT',
            'PEACOCK',
            'OSTRICH',
            'EMU',
            'RHEA',
            'CASSOWARY',
            'KIWI',
            'KOOKABURRA',
            'KINGFISHER',
            'WOODPECKER',
            'GOSHAWK',
            'HARRIER',
            'KESTREL',
            'BUZZARD',
            'SPARROW',
            'FINCH',
            'SALMON',
            'TUNA',
            'COD',
            'HALIBUT',
            'SARDINES',
            'ANCHOVIES',
            'CATFISH',
            'TILAPIA',
            'CARP',
            'SNAPPER',
            'GROUPER',
            'SOLE',
            'FLOUNDER',
            'TROUT',
            'BASS',
            'WALLEYE',
            'CATFISH',
            'PERCH',
            'CRAPPIE',
            'BLUEGILL',
            'SUNFISH',
            'PICKEREL',
            'MUSKELLUNGE',
            'STEELHEAD',
            'GRAYLING',
            'SWORDFISH',
            'FROG',
            'TOAD',
            'SALAMANDER',
            'NEWT',
            'CAECILIAN',
            'AXOLOTL',
            'HELLBENDER',
            'SNAKE',
            'LIZARD',
            'TURTLE',
            'CROCODILE',
            'ALLIGATOR',
            'GECKO',
            'IGUANA',
            'SKINK',
            'MONITOR',
            'PYTHON',
            'COBRA',
            'RATTLESNAKE',
            'ANACONDA',
            'KING COBRA',
            'BOA',
            'VIPER',
            'TORTOISE',
            'TERRAPIN',
            'GILA',]

        idx = randint(0, len(self.animals)-1)
        return self.animals[idx]

    def keypress(self, event) -> None:
        self._game_logic(event.char)


def main() -> None:
    app = Window()
    app.bind("<Key>", app.keypress)
    app.mainloop()


if __name__ == '__main__':
    main()
