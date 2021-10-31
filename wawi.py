from flask import Flask, render_template, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "d58bd24dc2e9c3b57492560a5153339a"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/item")
def item():
    return render_template("item.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
