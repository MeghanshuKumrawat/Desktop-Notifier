# import libraries
from tkinter import *
from tkinter import ttk, messagebox
from plyer import notification
import datetime
# create a class
class Notifier():
    def __init__(self, root):
        self.root = root
        self.root.title("Prersonal Notifier")
        self.root.geometry("390x160")
        # variables
        self.hour = StringVar()
        self.min = StringVar()
        self.title = StringVar()
        self.msg = StringVar()
        # Header Text
        Label_alarm_header = Label(root, font=("arial", 15, "underline"), text="Set time").place(x=10, y=10)
        Label_msg_header = Label(root, font=("arial", 15, "underline"), text="Add message").place(x=180, y=10)
        # Label and Entry for User Input
        Label_hour = Label(root, text="Hours :").place(x=10, y=40)
        Entry_hour = ttk.Combobox(root, state="readonly", width=5, textvariable=self.hour)
        hour = []
        for y in range(1, 25):
            hour.append(y)
        Entry_hour["values"] = hour
        Entry_hour.place(x=80, y=40)

        Label_min = Label(root, text="Minutes :").place(x=10, y=70)
        Entry_min = ttk.Combobox(root, state="readonly", width=5, textvariable=self.min)
        min = []
        for x in range(0, 61):
            min.append(x)
        Entry_min["values"] = min
        Entry_min.place(x=80, y=70)

        Label_title = Label(root, text="Title :").place(x=180, y=40)
        Entry_title = Entry(root, textvariable=self.title).place(x=250, y=40)

        Label_msg = Label(root, text="Message :").place(x=180, y=70)
        Entry_msg = Entry(root, textvariable=self.msg).place(x=250, y=70)
        # Button To start the process
        Notify_me_btn = Button(root, text="Notify me",width=51, bg="#3390FF", activebackground="light blue",
                             activeforeground="white", fg="White", command=self.alarm).place(x=10, y=110)
        # Show starting Information
        messagebox.showinfo("Information", "Use 24-hour format to set an alarm!!!")

    def message(self, title, msg):
        '''Function For display notification'''
        notification.notify(
            title=title,
            message=msg,
            timeout=10)

    def alarm(self):
        '''Main Function'''
        while TRUE:
            # Set validation
            if self.hour.get() == "" or self.min.get() == "" or self.title.get()=="" or self.msg.get()=="":
                messagebox.showwarning("Warning", "All feilds are required")
                break
            else:
                # Chack Condition
                if self.hour.get() == datetime.datetime.now().strftime("%H") and \
                        self.min.get() == datetime.datetime.now().strftime("%M"):
                    self.message(self.title.get(),self.msg.get())
                    break
# Create Objects
root = Tk()
obj = Notifier(root)
# Main loop
root.mainloop()