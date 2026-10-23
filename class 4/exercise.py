from flask import Flask

app = Flask(__name__)

app.route("/catworld/<word>")
def catlatin(word):
    if (word[-1].lower() !="y"):
        return f""
app.run()