import smtplib
from email.message import EmailMessage

def send_email_report(receiver_email, file_path=None):
    """
    Sends a simple email notification to the user, optionally with an attachment.

    Args:
        receiver_email (str): The email address of the recipient.
        file_path (str, optional): The path to a file to attach to the email. Defaults to None.
    
    Replace `sender_email` and `app_password` with your own credentials.
    For `app_password`, you'll need to generate an App Password for your Google account.
    See: https://support.google.com/accounts/answer/185833
    """

    # IMPORTANT: Replace these with your actual email and generated app password
    sender_email = "your_email@gmail.com"
    app_password = "your_16_character_app_password"

    msg = EmailMessage()

    msg["Subject"] = "Expense Tracker Monthly Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        """
Hello,

Your monthly expense report has been generated.

YouYou can also export the CSV report and view charts from the Expense Tracker application.

Thank you for using Expense Tracker.
        """
    )

    if file_path:
        try:
            with open(file_path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_path.split('/')[-1] # Extracts filename from path
                )
            print(f"Attached {file_path} to the email.")
        except FileNotFoundError:
            print(f"Error: Attachment file not found at {file_path}.")
        except Exception as e:
            print(f"Error attaching file {file_path}: {e}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        print("Email sent successfully.")

    except Exception as e:
        print("Failed to send email.")
        print("Error:", e)
        print("Please ensure your sender_email and app_password are correct and that you have enabled App Passwords for your Google account.")
