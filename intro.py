import random
from tkinter import Tk, Canvas, Label, Entry, Button, StringVar, OptionMenu, messagebox
from app import *
from score import *


class IntroWindow:
    def __init__(self, root):
        self.root = root
        self.instance_score = Score()
        self.root.title("Sudoku Game")
        root.geometry("450x450")
        self.username = StringVar()
        self.difficulty = StringVar()
        self.difficulty.set("Easy")

        self.create_intro_window()

    def create_intro_window(self):
        
        scores = self.instance_score.return_scores() 
        # print(scores)

        Button(self.root, text="Start Game", border=3,font = 5,activebackground="black",padx=20, pady=10, activeforeground="white", command=self.start_game).pack(pady=20)
        Label(self.root, text="Enter your username:", font=5).pack(pady=10)
        Entry(self.root, textvariable=self.username, width=30).pack(pady=5)
        
        Label(self.root, text="Select difficulty level:").pack(pady=10)
        difficulties = ["Easy", "Medium", "Hard"]
        OptionMenu(self.root, self.difficulty, *difficulties).pack(pady=10)
        
        Label(self.root, text="HIGHEST SOCRES", font=5).pack(pady=10)

        for i in scores:
            Label(self.root, text=f"{i[0]}  {i[1]}").pack(pady=2)
            
        

    def start_game(self):
        user_name = self.username.get()
        level = self.difficulty.get()

        if not user_name:
            messagebox.showwarning("Input Error", "Please enter a username.")
            return
        

        self.root.destroy()
        
        main_window = Tk()
        SudokuGame(main_window, level, user_name)
        main_window.mainloop()