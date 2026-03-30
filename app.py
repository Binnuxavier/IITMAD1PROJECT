from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to placement portal"

@app.route("/login")
def login():
    return "Login Page"

@app.route("/student/register")
def student_register():
    return "Student Register"

@app.route("/company/register")
def company_register():
    return "Company Registration"

@app.route("/student/dashboard")
def student_dashboard():
    return "Student Dashboard"

@app.route("/company/dashboard")
def company_dashboard():
    return "Company Dashboard"

@app.route("/admin/dashboard")
def admin_dashboard():
    return "Admin Dashboard"

@app.route("/job/post")
def job_post():
    return "Job Post"

@app.route("/job/apply")
def job_apply():
    return "Job Apply"

@app.route("/apply/status")
def apply_status():
    return "Apply Status"

@app.route("/about")
def about():
    return "About"
if __name__=="__main__":
    app.run(debug=True)