import tkinter as tk
from tkinter import messagebox
 
 
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
 
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
 
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text="", font=("Arial", 30), width=5, height=2,
                               command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
 
        reset_button = tk.Button(master, text="Reset", font=("Arial", 12), command=self.reset)
        reset_button.grid(row=3, column=1, pady=10)
 
    def click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
 
    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False
 
    def reset(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text="")
        messagebox.showinfo("Tic Tac Toe", "Game reset")
 
 
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()