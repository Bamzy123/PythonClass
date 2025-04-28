import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")

if not email or not password:
    raise ValueError("EMAIL or APP_PASSWORD not found in environment variables.")

yg = yagmail.SMTP(user=email, password=password)

recipient = "ayoomotoso@gmail.com"
subject = "This message is from your son"
content = """
           Dad just upgraded my python skill, i can send emails without opening my gmail, very interesting
           this message you are seeing now is done from my coding app, I'll call chat you when it's closing time.
           """

yg.send(to=recipient, subject=subject, contents=content)

print("Email sent successfully!!!")