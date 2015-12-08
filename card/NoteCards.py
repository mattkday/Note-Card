__author__ = 'Matthew00'
import os
import Tkinter


class SampleApp:
    def __init__(self, master):
        self.master = master

        self.cardFace = Tkinter.StringVar()

        self.frame = Tkinter.Frame(self.master)
        self.frame.pack(fill=Tkinter.BOTH, expand=True)

        self.build_grid()

        self.L1 = Tkinter.Label(self.frame, text="Card Number")
        self.E1 = Tkinter.Entry(self.frame, bd =5)

        self.A1 = Tkinter.Label(self.frame, text=os.listdir(os.getcwd() + "/cards"))
        self.A1.grid(row=3, column=0, sticky='nsew')

        self.L1.grid(row=1, column=0, sticky='ew')
        self.E1.grid(row=1, column=1, sticky='ew')

        self.build_buttons()
        self.build_card()

        self.side = 0
        self.front = ''
        self.back = ''
    #FUNCTIONS
    def build_grid(self):
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=1)

    def build_buttons(self):
        buttons_frame = Tkinter.Frame(self.frame)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.Dbutton = Tkinter.Button(buttons_frame, text="Draw a Card", command=self.on_button)
        self.Fbutton = Tkinter.Button(buttons_frame, text="Flip Card", command=self.flip)

        self.Dbutton.grid(row=0, column=0, sticky='ew')
        self.Fbutton.grid(row=0, column=1, sticky='ew')

    def build_card(self):
        print "Card built"
        self.Card = Tkinter.Label(self.frame, text = self.cardFace.get())
        self.Card.grid(row=2, column=1, sticky='nsew')

    def draw_card(self, int):
        self.side = 0

        cards = os.listdir(os.getcwd() + "/cards")
        curcard = cards[int]
        f = open('cards/'+ curcard, 'r')

        self.front = f.readline().rstrip()
        self.back = f.readline()
        f.close()

        self.cardFace.set(self.front)
        self.build_card()

    def flip(self):

        if self.side == 0:
            print self.back
            self.cardFace.set(self.back)
            self.side = 1
        elif self.side == 1:
            print self.front
            self.cardFace.set(self.front)
            self.side = 0
        self.build_card()

    def on_button(self):

        entry = int(self.E1.get())-1

        self.draw_card(entry)

if __name__ == '__main__':
    root = Tkinter.Tk()
    SampleApp(root)
    root.mainloop()
