from tkinter import *
from tkinter import messagebox
import smtplib

f = Tk()
f.title("Mail UI")
f.geometry("500x280")
f.configure(background="gainsboro")

p1 = PhotoImage(file=r"C:/Users/dell/OneDrive/Desktop/Python project/MailGUI/Mail.png")
f.iconphoto(False, p1)

send_email = StringVar()
send_pass = StringVar()
recv_email = StringVar()
msg_body = None


def layout():
    menuBar = Menu(f)
    menuBar.add_command(label="Instructions", command=instruct)
    menuBar.add_command(label="About", command=about)
    f.config(menu=menuBar)

    sender_email = Label(f, text="Sender’s Gmail ID: ")
    sender_entry = Entry(f, textvariable=send_email, bd=5, width=50)
    sender_pass = Label(f, text="Sender’s Gmail Pass: ")
    sender_passentry = Entry(f, show="*", textvariable=send_pass, bd=5, width=50)

    receiver_email = Label(f, text="Receiver’s Email: ")
    receiver_entry = Entry(f, textvariable=recv_email, bd=5, width=50)

    msg_label = Label(f, text="Message")
    global msg_body
    msg_body = Text(f, height=5, width=38, bd=5)

    send = Button(f, text="Send", width=8, command=mail, bd=5)
    cancel = Button(f, text="Cancel", width=8, command=destroy, bd=5)

    sender_email.grid(row=0, column=0, padx=5, pady=3)
    sender_entry.grid(row=0, column=1, padx=5, pady=3)
    sender_pass.grid(row=1, column=0, padx=5, pady=3)
    sender_passentry.grid(row=1, column=1, padx=5, pady=3)
    receiver_email.grid(row=2, column=0, padx=5, pady=3)
    receiver_entry.grid(row=2, column=1, padx=5, pady=3)
    msg_label.grid(row=3, column=0, padx=5, pady=3)
    msg_body.grid(row=3, column=1, padx=5, pady=3)
    send.grid(row=4, column=0, padx=5, pady=3)
    cancel.grid(row=4, column=1, padx=5, pady=3)
    f.mainloop()


def destroy():
    f.destroy()

def msg_box():
    messagebox.showinfo("Email Info", "Mail Sent")


def instruct():
    messagebox.showinfo(
        "Instruction",
        "switch ‘allow less secure apps’ to ON from \n https://myaccount.google.com/u/0/security?hl=en&pli=1#connectedapps\nbefore using the app!!",
    )


def about():
    messagebox.showinfo(
        "About",
        "This app is for only educational purpose \nCreated by Zeeshaan Siddique\nNon-Copywrite",
    )


def mail():
    try:
        if send_email.get() == "" or send_pass.get() == "" or recv_email.get() == "":
            messagebox.showerror("Error", "Please enter the complete details.")
        else:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            a = send_email.get()
            b = send_pass.get()
            c = msg_body.get("1.0", END)
            d = recv_email.get()
            server.login(a, b)
            server.sendmail(a, d, c)
            server.close()
            msg_box()

    except Exception as e:
        print(e)
        a = messagebox.askokcancel("Error", "Read instructions")


layout()
