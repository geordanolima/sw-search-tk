
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\.git\Testes\sw-view\assets\result")

def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


class Result():
    def __init__(self, person: dict = {}) -> None:
        self.person = person
    
    def get_screen(self):
        self.window = Tk(className='sw-result')
        self.window.geometry("835x585")
        self.window.configure(bg="#000")
        
        person = self.person.get('name', 'Yoda')
        description = self.person.get('description', 'mester Jedi')
        
        canvas = Canvas(self.window, bg = "#000", height = 585, width = 837, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)
        background = PhotoImage(file=relative_to_assets("background.png"))
        image_1 = canvas.create_image(418.0, 292.0, image=background)
        label_1 = Label(self.window, bd=0, bg="#000",fg="#fff", font='Helvetica 20', text=person)
        label_1.place(x=28.0, y=41.0, width=461.0, height=44.0)
        label_2 = Label(self.window,bd=0, bg="#000", fg="#fff", font='Helvetica 15', text=description)
        label_2.place(x=28.0, y=98.0, width=461.0, height=294.0)
        image_image_2 = PhotoImage(file=relative_to_assets("person.png"))
        image_2 = canvas.create_image(664.0, 217.0, image=image_image_2)
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, 
                          command=lambda: self.window.destroy(), relief="flat", background='#000')
        button_1.place(x=600.0, y=511.0, width=220.0, height=56.0 )
        
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, background='#000')
        button_2.place(x=354.0, y=400.0, width=140.0, height=35.0 )
        
        self.window.resizable(False, False)
        self.window.mainloop()

Result({}).get_screen()