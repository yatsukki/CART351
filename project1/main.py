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
    # variables to fetch user and password

    user = session.get("user")
    password = session.get("password")
    # check if user and password exists inside session
    if not user or not password:
        
        return redirect(url_for("login"))
        
    else:
        return render_template("scammed.html",user = session["user"],
        password = session["password"] )

  


app.run(debug = True)