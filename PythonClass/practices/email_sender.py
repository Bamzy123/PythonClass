import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")

if not email or not password:
    raise ValueError("EMAIL or APP_PASSWORD not found in environment variables.")

yg = yagmail.SMTP(user=email, password=password)

recipient = "onyinyeekezie2017@gmail.com"
subject = "This message is from pycharm"
content = "ths your bby"

yg.send(to=recipient, subject=subject, contents=content)

print("Email sent successfully!")