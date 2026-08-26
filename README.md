# 📧 Student Data & Email Automation System

> A Python-based automation system that sends personalized student emails with student information and a dynamically generated HTML report attached.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SMTP](https://img.shields.io/badge/Email-Gmail%20SMTP-red?logo=gmail)
![HTML](https://img.shields.io/badge/Report-HTML-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

**Student Data & Email Automation System** is a lightweight Python command-line application designed to automate the process of sending personalized student emails.

Instead of manually creating an email and preparing a student report, the system allows you to enter the student's information and a custom message. It then automatically:

* Creates a personalized email
* Includes the student's information in the email body
* Generates a professional HTML report
* Attaches the HTML report to the email
* Sends the email through Gmail SMTP
* Handles errors using exception handling

This project demonstrates practical use of **Python, SMTP, HTML generation, email automation, file handling, and environment variables**.

---

## ✨ Features

* 📧 **Automated Email Sending**
* 👨‍🎓 **Student Information Processing**
* 📝 **Custom Email Message**
* 📄 **Dynamic HTML Report Generation**
* 📎 **HTML Report Attachment**
* 🔐 **Secure Gmail App Password Authentication**
* ⚠️ **Exception Handling**
* 💻 **Command-Line Interface**
* 🧩 **Modular Python Structure**
* 🚀 **Simple and Lightweight**

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      main.py        │
                    │   User Input        │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
          ┌──────────────────┐   ┌──────────────────┐
          │ report_generator │   │  email_service   │
          │      .py         │   │      .py         │
          └────────┬─────────┘   └────────┬─────────┘
                   │                      │
                   ▼                      ▼
          ┌──────────────────┐   ┌──────────────────┐
          │   HTML Report    │──▶│   Email + HTML   │
          │    Generation    │   │    Attachment    │
          └──────────────────┘   └────────┬─────────┘
                                          │
                                          ▼
                                  ┌──────────────────┐
                                  │   Gmail SMTP     │
                                  └────────┬─────────┘
                                           │
                                           ▼
                                  ┌──────────────────┐
                                  │ Student's Email  │
                                  └──────────────────┘
```

---

## 📂 Project Structure

```text
student-email-automation/
│
├── main.py
├── email_service.py
├── report_generator.py
├── requirements.txt
├── .env
├── .gitignore
│
└── README.md
```

### File Description

| File                  | Purpose                                      |
| --------------------- | -------------------------------------------- |
| `main.py`             | Main application and user input              |
| `email_service.py`    | Gmail SMTP connection and email sending      |
| `report_generator.py` | Dynamic HTML report generation               |
| `.env`                | Stores email credentials securely            |
| `.gitignore`          | Prevents sensitive files from being uploaded |
| `requirements.txt`    | Python dependencies                          |
| `README.md`           | Project documentation                        |

---

## 🔄 How It Works

### Step 1 — Enter Student Information

The program asks for:

```text
Student ID
Student Name
Student Email
Course
Status
```

Example:

```text
Student ID: 1001
Student Name: Joynul Hasan
Student Email: student@gmail.com
Course: Computer Science
Status: Active
```

---

### Step 2 — Enter Custom Message

The user enters a personalized message:

```text
Your student registration has been successfully completed.
```

---

### Step 3 — Generate HTML Report

The system dynamically creates an HTML report containing the student's information.

Example:

```text
student_report_1001.html
```

The report contains:

* Student ID
* Student Name
* Email
* Course
* Status

---

### Step 4 — Create Email

The system creates a personalized email.

```text
Subject:
Student Report - Joynul Hasan
```

The email body contains:

```text
Dear Joynul Hasan,

Your student registration has been successfully completed.

Student Information:

Student ID: 1001
Name: Joynul Hasan
Email: student@gmail.com
Course: Computer Science
Status: Active

Please find the attached HTML report for your student information.

Best regards,
Student Data Management System
```

---

### Step 5 — Attach HTML Report

The generated HTML file is automatically attached:

```text
📎 student_report_1001.html
```

---

### Step 6 — Send Through Gmail SMTP

The application connects to:

```text
smtp.gmail.com
Port: 587
```

The connection uses **TLS encryption** and Gmail App Password authentication.

---

## 🛠️ Technologies Used

### Programming Language

* 🐍 Python 3

### Libraries

* `smtplib`
* `email.mime`
* `python-dotenv`

### Other Technologies

* HTML5
* CSS3
* Gmail SMTP
* Environment Variables

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-email-automation.git
```

### 2. Enter the Project Directory

```bash
cd student-email-automation
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Gmail Configuration

This project uses a **Gmail App Password** rather than your normal Gmail password.

Create a `.env` file in the project root:

```env
YOUR_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_16_character_app_password
```

### ⚠️ Security Warning

**Never upload your `.env` file to GitHub.**

Your `.gitignore` should contain:

```gitignore
.env
__pycache__/
*.pyc
student_report_*.html
```

If an App Password is accidentally exposed, revoke it immediately and generate a new one.

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Example:

```text
==================================================
     STUDENT EMAIL AUTOMATION SYSTEM
==================================================

Enter Student Information

Student ID: 1001
Student Name: Joynul Hasan
Student Email: student@gmail.com
Course: Computer Science
Status: Active

Enter Email Message
Message: Your registration has been successfully completed.

[1/3] Generating HTML report...
[SUCCESS] Report created: student_report_1001.html

[2/3] Preparing email...

[3/3] Sending email...

[SUCCESS] Email sent successfully!
[INFO] Recipient: student@gmail.com
[INFO] Attachment: student_report_1001.html
```

---

## 📧 Email Workflow

```text
Student Data
     │
     ▼
Custom Message
     │
     ▼
Generate HTML Report
     │
     ▼
Create Email
     │
     ├── Email Body
     │
     └── HTML Attachment
     │
     ▼
Gmail SMTP
     │
     ▼
Student Email
```

---

## 📊 Sample HTML Report

The generated report provides a clean browser-friendly view of the student's information.

```text
┌─────────────────────────────────────────┐
│       Student Information Report        │
├─────────────────────────────────────────┤
│ Student ID │ 1001                       │
│ Name       │ Joynul Hasan               │
│ Email      │ student@gmail.com          │
│ Course     │ Computer Science           │
│ Status     │ Active                     │
└─────────────────────────────────────────┘
```

---

## 🧠 Error Handling

The application uses Python exception handling to prevent unexpected failures.

For example:

```python
try:
    ...
except Exception as error:
    print(f"[ERROR] {error}")
```

Possible errors include:

* Invalid Gmail credentials
* SMTP connection failure
* Missing `.env` configuration
* Invalid email address
* HTML report file errors
* Network connection problems

---

## 🔒 Security Practices

This project follows basic security practices:

* Credentials are stored in `.env`
* `.env` is excluded using `.gitignore`
* Gmail App Password is used instead of the normal account password
* TLS is enabled for SMTP communication
* Sensitive credentials are not hard-coded into the source code

---

## 🚀 Future Improvements

Possible future upgrades include:

* 📊 CSV/Excel student data import
* 📧 Bulk email sending
* 📨 Email delivery logs
* 📎 PDF report generation
* 🖥️ GUI interface
* 🌐 Web-based dashboard
* 🗄️ SQLite/MySQL database
* 📅 Scheduled email delivery
* 📋 Email templates
* 📈 Student statistics dashboard
* 🔐 Improved credential management

---

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

```text
Python Programming
       │
       ├── File Handling
       ├── Functions
       ├── Exception Handling
       ├── Environment Variables
       │
       ▼
Email Automation
       │
       ├── SMTP
       ├── TLS
       ├── MIME
       └── Attachments
       │
       ▼
Report Generation
       │
       ├── HTML
       └── CSS
```

---

## 👨‍💻 Author

**Joynul Hasan**

Aspiring Cybersecurity Analyst | SOC | Network Security | Python

### Connect With Me

* 💼 LinkedIn: [Joynul Hasan](https://www.linkedin.com/)
* 🐙 GitHub: [Joynul Hasan](https://github.com/)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the **MIT License**.

---

> **Built with Python 🐍 | SMTP 📧 | HTML 🌐 | Automation ⚡**
