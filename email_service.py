import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()

YOUR_EMAIL = os.getenv("YOUR_EMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def send_email(student, message, report_file):
    subject = f"Student Report - {student['name']}"

    body = f"""Dear {student['name']},

{message}

Student Information:

Student ID: {student['student_id']}
Name: {student['name']}
Email: {student['email']}
Course: {student['course']}
Status: {student['status']}

Please find the attached HTML report for your student information.

Best regards,
Student Data Management System
"""

    try:
        if not YOUR_EMAIL or not GMAIL_APP_PASSWORD:
            raise ValueError("YOUR_EMAIL or GMAIL_APP_PASSWORD is missing from .env")

        email = MIMEMultipart()
        email["From"] = YOUR_EMAIL
        email["To"] = student["email"]
        email["Subject"] = subject
        email.attach(MIMEText(body, "plain"))

        with open(report_file, "rb") as file:
            attachment = MIMEApplication(file.read(), _subtype="html")
            attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=os.path.basename(report_file),
            )
            email.attach(attachment)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(YOUR_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(email)

        print("\n[SUCCESS] Email sent successfully!")
        print(f"[INFO] Recipient: {student['email']}")
        print(f"[INFO] Attachment: {report_file}")
        return True

    except Exception as error:
        print("\n[ERROR] Failed to send email.")
        print(f"[ERROR] {error}")
        return False
