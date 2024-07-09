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

    def update_timer(self):
        if self.is_running:
            if self.current_time > 0:
                self.current_time -= 1
                self.label.config(text=self.format_time(self.current_time))
                self.root.after(1000, self.update_timer)
            else:
                if not self.is_on_break:
                    self.current_time = self.break_time
                    self.is_on_break = True
                    self.label.config(text="Break Time!")
                else:
                    self.current_time = self.work_time
                    self.is_on_break = False
                self.update_timer()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()