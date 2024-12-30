import random
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp(length=6):
    """Generates a random OTP with the specified length (4 to 8 digits)."""
    if length < 4 or length > 8:
        raise ValueError("OTP length must be between 4 and 8 digits.")
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def send_email(otp, recipient_email):
    """Sends the OTP to the recipient's email address."""
    # Replace with your email credentials
    sender_email = "sagurbhai420@gmail.com"
    sender_password = "mffu cjyk kvgp nywf"
    smtp_server = "smtp.gmail.com"  # Adjust for your email provider
    smtp_port = 587
    
    # Compose the email
    subject = "Your One-Time Password (OTP)"
    body = f"Your one-time password (OTP) is: {otp}"
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Encrypt the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"OTP sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def is_valid_email(email):
    """Validate email using regex."""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

def main():
    try:
        # Input email and validate
        email = input("Enter a valid email address: ").strip()
        if not is_valid_email(email):
            print(f"Invalid email address format: {email}")
            return
        
        # Prompt until valid OTP length is entered
        while True:
            try:
                otp_length = int(input("Enter the OTP length (4-8): "))
                otp = generate_otp(otp_length)
                break  # Exit the loop if OTP is generated successfully
            except ValueError as e:
                print(e)  # Print the error if OTP length is invalid
                continue  # Prompt the user to enter a valid OTP length

        # Send OTP via email
        send_email(otp, email)

        # Prompt user to enter OTP for verification
        input_otp = input("Enter the OTP sent to your email: ").strip()
        if input_otp == otp:
            print("OTP verified successfully.")
        else:
            print("Invalid OTP. Verification failed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Correct the typo here: use __name__ instead of _name_
if __name__ == "__main__":
    main()
