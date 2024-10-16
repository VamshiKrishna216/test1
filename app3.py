from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)

@app.route("/")
def func():
    return "welcome to gvk's space"

@app.route("/log")
def func1():
    return  render_template("aa.html")

@app.route("/mr")
def func2():
    return  redirect(url_for("func"))


if __name__=="__main__":
    app.run(debug=True)
