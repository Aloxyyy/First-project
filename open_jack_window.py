import random
from tkinter import *
from fpdf import *
from time import *
import datetime
from PIL import Image, ImageTk
from subprocess import call


deck_of_cards = [
    '6c', '6p', '6b', '6k'
    '7c', '7p', '7b', '7k'
    '8c', '8p', '8b', '8k'
    '9c', '9p', '9b', '9k'
    '10c', '10p', '10b', '10k'
    'jackc', 'jackp', 'jackb', 'jackk'
    'jackc', 'jackp', 'jackb', 'jackk'
    'queenc', 'queenp', 'queenb', 'queenk'
    'kingc', 'kingp', 'kingb', 'kingk'
    'acec', 'acep', 'aceb', 'acek'
]

random.shuffle(deck_of_cards)


black_jack_open_window = Tk()
black_jack_open_window.resizable(0, 0)
black_jack_open_window.title('Блэк Джек')
black_jack_open_window.geometry('800x533')

class bckgrnd_black_jack(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("black_jack_background.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

back_black_jack = bckgrnd_black_jack(black_jack_open_window)
back_black_jack.pack(fill=BOTH, expand=YES)

black_jack_open_window.mainloop()