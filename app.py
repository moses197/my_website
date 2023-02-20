from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("index.html")

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