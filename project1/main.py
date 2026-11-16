from flask import Flask, render_template,request,redirect,url_for,session
app = Flask(__name__)

# specify route
@app.route ("/login", methods= ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        # make dictionary key and put it beside session
        session["user"] = user
        return redirect(url_for("scammed"))
    else:
        return render_template("login.html")


@app.route ("/")
def index():
    
    return render_template("index.html")

@app.route ("/scammed")
def scammed():
    # check if user info is present
    if "user" in session:
        user = session["user"]
    return f"<h1>{user}</h1>"

app.run(debug = True)