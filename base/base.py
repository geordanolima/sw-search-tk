from translate_shell.translate import translate
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class Search():
    # def __init__(self) -> None:
    #     self.result()
    
    def get_person(self, value):
        return {
            'name': 'Darth Vader',
            'description': 'lord sith'
        }
    
    def screen(self):
        pass


class Translate():
    def __init__(self) -> None:
        self.to_lng = 'pt_br'
    
    def get_translated_text(self, text: str) -> str:
        try:
            return translate(text, self.to_lng)
        except Exception:
            return None


Search().screen()