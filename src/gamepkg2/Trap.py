import tkinter as tk
import random


class TrapGame:

    def __init__(self, root):

        self.root = root

        self.WIDTH = 800
        self.HEIGHT = 350

        self.LINE_LEFT = 50
        self.LINE_RIGHT = self.WIDTH - 50

        self.BOX_SIZE = 30

        self.score = 0
        self.speed = 6
        self.game_over = False

        self.red_width = 120
        self.MIN_RED_WIDTH = 20

        self.line_y = 180

        root.title("Trap")
        root.geometry("820x430")
        root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="white"
        )
        self.canvas.pack()

        # เส้นดำ
        self.canvas.create_line(
            self.LINE_LEFT,
            self.line_y,
            self.LINE_RIGHT,
            self.line_y,
            fill="black",
            width=6
        )

        # ข้อความ
        self.result_text = self.canvas.create_text(
            self.WIDTH // 2,
            40,
            text="กด SPACE เมื่อกล่องอยู่ในแถบแดง",
            font=("Arial", 18)
        )

        self.score_text = self.canvas.create_text(
            self.WIDTH // 2,
            80,
            text="คะแนน: 0",
            font=("Arial", 16)
        )

        # เป้าแดง
        red_start = random.randint(120, 550)

        self.red_bar = self.canvas.create_rectangle(
            red_start,
            self.line_y - 12,
            red_start + self.red_width,
            self.line_y + 12,
            fill="red",
            outline=""
        )

        # กล่อง
        self.box = self.canvas.create_rectangle(
            self.LINE_LEFT,
            self.line_y - self.BOX_SIZE // 2,
            self.LINE_LEFT + self.BOX_SIZE,
            self.line_y + self.BOX_SIZE // 2,
            fill="blue"
        )

        self.direction = 1

        tk.Button(
            root,
            text="New Game",
            font=("Arial", 12),
            command=self.new_game
        ).pack(pady=10)

        root.bind("<space>", self.hit)

        self.move_box()

    def move_box(self):

        if not self.game_over:

            self.canvas.move(
                self.box,
                self.speed * self.direction,
                0
            )

            x1, y1, x2, y2 = self.canvas.coords(self.box)

            if x1 <= self.LINE_LEFT:
                self.direction = 1

            if x2 >= self.LINE_RIGHT:
                self.direction = -1

        self.root.after(15, self.move_box)

    def new_target(self):

        start = random.randint(100, 600)

        self.canvas.coords(
            self.red_bar,
            start,
            self.line_y - 12,
            start + self.red_width,
            self.line_y + 12
        )

    def hit(self, event=None):

        if self.game_over:
            return

        bx1, by1, bx2, by2 = self.canvas.coords(self.box)
        rx1, ry1, rx2, ry2 = self.canvas.coords(self.red_bar)

        center = (bx1 + bx2) / 2

        if rx1 <= center <= rx2:

            self.score += 1

            self.speed += 0.5

            if self.red_width > self.MIN_RED_WIDTH:
                self.red_width -= 5

            self.canvas.itemconfig(
                self.result_text,
                text="✅ ตรงเป้า!",
                fill="green"
            )

            self.canvas.itemconfig(
                self.score_text,
                text=f"คะแนน: {self.score}"
            )

            self.new_target()

        else:

            self.game_over = True

            self.canvas.itemconfig(
                self.result_text,
                text=f"💀 GAME OVER | คะแนน {self.score}",
                fill="red"
            )

    def new_game(self):

        self.score = 0
        self.speed = 6
        self.red_width = 120
        self.game_over = False
        self.direction = 1

        self.canvas.coords(
            self.box,
            self.LINE_LEFT,
            self.line_y - self.BOX_SIZE // 2,
            self.LINE_LEFT + self.BOX_SIZE,
            self.line_y + self.BOX_SIZE // 2
        )

        self.canvas.itemconfig(
            self.score_text,
            text="คะแนน: 0"
        )

        self.canvas.itemconfig(
            self.result_text,
            text="กด SPACE เมื่อกล่องอยู่ในแถบแดง",
            fill="black"
        )

        self.new_target()


def main2():
    root = tk.Tk()
    TrapGame(root)
    root.mainloop()


if __name__ == "__main__":
    main2()