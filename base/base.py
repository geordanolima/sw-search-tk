from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class Search():
    # def __init__(self) -> None:
    #     self.result()
    
    def result(self):
        New_Window = Tk()
        button_1 = Button(New_Window,
            command=lambda: New_Window.destroy(),
            text='close'
        )
        button_1.place(
            x=10.0,
            y=10.0,
            width=100.0,
            height=50.0
        )
        New_Window.mainloop()

