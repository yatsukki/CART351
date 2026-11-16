from flask import Flask, render_template,request,redirect,url_for,session
app = Flask(__name__)

app.secret_key = "hola"

# specify route
@app.route ("/login", methods= ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        pwd = request.form ["p_word"]
        # make dictionary key (user) and put it beside session and give it a value (value being my request.form which is user)
        session["user"] = user
        session["password"] = pwd
        return redirect(url_for("scammed"))
    else:
        return render_template("login.html")


@app.route ("/")
def index():
    
    return render_template("index.html")

@app.route ("/scammed")
def scammed():
    # check if user exists inside session
    if "user" in session and "password" in session:
        user = session["user"]
        password = session["password"]
        return f"<h1>Hello {user}!! you've been scammed lmao we know that your password is {password}, send us $5 billion dollars or we leak your info</h1>"
    else:
        return redirect(url_for("login"))


app.run(debug = True)