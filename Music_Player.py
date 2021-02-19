from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from playsound import playsound
import pygame
from pydub import AudioSegment
from pydub.playback import play


pygame.init()
pygame.mixer.init()


file = None

def add():
    global file
    file = askopenfilename(defaultextension=".mp3", filetypes=[("Music", "*.mp3")])
    if file != "":
        lst.insert(END, os.path.basename(file))

def dele():
    select = lst.curselection()
    lst.delete(select)


def ply():
    global file
    if file != None:
        while TRUE:
            a = lst.curselection()
            pygame.mixer.music.load(os.path.join(str(a), file))
            pygame.mixer.music.play()


def prv():
    sel = lst.curselection()
    b = lst.index(sel)
    d = b-1
    pygame.mixer.music.load(os.path.join(str(d), file))
    pygame.mixer.music.play()


def nxt():
    sel = lst.curselection()
    x = lst.index(sel)
    y = x+1
    pygame.mixer.music.load(os.path.join(str(y), file))
    pygame.mixer.music.play()

def vlmn():
    select = lst.curselection()
    song = AudioSegment.from_mp3(select)
    a = sc.get()
    if a == 6:
        song = song + 2
    elif a == 8:
        song = song + 4
    elif a == 10:
        song = song + 6
    elif a == 2:
        song = song - 2


root = Tk()
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)
root.title("mp3_Player")
root.iconphoto(False, PhotoImage(file='mu.png'))
root.configure(background = "black")

Label(root, text="Song's List", fg="white", bg="black", padx=15, pady=5, font=(None,12,"bold")).pack(anchor="nw")

#scrl = Scrollbar(root)
#scrl.pack(side=RIGHT, fill=Y)

lst = Listbox(root, bg="white", borderwidth=3)#, yscrollcommand=scrl.set)
lst.pack(padx=15, fill=X)
#scrl.config(command=lst.yview)

f1 = Frame(root, borderwidth=5,padx=15, pady=7, bg="black")
Button(f1, fg="black", bg="grey", borderwidth=3, text="ADD", font=(None,12,"bold"), command=add).pack(side=LEFT)
Button(f1, fg="black", bg="grey", borderwidth=3, text="DEL", font=(None,12,"bold"), command=dele).pack(side=RIGHT)
f1.pack(fill=X)


f2 = Frame(root, borderwidth=5,padx=95, pady=28, bg="black")
Button(f2, fg="black", bg="grey", borderwidth=3, padx=30, text="PREV", font=(None,10,"bold"), command=prv).pack(side=LEFT)
Button(f2, fg="black", bg="grey", borderwidth=3, padx=30, text="PLAY", font=(None,10,"bold"), command=ply).pack(side=LEFT)
Button(f2, fg="black", bg="grey", borderwidth=3, padx=30, text="NEXT", font=(None,10,"bold"), command=nxt).pack(side=LEFT)
f2.pack(fill=X)


sc = Scale(root, from_=0, to=10, orient=HORIZONTAL, bg="black", tickinterval=2, command=vlmn)
#sc.set(4)
sc.pack()

Label(root, text="Volume", bg="black", fg="white", font=(None,10,"bold")).pack()


Label(root, text="!! Listen only your favorite songs !!", fg="black",bg="grey", font=(None,12,"bold")).pack(fill=X, padx=15, pady=5, side=BOTTOM)


root.mainloop()