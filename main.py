from report_generator import generate_html_report
from email_service import send_mail

def main():

    print("=" * 50)
    print("     STUDENT EMAIL AUTOMATION SYSTEM")
    print("=" * 50)

    # Student information
    print("\nEnter Student Information")

    student_id = input("Student ID: ")
    name = input("Student Name: ")
    email = input("Student Email: ")
    course = input("Course: ")
    status = input("Status: ")

    # Custom message
    print("\nEnter Email Message")
    message = input("Message: ")

    # Store student data
    student = {
        "student_id": student_id,
        "name": name,
        "email": email,
        "course": course,
        "status": status
    }

    print("\n[1/3] Generating HTML report...")

    # Generate HTML report
    report_file = generate_html_report(student)

    print(f"[SUCCESS] Report created: {report_file}")

    print("\n[2/3] Preparing email...")

    # Send email
    print("[3/3] Sending email...")

    send_mail(
        student,
        message,
        report_file
    )


if __name__ == "__main__":
    main()