import flask as f
r = f.request

app = f.Flask(__name__)

@app.route("/")
def index():
    key = r.cookies.get("key")
    baddcookie = r.cookies.get("badcookie")
    if key and key in ["list of valid keys"] and not baddcookie:
        return f.render_template("index.jinja", args=r.args)
    elif baddcookie:
        badcookie = f.make_response("timer is reset")
        badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
        return badcookie
    elif key:
        badcookie = f.make_response("bad")
        badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
        return badcookie
    return f.redirect("/login/")

@app.route("/login/",methods=["GET","POST"])
def login():
    if r.method == "GET":
        return f.render_template("login.jinja")
    elif r.method == "POST":
        if r.form["key"]:
            if r.form["key"] in ["list of valid keys"]:
                keyy = f.make_response("Granting access: Valid key")
                keyy.set_cookie("key",r.form["key"])
                return f.redirect("/")
            return f.redirect("#incorrect")
        return f.redirect("#")

@app.route("/keygen/",methods=["GET","POST"])
def keygen():
    # add logic for master key
    if r.method == "GET":
        pass
    elif r.method == "POST":
        pass # logic for making key