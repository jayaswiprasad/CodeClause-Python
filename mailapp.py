import tkinter as tk
import smtplib

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("Mail Application")

        self.to_label = tk.Label(master, text="To:")
        self.to_label.pack()
        self.to_entry = tk.Entry(master)
        self.to_entry.pack()

        self.subject_label = tk.Label(master, text="Subject:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(master)
        self.subject_entry.pack()

        self.body_label = tk.Label(master, text="Body:")
        self.body_label.pack()
        self.body_entry = tk.Text(master)
        self.body_entry.pack()

        self.send_button = tk.Button(master, text="Send", command=self.send_mail)
        self.send_button.pack()

    def send_mail(self):
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        body = self.body_entry.get("1.0", "end-1c")

        # Replace with your own email and password
        email = "your_email_address@gmail.com"
        password = "your_email_password"

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, password)
            server.sendmail(email, to_address, message)

        self.to_entry.delete(0, "end")
        self.subject_entry.delete(0, "end")
        self.body_entry.delete("1.0", "end")

root = tk.Tk()
app = MailApp(root)
root.mainloop()
