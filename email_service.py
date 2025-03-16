import smtplib
from email.message import EmailMessage

def send_email(email, order_id, cart):
    msg = EmailMessage()
    msg['Subject'] = f"Order Confirmation - {order_id}"
    msg['From'] = "yourstore@example.com"
    msg['To'] = email

    cart_details = "\n".join([f"{item['name']} - ${item['price']} x {item['quantity']}" for item in cart])
    msg.set_content(f"Thank you for your order!\n\nOrder ID: {order_id}\n\nItems:\n{cart_details}")

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email", "your_password")
        server.send_message(msg)
