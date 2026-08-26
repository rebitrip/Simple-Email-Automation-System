from report_generator import generate_html_report
from email_service import send_email


def main():
    print("=" * 50)
    print("     STUDENT EMAIL AUTOMATION SYSTEM")
    print("=" * 50)

    print("\nEnter Student Information")
    student = {
        "student_id": input("Student ID: ").strip(),
        "name": input("Student Name: ").strip(),
        "email": input("Student Email: ").strip(),
        "course": input("Course: ").strip(),
        "status": input("Status: ").strip(),
    }

    print("\nEnter Email Message")
    message = input("Message: ").strip()

    print("\n[1/3] Generating HTML report...")
    report_file = generate_html_report(student)
    print(f"[SUCCESS] Report created: {report_file}")

    print("\n[2/3] Preparing email...")
    print("[3/3] Sending email...")

    send_email(student, message, report_file)


if __name__ == "__main__":
    main()
