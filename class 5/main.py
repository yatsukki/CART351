from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/pineappleA")
def pineAppleA():

    return render_template("pineappleChild.html",
                           dataPassedA = "child A!" )

@app.route("/pineappleB")
def pineAppleB():

    return render_template("pineappleChild_B.html",
                           passedImg = "../static/images/pineapple_2.jpg" )
@app.route("/inputPlant")
def addPlantData():
    return render_template("addPlantData.html") 

@app.route("/")
def index():

    return render_template("index.html", 
                           user={"username":"sabine"},
                           passedDictionary={
                                            "fav_color":"fuscia", 
                                             "fav_veg":"cauliflower",
                                             "fav_fruit":"kiwi",
                                             "fav_animal":"toucan"
                                             },
                            imgPath = "../static/images/pineapple_2.jpg"
                                        
                        )

@app.route("/register")
def register():
     return render_template("register.html")

@app.route("/reg_thank_you",methods = ['POST', 'GET'])
def reg_thank_you():
    app.logger.info(request.form["f_name"])
    app.logger.info(request.form["l_name"])
    return render_template("thank_you_reg.html")



app.run(debug=True)