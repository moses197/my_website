from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def greet():
    return render_template("greet.html")

@app.route("/home", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("index.html", name=name)
    if request.method == "GET":
        return render_template("greet.html")
    # else:
    #     return redirect

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact_page.html")

@app.route("/project")
def project():
    return render_template("project_page.html")

if __name__ ==' __main__':
    app.run(debug = True)