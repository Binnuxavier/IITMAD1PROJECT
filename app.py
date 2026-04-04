from flask import Flask, render_template,request
import sqlite3
app=Flask(__name__)

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
                   location text)""")
    conn.commit()
    conn.close()
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/student/register", methods =["GET","POST"])
def student_register():
    if request.method == "POST":
        student_id= request.form.get("student_id")
        student_name=request.form.get("student_name")
        program_name=request.form.get("program_name")
        mobile_number=request.form.get("mobile_number")
        email_id=request.form.get("email_id")       
        password=request.form.get("password")

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db") 
        cursor =conn.cursor()
        cursor.execute(
            "INSERT INTO students VALUES(?,?,?,?,?,?)",
            (student_id,student_name,program_name,mobile_number,email_id,password)
        )
        conn.commit()
        conn.close()
        print(student_id)
        print(student_name)
        print(program_name)
        print(mobile_number)
        print(email_id)
        
        return render_template("studentdashboard.html",
                               student_id=student_id,
                               student_name=student_name,
                               program_name=program_name,
                               mobile_number=mobile_number,
                               email_id=email_id)
    
    return render_template("studentregister.html")

@app.route("/company/register",methods=["GET","POST"])
def company_register():
    if request.method=="POST":
        company_id=request.form.get("company_id")
        company_name=request.form.get("company_name")
        mobile_number=request.form.get("mobile_number")
        email_id=request.form.get("email_id")
        password=request.form.get("password")
        print(company_id)
        print(company_name)
        print(mobile_number)
        print(email_id)

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db") 
        cursor =conn.cursor()
        cursor.execute(
            "INSERT INTO company VALUES(?,?,?,?,?,?)",
            (company_id,company_name,mobile_number,email_id,password,"Pending")
        )
        conn.commit()
        conn.close()
        return render_template("companydashboard.html",
                               company_id=company_id,
                               company_name=company_name,
                               mobile_number=mobile_number,
                               email_id=email_id)


    return render_template("companyregister.html")

@app.route("/student/login" , methods=["GET","POST"])
def student_login():

    if request.method== "POST":
        student_id = request.form.get("student_id")
        password = request.form.get("password")

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db") 
        cursor =conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id=? AND password=?", 
            (student_id,password))
        student = cursor.fetchone()

        conn.close()

        if student:
            return render_template ("studentdashboard.html",
                                    student_id=student[0],
                                    student_name=student[1],
                                    program_name=student[2],
                                    mobile_number=student[3],
                                    email_id=student[3])
        else:
            return "Invaild Login"
       
        return render_template ("studentdashboard.html")

    return render_template("studentlogin.html")

@app.route("/student/dashboard")
def student_dashboard():
    return render_template("studentdashboard.html")

@app.route("/company/login" , methods=["GET","POST"])
def company_login():

    if request.method== "POST":
        company_id = request.form.get("company_id")
        password = request.form.get("password")

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db") 
        cursor =conn.cursor()

        cursor.execute(
            "SELECT * FROM company WHERE company_id=? AND password=?", 
            (company_id,password))
        
        company = cursor.fetchone()
        
        conn.close()

        if company:
            return render_template ("companydashboard.html",
                                    company_id=company[0],
                                    company_name=company[1],
                                    mobile_number=company[2],
                                    email_id=company[3])
        else:
            return "Invaild Login"
        
        return render_template ("companydashboard.html")

    return render_template("companylogin.html")
@app.route("/company/dashboard")
def company_dashboard():
    return render_template("companydashboard.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admindashboard.html")

@app.route("/job/post", methods=["GET","POST"])
def job_post():
    if request.method == "POST":
        job_id = request.form.get("job_id")
        company_id = request.form.get("company_id")
        job_role = request.form.get("job_role")
        salary = request.form.get("salary")
        location = request.form.get("location")

        conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO jobs VALUES(?,?,?,?,?)",
            (job_id, company_id, job_role, salary, location)
        )
        conn.commit()
        conn.close()

        return "Job Posted Successfully"

    return render_template("jobposting.html")

@app.route("/job/apply")
def job_apply():
    conn = sqlite3.connect(r"C:\Users\binnu\OneDrive\Desktop\iit_project\placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    conn.close()

    return render_template("jobapply.html", jobs=jobs)

@app.route("/apply/status")
def apply_status():
    return render_template("jobstatus.html")

@app.route("/about")
def about():
    return render_template("about.html")
if __name__=="__main__":
    init_db()
    app.run(debug=True)