
import random
from tkinter import Tk, Canvas, Label, Entry, Button, StringVar, OptionMenu, messagebox



class SudokuGame:
    def __init__(self, root, difficulty, user):
        self.root = root
        self.root.title(user)
        self.canvas = Canvas(self.root, width=450, height=450)
        self.canvas.pack()
        self.difficulty = difficulty
        self.board = [[0]*9 for _ in range(9)]
        self.selected_cell = None
        self.create_initial_numbers()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)
        self.delay = 500  

    def create_initial_numbers(self):
        if self.difficulty == "Easy":
            numbers_to_place = 20
        elif self.difficulty == "Medium":
            numbers_to_place = 30
        elif self.difficulty == "Hard":
            numbers_to_place = 40
        else:
            numbers_to_place = 20 
        for _ in range(numbers_to_place):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            if self.is_safe(row, col, num):
                self.board[row][col] = num

    def is_safe(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[box_start_row + i][box_start_col + j] == num:
                    return False
        return True

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(9):
            self.canvas.create_rectangle(150*(i%3),150*(i//3), 150+150*(i%3), 150+150*(i//3),width=3)
            for j in range(9):
                x1, y1 = i * 50, j * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2)
                if self.board[i][j] != 0:
                    self.canvas.create_text(x1 + 25, y1 + 25, text=str(self.board[i][j]), font=("Arial", 24))

    def cell_clicked(self, event):
        row, col = event.y // 50, event.x // 50
        if self.board[row][col] == 0:
            self.selected_cell = (row, col)
            self.canvas.focus_set()
        else:
            self.selected_cell = None
        print(row, col)

    def key_pressed(self, event):
        if event.keysym == "space":
            if self.solve_sudoku_step_by_step():
                self.draw_board()
            else:
                messagebox.showwarning("Unsolvable", "The Sudoku puzzle cannot be solved.")
        elif self.selected_cell and event.char in "123456789":
            col, row = self.selected_cell
            num = int(event.char)
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                self.selected_cell = None
                self.draw_board()
            else:
                messagebox.showwarning("Invalid Move", f"The number {num} cannot be placed at row {row+1}, column {col+1}.")
        elif self.selected_cell and not event.char in "123456789":
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 9.")
        

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve_sudoku_step_by_step(self):
        self.solved = False
        self.solving_process = True
        self.solve_step()
        return self.solved

    def solve_step(self):
        if not self.solving_process:
            return

        if self.solved:
            return

        empty_cell = self.find_empty_cell()
        if not empty_cell:
            self.solved = True
            return 

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                self.draw_board()
                self.root.update() 
                self.root.after(self.delay)

                if self.solve_step():
                    return True

                self.board[row][col] = 0  
                self.draw_board()
                self.root.update()  
                self.root.after(self.delay)  

        self.solving_process = False  
        return False  




