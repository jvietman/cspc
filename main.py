from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as scrolledtext
import os

from lib import *

root = Tk()
root.title("csgo prefire creator")
root.geometry("800x600")

name = Entry(root, font=("", 15))
name.place(anchor=NW, relx=0.1, rely=0.1)
name.insert(0, "Name")
path = Entry(root, width=50)
path.place(anchor=NW, relx=0.1, rely=0.15)
path.insert(0, os.getcwd())
way = Entry(root, width=50)
way.place(anchor=NW, relx=0.05, rely=0.25)
way.insert(0, "a > b > c")

# settings
weapons = {
    "AK47": "weapon_ak47",
    "M4A1-S": "weapon_m4a1_silencer",
    "UPS-S": "weapon_usp_silencer",
    "GLOCK": "weapon_glock",
    "DESERT EAGLE": "weapon_deagle"
}
infiniteammo = IntVar(value=1)
weapon = StringVar(value="AK47")
Checkbutton(root, text="Infinite ammo", variable=infiniteammo).place(anchor=NW, relx=0.7, rely=0.1)
weaponbox = ttk.Combobox(root, textvariable=weapon)
weaponbox['values'] = list(weapons.keys())
weaponbox['state'] = 'readonly'
weaponbox.place(anchor=NW, relx=0.7, rely=0.15)

txt = scrolledtext.ScrolledText(root, undo=True)
txt.place(anchor=CENTER, relx=0.5, rely=0.6, relwidth=0.9, relheight=0.6)

def build():
    buildconfig(way.get(), extractpositions(txt.get("1.0", END)), name.get(), path.get(), bool(infiniteammo.get()), weapons[weapon.get()])
    messagebox.showinfo(title="csgo prefire creator", message=name.get()+".cfg has been built!")

buildbtn = Button(root, text="Build", font=("", 15), width=10, command=build)
buildbtn.place(anchor=W, relx=0.05, rely=0.95)

root.mainloop()