from flask import Flask, render_template,request,redirect,session
import sqlite3
import uuid
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

app=Flask(__name__)
app.secret_key = "mysecretkey"

def init_db():
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db") 
    cursor =conn.cursor()
    cursor.execute("""
                create table if not exists students(
                student_id text PRIMARY KEY,
                student_name text,
                program_name text,
                mobile_number text,
                email_id text,
                password text)""")
    cursor.execute("""
                   create table if not exists company(
                   company_id text PRIMARY KEY,
                   company_name text,
                   mobile_number text,
                   email_id text,
                   password text,
                   approval_status text)""")
    cursor.execute("""
                   create table if not exists jobs(
                   job_id text PRIMARY KEY,
                   company_id text,
                   job_role text,
                   salary text,
                   location text,
                   expiry_date date)""")
    
    cursor.execute("""
    create table if not exists applications(
    application_id text PRIMARY KEY,
    student_id text,
    job_id text,
    status text)""")
  
    conn.commit()
    conn.close()
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/student/register", methods=["GET", "POST"])
def student_register():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        student_name = request.form.get("student_name")
        program_name = request.form.get("program_name")
        mobile_number = request.form.get("mobile_number")
        email_id = request.form.get("email_id")
        password = request.form.get("password")

        # VALIDATIONS
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            return render_template("studentregister.html",
                                   error="Mobile number must be exactly 10 digits",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if "@" not in email_id:
            return render_template("studentregister.html",
                                   error="Enter a valid email address",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if len(password) < 6:
            return render_template("studentregister.html",
                                   error="Password must be at least 6 characters",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[A-Z]", password):
            return render_template("studentregister.html",
                                   error="Password must contain at least one uppercase letter",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[a-z]", password):
            return render_template("studentregister.html",
                                   error="Password must contain at least one lowercase letter",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[0-9]", password):
            return render_template("studentregister.html",
                                   error="Password must contain at least one number",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[@#$%^&+=!]", password):
            return render_template("studentregister.html",
                                   error="Password must contain at least one special character",
                                   student_id=student_id,
                                   student_name=student_name,
                                   program_name=program_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        # HASH PASSWORD
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students VALUES(?,?,?,?,?,?)",
            (student_id, student_name, program_name, mobile_number, email_id, hashed_password)
        )
        conn.commit()
        conn.close()

        return render_template("studentdashboard.html",
                               student_id=student_id,
                               student_name=student_name,
                               program_name=program_name,
                               mobile_number=mobile_number,
                               email_id=email_id)

    return render_template("studentregister.html")

@app.route("/company/register", methods=["GET", "POST"])
def company_register():
    if request.method == "POST":
        company_name = request.form.get("company_name")
        mobile_number = request.form.get("mobile_number")
        email_id = request.form.get("email_id")
        password = request.form.get("password")

        # VALIDATIONS
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            return render_template("companyregister.html",
                                   error="Mobile number must be exactly 10 digits",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if "@" not in email_id:
            return render_template("companyregister.html",
                                   error="Enter a valid email address",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if len(password) < 6:
            return render_template("companyregister.html",
                                   error="Password must be at least 6 characters",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[A-Z]", password):
            return render_template("companyregister.html",
                                   error="Password must contain at least one uppercase letter",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[a-z]", password):
            return render_template("companyregister.html",
                                   error="Password must contain at least one lowercase letter",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[0-9]", password):
            return render_template("companyregister.html",
                                   error="Password must contain at least one number",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        if not re.search("[@#$%^&+=!]", password):
            return render_template("companyregister.html",
                                   error="Password must contain at least one special character",
                                   company_name=company_name,
                                   mobile_number=mobile_number,
                                   email_id=email_id)

        # HASH PASSWORD
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
        cursor = conn.cursor()

        # AUTO GENERATE COMPANY ID
        cursor.execute("SELECT COUNT(*) FROM company")
        count = cursor.fetchone()[0]
        company_id = "C" + str(101 + count)

        cursor.execute(
            "INSERT INTO company VALUES(?,?,?,?,?,?)",
            (company_id, company_name, mobile_number, email_id, hashed_password, "Pending")
        )
        conn.commit()
        conn.close()

        return render_template("companydashboard.html",
                               company_id=company_id,
                               company_name=company_name,
                               mobile_number=mobile_number,
                               email_id=email_id)

    return render_template("companyregister.html")

@app.route("/student/login", methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        password = request.form.get("password")

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (student_id,)
        )
        student = cursor.fetchone()
        conn.close()

        if student and check_password_hash(student[5], password):
            return render_template("studentdashboard.html",
                                   student_id=student[0],
                                   student_name=student[1],
                                   program_name=student[2],
                                   mobile_number=student[3],
                                   email_id=student[4])
        else:
            return "Invalid Login"

    return render_template("studentlogin.html")

@app.route("/company/login", methods=["GET", "POST"])
def company_login():
    if request.method == "POST":
        company_id = request.form.get("company_id")
        password = request.form.get("password")

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM company WHERE company_id=? AND approval_status=?",
            (company_id, "Approved")
        )
        company = cursor.fetchone()
        conn.close()

        if company and check_password_hash(company[4], password):
            session["company_id"] = company[0]
            return render_template("companydashboard.html",
                                   company_id=company[0],
                                   company_name=company[1],
                                   mobile_number=company[2],
                                   email_id=company[3])
        else:
            return "Invalid Login or Company Not Approved"

    return render_template("companylogin.html")

@app.route("/company/dashboard")
def company_dashboard():
    return render_template("companydashboard.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM company")
    companies = cursor.fetchall()

    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()

    conn.close()

    return render_template("admindashboard.html",
                           students=students,
                           companies=companies,
                           jobs=jobs,
                           applications=applications)
@app.route("/admin/company/approve/<company_id>")
def approve_company(company_id):
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE company SET approval_status=? WHERE company_id=?",
        ("Approved", company_id)
    )

    conn.commit()
    conn.close()

    return redirect("/admin/dashboard")


@app.route("/admin/company/reject/<company_id>")
def reject_company(company_id):
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE company SET approval_status=? WHERE company_id=?",
        ("Rejected", company_id)
    )

    conn.commit()
    conn.close()

    return redirect("/admin/dashboard")

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            return redirect("/admin/dashboard")
        else:
            return "Invalid Admin Login"

    return render_template("adminlogin.html")
@app.route("/job/post", methods=["GET", "POST"])
def job_post():
    if request.method == "POST":
        company_id = session.get("company_id")
        if not company_id:
            return "Please login first"

        job_role = request.form.get("job_role")
        salary = request.form.get("salary")
        location = request.form.get("location")
        expiry_date = request.form.get("expiry_date")

        # Prevent past date from backend too
        if expiry_date < str(date.today()):
            return "Expiry date cannot be in the past"

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
        cursor = conn.cursor()

        # AUTO GENERATE JOB ID
        cursor.execute("SELECT COUNT(*) FROM jobs")
        count = cursor.fetchone()[0]
        job_id = "J" + str(101 + count)

        cursor.execute(
            "INSERT INTO jobs VALUES(?,?,?,?,?,?)",
            (job_id, company_id, job_role, salary, location, expiry_date)
        )

        conn.commit()
        conn.close()

        return "Job Posted Successfully. Job ID: " + job_id

    return render_template("jobposting.html", today=str(date.today()))

@app.route("/job/apply", methods=["GET", "POST"])
def job_apply():
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    if request.method == "POST":
        student_id = request.form.get("student_id")
        job_id = request.form.get("job_id")

        # CHECK IF ALREADY APPLIED
        cursor.execute(
            "SELECT * FROM applications WHERE student_id=? AND job_id=?",
            (student_id, job_id)
        )
        existing = cursor.fetchone()

        if existing:
            conn.close()
            return "Already applied for this job"

        # CHECK IF JOB IS EXPIRED
        cursor.execute("SELECT expiry_date FROM jobs WHERE job_id=?", (job_id,))
        job = cursor.fetchone()

        if job and job[0] < str(date.today()):
            conn.close()
            return "This job has expired"

        # AUTO GENERATE APPLICATION ID
        cursor.execute("SELECT COUNT(*) FROM applications")
        count = cursor.fetchone()[0]
        application_id = "A" + str(101 + count)

        cursor.execute(
            "INSERT INTO applications VALUES(?,?,?,?)",
            (application_id, student_id, job_id, "Pending")
        )

        conn.commit()
        conn.close()

        return "Application submitted successfully. Application ID: " + application_id

    # SHOW ONLY ACTIVE JOBS
    cursor.execute("SELECT * FROM jobs WHERE expiry_date >= ?", (str(date.today()),))
    jobs = cursor.fetchall()

    conn.close()

    return render_template("jobapply.html", jobs=jobs)

@app.route("/company/applications")
def company_applications():
    company_id = session.get("company_id")
    if not company_id:
        return "Please login first"

    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT applications.application_id,
               applications.student_id,
               applications.job_id,
               applications.status
        FROM applications
        JOIN jobs ON applications.job_id = jobs.job_id
        WHERE jobs.company_id = ?
    """, (company_id,))

    applications = cursor.fetchall()
    conn.close()

    return render_template("companyapplications.html", applications=applications)
@app.route("/company/application/update/<application_id>", methods=["POST"])
def update_application_status(application_id):
    company_id = session.get("company_id")
    if not company_id:
        return "Please login first"

    new_status = request.form.get("status")

    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    # Make sure application belongs to this company's job
    cursor.execute("""
        SELECT applications.application_id
        FROM applications
        JOIN jobs ON applications.job_id = jobs.job_id
        WHERE applications.application_id = ? AND jobs.company_id = ?
    """, (application_id, company_id))

    valid_application = cursor.fetchone()

    if not valid_application:
        conn.close()
        return "Unauthorized action"

    cursor.execute(
        "UPDATE applications SET status=? WHERE application_id=?",
        (new_status, application_id)
    )

    conn.commit()
    conn.close()

    return redirect("/company/applications")

@app.route("/apply/status")
def apply_status():
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db", timeout=10)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()

    conn.close()

    return render_template("jobstatus.html", applications=applications)

@app.route("/about")
def about():
    return render_template("about.html")
if __name__=="__main__":
    init_db()
    app.run(debug=True)