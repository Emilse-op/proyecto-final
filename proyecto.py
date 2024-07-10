from tkinter import *
import tkinter as tk
from datetime import datetime, timedelta

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Tecnica Pomodoro")
        self.root.geometry("510x510")
        self.root.resizable(False, False)
        self.create_widgets()
        self.is_running = False
        self.start_time = None
        self.time_left = None

    def create_widgets(self):
        self.root.config(bg="#FFFAF0")
        
        try:
            self.img = tk.PhotoImage(file="tomato.png")
        except tk.TclError as e:
            print(f"Error loading image: {e}")
            self.img = None
        
        if self.img:
            self.lbl_img = tk.Label(self.root, image=self.img, bg="#FFFAF0")
            self.lbl_img.pack(pady=10)             

        self.title_label = tk.Label(self.root, text="TECNICA POMODORO", font=("Helvetica", 20, "bold"), bg="#FFFAF0")
        self.title_label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="25:00", font=("Helvetica", 48), bg="#FFFAF0")
        self.timer_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="#FFFAF0")
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Iniciar", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(self.button_frame, text="Detener", command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(self.button_frame, text="Reiniciar", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.designers_label = tk.Label(self.root, text="Diseñado por Emilse Obando y Julian Quijano", font=("Helvetica", 10), bg="#FFFAF0")
        self.designers_label.pack(pady=10)

        self.is_running = False
        self.is_on_break = False


    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.is_on_break = False
        self.current_time = self.work_time
        self.label.config(text=self.format_time(self.current_time))

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.time_left = timedelta(minutes=25)
            self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.timer_label.config(text="25:00")

    def update_timer(self):
        if self.is_running:
            now = datetime.now()
            elapsed_time = now - self.start_time
            self.time_left = timedelta(minutes=25) - elapsed_time

            minutes, seconds = divmod(self.time_left.seconds, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

            if self.time_left.total_seconds() > 0:
                self.root.after(1000, self.update_timer)
            else:
                self.timer_label.config(text="00:00")
                self.is_running = False               

def start_timer():
    global reps
    reps += 1

if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()