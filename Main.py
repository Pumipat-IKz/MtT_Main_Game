import tkinter as tk



from src.gamepkg1 import Wordle
from src.gamepkg2 import Trap




def open_wordle():
    root.destroy()
    Wordle.main1()




def open_trap():
    root.destroy()
    Trap.main2()




root = tk.Tk()



root.title("Game Center")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#20232A")



title = tk.Label(
    root,
    text="🎮 GAME CENTER",
    font=("Arial", 28, "bold"),
    bg="#20232A",
    fg="white"
)
title.pack(pady=40)



subtitle = tk.Label(
    root,
    text="เลือกเกมที่ต้องการเล่น",
    font=("Arial", 14),
    bg="#20232A",
    fg="lightgray"
)
subtitle.pack(pady=10)



wordle_btn = tk.Button(
    root,
    text="📝 WORDLE",
    font=("Arial", 18, "bold"),
    width=20,
    height=2,
    bg="#4CAF50",
    fg="white",
    command=open_wordle
)
wordle_btn.pack(pady=20)



trap_btn = tk.Button(
    root,
    text="⚠ TRAP",
    font=("Arial", 18, "bold"),
    width=20,
    height=2,
    bg="#E53935",
    fg="white",
    command=open_trap
)
trap_btn.pack(pady=20)



footer = tk.Label(
    root,
    text="Version 1.0",
    font=("Arial", 10),
    bg="#20232A",
    fg="gray"
)
footer.pack(side="bottom", pady=15)



root.mainloop()
