import os
import smtplib
from email.mime.text import MIMEText

def send_email_alert(product_name, price, url):
    msg = MIMEText(f"The price of {product_name} has changed to {price}. Check it out: {url}")
    msg["Subject"] = "Price Change Alert!"
    msg["From"] = os.environ.get("EMAIL_USER")
    msg["To"] = os.environ.get("EMAIL_TO")

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your-email@example.com", "your-password")
        server.send_message(msg)