from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("pineapples.html")

@app.route('/another')
def another():
    return render_template("pineapple2.html")

@app.route('/three/<name>')
def three(name):
    
    someList = ["one","two","three"]
    return render_template("pineapple3.html",
                           someNewVar = name,
                           my_list = someList)

@app.route('/four')
def four():
    a_new_list = [1,2,3,4,5]
    b_new_list = ["yellow","orange","blue", "green", "turquoise","fuscia","navy"]

    return render_template("pineapple4.html",a_num_list = a_new_list,color_list = b_new_list)


app.run(debug=True)