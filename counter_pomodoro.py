import threading
import time
import tkinter as tk


def start_thread(self):
    t = threading.Thread(target=self.start)
    t.start()

def start(self):
    self.stop_loop = False
    minutes, seconds = 0,5 # For Long Break, Short Break and Working time I can add conditions

    full_seconds = minutes*60 + seconds

    while full_seconds >0 and not self.stop_loop:
        full_seconds -= 1

        minutes, seconds = divmod(full_seconds, 60)
        self.time_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
        self.root.update()
        time.sleep(1)

    #Short term counting
    isDone = False
    count = 0
    while not isDone:
        count+=1
        if count==2:
            isDone=True

        if not self.stop_loop:
            self.stop_loop = False
            minutes, seconds = 0, 5  # For Long Break, Short Break and Working time I can add conditions

            full_seconds = minutes * 60 + seconds
            self.label1.config(text=f"{Text2}")
            self.root.update()
            time.sleep(1)
            if count==2:
                self.label1.config(text=f"{Text3}")
                self.root.update()

            while full_seconds > 0 and not self.stop_loop:

                full_seconds -= 1

                minutes, seconds = divmod(full_seconds, 60)
                self.time_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)



def reset(self):
    self.stop_loop = True
    self.time_label.config(text="Time:00:00")

def stop(self):
    self.stop_loop = True
    self.root.update()
    pass

CountdownTimer()