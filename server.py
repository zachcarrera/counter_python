from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'password'


@app.route("/")
def index():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1

    if "visits" in session:
        session["visits"] += 1
    else:
        session["visits"] = 1

    if "increment" not in session:
        session["increment"] = 2

    return render_template("index.html")

@app.route("/button_press", methods=["POST"])
def button_press():
    print("User pressed button!")
    print(request.form)
    if request.form["which_form"] == "add":
        session["count"] += int(session["increment"])-1
        print(f"adding {session['increment']}")
        return redirect("/")
    else:
        session["count"]=0
        return redirect("/")


@app.route("/change_increment", methods=["POST"])
def change_increment():
    session["increment"] = request.form["new_increment"]
    session["count"] -= 1
    return redirect("/")


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    session["count"]=0
    session["increment"]=2
    return redirect("/")

if __name__ == ("__main__"):
    app.run(debug=True)