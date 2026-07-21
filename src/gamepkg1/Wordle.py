import tkinter as tk
from tkinter import messagebox
import random

WORDS = [
    "APPLE", "GRAPE", "HOUSE", "MOUSE", "PLANT",
    "TRAIN", "LIGHT", "SMILE", "BRICK", "CLOUD",
    "WATER", "SHEEP", "TABLE", "CHAIR", "PIZZA",
    "SNAKE", "BREAD", "HEART", "FRUIT", "CANDY",
    "PHONE", "GHOST", "STONE", "NURSE", "TIGER"
]


class WordleGame:

    def __init__(self, root):
        self.root = root

        root.title("Wordle")
        root.geometry("630x930")
        root.resizable(False, False)

        self.answer = random.choice(WORDS)

        self.current_row = 0
        self.current_col = 0
        self.current_word = ""

        self.boxes = []

        tk.Label(
            root,
            text="WORDLE",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        board = tk.Frame(root)
        board.pack(pady=10)

        for r in range(6):
            row = []

            for c in range(5):
                lbl = tk.Label(
                    board,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 26, "bold"),
                    relief="solid",
                    bg="white"
                )

                lbl.grid(
                    row=r,
                    column=c,
                    padx=8,
                    pady=8
                )

                row.append(lbl)

            self.boxes.append(row)

        bf = tk.Frame(root)
        bf.pack(side="bottom", pady=40)

        tk.Button(
            bf,
            text="New Game",
            font=("Arial", 14, "bold"),
            width=12,
            height=2,
            command=self.new_game
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            bf,
            text="Reset",
            font=("Arial", 14, "bold"),
            width=12,
            height=2,
            command=self.reset_board
        ).grid(row=0, column=1, padx=10)

        root.bind("<Key>", self.key_pressed)
        root.focus_force()

    def key_pressed(self, event):

        k = event.keysym

        if k == "BackSpace":

            if self.current_col > 0:

                self.current_col -= 1
                self.current_word = self.current_word[:-1]

                self.boxes[self.current_row][self.current_col]["text"] = ""

            return

        if k == "Return":

            if len(self.current_word) == 5:
                self.check_word()

            return

        if (
            len(event.char) == 1
            and event.char.isalpha()
            and self.current_col < 5
        ):

            ch = event.char.upper()

            self.current_word += ch

            self.boxes[self.current_row][self.current_col]["text"] = ch

            self.current_col += 1

    def check_word(self):

        guess = self.current_word

        answer_copy = list(self.answer)
        colors = ["gray"] * 5

        # ตัวอักษรถูกตำแหน่ง
        for i in range(5):

            if guess[i] == self.answer[i]:
                colors[i] = "green"
                answer_copy[i] = None

        # มีตัวอักษรอยู่ในคำแต่ตำแหน่งผิด
        for i in range(5):

            if colors[i] == "green":
                continue

            if guess[i] in answer_copy:

                colors[i] = "gold"
                answer_copy[answer_copy.index(guess[i])] = None

        for i, color in enumerate(colors):

            self.boxes[self.current_row][i].config(
                bg=color,
                fg="white"
            )

        if guess == self.answer:

            messagebox.showinfo(
                "Winner!",
                "Congratulations!"
            )

            self.root.unbind("<Key>")
            return

        self.current_row += 1
        self.current_col = 0
        self.current_word = ""

        if self.current_row >= 6:

            messagebox.showinfo(
                "Game Over",
                f"The word was {self.answer}"
            )

            self.root.unbind("<Key>")

    def reset_board(self):

        self.current_row = 0
        self.current_col = 0
        self.current_word = ""

        for row in self.boxes:

            for box in row:

                box.config(
                    text="",
                    bg="white",
                    fg="black"
                )

        self.root.bind("<Key>", self.key_pressed)
        self.root.focus_force()

    def new_game(self):

        self.answer = random.choice(WORDS)
        self.reset_board()


def main1():

    root = tk.Tk()
    WordleGame(root)
    root.mainloop()


if __name__ == "__main__":
    main1()