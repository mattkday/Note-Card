import os
import Tkinter as tk
from Tkinter import*

class SampleApp(tk.Tk):
    
    wuc = "H"
    side = 0
    front = ''
    back = ''
    print "Welcome to the index card application!\n To see the available cards, enter 'aCards()'.\n To select a card, enter 'draw_card()' with the number of the card between the parentheses.\n To flip the card, enter 'flip()'. "

    def draw_card(self, int):
        global wuc
        global front
        global back
        global side
        
        side = 0

        cards = os.listdir(os.getcwd() + "/cards")
        curcard = cards[int]
        f = open('cards/'+ curcard, 'r')
        


        front = f.readline()
        back = f.readline()
        f.close()

        wuc = front
        print front

    def flip(self):
        global wuc
        global side
        global front
        global back
        
        if side == 0:
            print back
            wuc = back
            side = 1
        elif side == 1:
            print front
            wuc = front
            side = 0

    def aCards(ex):
        print os.listdir(os.getcwd() + "/cards")

        
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        
        cardFace = StringVar()
        cardFace.set(self.wuc)
        
        self.frame = Frame(self )
        self.frame.pack()

        self.cframe = Frame(self, height = 100)
        self.cframe.pack()

        
        self.L1 = Label(self.frame, text="Card Number")
        self.E1 = Entry(self.frame, bd =5)
        self.Dbutton = Button(self.frame, text ="Draw a Card", command = self.on_button)
        self.Fbutton = Button(self.frame, text ="Flip Card", command = self.flip)
        self.Abutton = Button(self.frame, text ="Available Card", command = self.aCards)


        self.Card = Label(self.cframe, textvariable = cardFace)

        self.Abutton.pack(side = LEFT)
        self.Dbutton.pack(side = LEFT)
        self.Fbutton.pack(side = LEFT)
        self.E1.pack(side = RIGHT)
        self.L1.pack(side = RIGHT)
        

        self.Card.pack(side = BOTTOM)

    

    def on_button(self):
        
        entry = int(self.E1.get())-1
        
        self.draw_card(entry)

app = SampleApp()
app.mainloop()


    
