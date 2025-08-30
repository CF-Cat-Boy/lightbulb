import flask as f
import json
r = f.request

app = f.Flask(__name__)

with open("httpdocs/lightbulb/users.json") as user:
    users = json.load(user)

with open("httpdocs/lightbulb/masterkeyword.txt") as keyword:
    masterkeyword = str(keyword)

for k, v in users.items():
    if v["master"] == 1:
        master = k
lovk = [i for i in users] # List Of Valid Keys = LOVK

@app.route("/")
def index():
    key = r.cookies.get("key")
    baddcookie = r.cookies.get("badcookie")
    if key and key in lovk and not baddcookie:
        return f.render_template("index.jinja", args=r.args)
    elif baddcookie:
        badcookie = f.make_response("timer is reset")
        badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
        return badcookie
    elif key:
        badcookie = f.make_response("bad")
        badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
        return badcookie
    return f.redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
    if r.method == "GET":
        return f.render_template("login.jinja")
    elif r.method == "POST":
        if r.form["key"]:
            if r.form["key"] in lovk:
                keyy = f.make_response("Granting access: Valid key")
                keyy.set_cookie("key",r.form["key"])
                return f.redirect("/")
            return f.redirect("#incorrect")
        return f.redirect("#")

@app.route("/keygen/<part>",methods=["GET","POST"])
def keygen(part):
    # add logic for master key
    if r.method == "GET":
        if part == "main" and r.cookies.get("master") == masterkeyword:
            return f.render_template("keygen_main.jinja")
        elif part == "auth":
            return f.render_template("keygen_auth.jinja")
    elif r.method == "POST":
        if part == "auth":
            if r.form["auth"] and r.form["auth"] == master:
                masterr = f.make_response(masterkeyword) # make master-ness cookie
                masterr.set_cookie("master",masterkeyword)
                return f.redirect("/keygen/main")
            else:
                return f.redirect("/keygen/auth")
        elif part == "main":
            return "hi"
    return f.redirect("/keygen/auth")

@app.route("/keygen/")
def kk():
    return f.redirect("/keygen/auth")

@app.route("/keygen/main/hi")
def kkk():
    return f.redirect("/keygen/main")