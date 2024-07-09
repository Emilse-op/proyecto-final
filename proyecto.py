import tkinter as tk
import time
class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.current_time = self.work_time

        self.is_running = False
        self.is_on_break = False

        self.label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT)
