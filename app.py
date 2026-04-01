from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/student/register", methods =["GET","POST"])
def student_register():
    if request.method=="POST":
        student_id= request.form.get("student_id")
        student_name=request.form.get("student_name")
        program_name=request.form.get("program_name")
        mobile_number=request.form.get("mobile_number")
        email_id=request.form.get("email_id")       

        print(student_id)
        print(student_name)
        print(program_name)
        print(mobile_number)
        print(email_id)
        return ("Data entered successfully")
    
    return render_template("studentregister.html")

@app.route("/company/register",methods=["GET","POST"])
def company_register():
    if request.method=="POST":
        company_id=request.form.get("company_id")
        company_name=request.form.get("company_name")
        mobile_number=request.form.get("mobile_number")
        email_id=request.form.get("email_id")
        print(company_id)
        print(company_name)
        print(mobile_number)
        print(email_id)
        return("Registered successfully")

    return render_template("companyregister.html")

@app.route("/student/dashboard")
def student_dashboard():
    return render_template("studentdashboard.html")

@app.route("/company/dashboard")
def company_dashboard():
    return render_template("companydashboard.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admindashboard.html")

@app.route("/job/post")
def job_post():
    return render_template("jobposting.html")

@app.route("/job/apply")
def job_apply():
    return render_template("jobapply.html")

@app.route("/apply/status")
def apply_status():
    return render_template("jobstatus.html")

@app.route("/about")
def about():
    return render_template("about.html")
if __name__=="__main__":
    app.run(debug=True)