import email_service

def generate_html_report(student):
    filename = f"student_report_{student['student_id']}.html"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            padding: 40px;
        }}

        .container {{
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }}

        h1 {{
            text-align: center;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 25px;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}

        th {{
            background-color: #f1f1f1;
        }}
    </style>
</head>

<body>

<div class="container">

    <h1>Student Information Report</h1>

    <table>

        <tr>
            <th>Student ID</th>
            <td>{student['student_id']}</td>
        </tr>

        <tr>
            <th>Name</th>
            <td>{student['name']}</td>
        </tr>

        <tr>
            <th>Email</th>
            <td>{student['email']}</td>
        </tr>

        <tr>
            <th>Course</th>
            <td>{student['course']}</td>
        </tr>

        <tr>
            <th>Status</th>
            <td>{student['status']}</td>
        </tr>

    </table>

</div>

</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    return filename