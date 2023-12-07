#import time
#time.sleep (6)

import tkinter as tk
from ctypes import windll
import subprocess
import sys
windll.shcore.SetProcessDpiAwareness(1)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

root = tk.Tk()
root.withdraw()
root.wm_attributes("-topmost", True)
root.update()

class CustomErrorDialog(tk.Toplevel):
    def __init__(self, message1, message2, width_percent, height_percent, button1_text, button2_text):
        parent = root
        super().__init__(parent)

        global screen_width
        global screen_height

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        box_width = int(screen_width * width_percent)
        box_height = int(screen_height * height_percent)

        self.overrideredirect(True)
        self.geometry(f"{box_width}x{box_height}+{int((screen_width - box_width) / 2)}+{int((screen_height - box_height) / 2)}")
        self.configure(bg='#0067b1')  # Set background color to blue

        label1 = tk.Label(self, text=message1, bg='#0067b1', fg='white', font=('Segoe UI', 29))
        label1.place(x=38, y=29)

        label2 = tk.Label(self, text=message2, bg='#0067b1', fg='white', font=('Segoe UI', 17))
        label2.place(x=48, y=130)

        additional_text = tk.Label(self, text="Don't remind me again", bg='#0067b1', fg='#70befa', font=('Segoe UI', 17), cursor='hand2')
        additional_text.place(x=48, y=200)
        additional_text.bind("<Button-1>", self.on_additional_text_click)

        self.create_double_box(button1_text, button2_text)

    def on_additional_text_click(self, event):
        #print("Additional text clicked!")
        pass

    def create_double_box(self, button1_text, button2_text):
        button_1 = tk.Label(self, text="Manage storage", fg='white', bg="#0067b1", width=15, height=1, font=('Segoe UI', 20, 'bold'))
        button_1.pack_propagate(False)
        button_1.config(highlightbackground="white", highlightthickness=3)
        button_1.place(x=screen_width/2.2, y=380)
        button_1.bind("<Enter>", lambda event: button_1.config(bg='#0076d6', fg='white'))
        button_1.bind("<Leave>", lambda event: button_1.config(bg="#0067b1", fg='white'))
        button_1.bind("<Button-1>", lambda e: self.on_button1_click("Label 1"))

        button_2 = tk.Label(self, text="Close", fg='white', bg="#0067b1", width=8, height=1, font=('Segoe UI', 20, 'bold'))
        button_2.pack_propagate(False)
        button_2.config(highlightbackground="white", highlightthickness=3)
        button_2.place(x=screen_width/1.55, y=380)
        button_2.bind("<Enter>", lambda event: button_2.config(bg='#0076d6', fg='white'))
        button_2.bind("<Leave>", lambda event: button_2.config(bg="#0067b1", fg='white'))
        button_2.bind("<Button-1>", lambda f: root.destroy ())

    def on_button1_click(self, button_text):
        #print(f"Button 1 clicked! Text: {button_text}")
        import os
        os.system ("start ms-settings:storagesense")
        self.destroy ()
        #sys.path.insert (0, r'C:\Users\Public\Loki')
        import error2
        error2.show ()

    def on_button2_click(self, button_text):
        #print(f"Button 2 clicked! Text: {button_text}")
        pass


width_percent = 0.77
height_percent = 0.324
button1_text = "Button 1"
button2_text = "Button 2"

CustomErrorDialog("Low disk space", "You're running out of space on this PC. Manage storage to view usage and free up some space.", width_percent, height_percent, button1_text, button2_text)

root.mainloop()
