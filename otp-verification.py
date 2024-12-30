import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError

def generate_otp(length=6):
    """Generates a random OTP with the specified length (4 to 8 digits)."""
    if length < 4 or length > 8:
        raise ValueError("OTP length must be between 4 and 8 digits.")
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def send_email(otp, recipient_email):
    """Sends the OTP to the recipient's email address."""
    # Replace with your email credentials
    sender_email = "vedantimahadik2004@gmail.com"
    sender_password = "lsxf slbx zwci cglg"
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

def main():
    try:
        # Input email and validate
        email = input("Enter a valid email address: ").strip()
        validate_email(email)  # Validate email format
        
        # Generate OTP
        otp_length = int(input("Enter the OTP length (4-8): "))
        otp = generate_otp(otp_length)
        
        # Send OTP via email
        send_email(otp, email)
    except EmailNotValidError as e:
        print(f"Invalid email address: {e}")
    except ValueError as e:
        print(f"Error: {e}")

        # Prompt user to enter the OTP
        input_otp = input("Enter the OTP sent to your email: ").strip()
        if input_otp == otp:
            print("OTP verified successfully.")
        else:
            print("Invalid OTP. Verification failed.")
    except EmailNotValidError as e:
        print(f"Invalid email address: {e}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


