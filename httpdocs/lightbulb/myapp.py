import flask as f
r = f.request

app = f.Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    key = r.cookies.get("key")
    baddcookie = key = r.cookies.get("badcookie")
    if r.method == "POST":
        pass
    elif r.method == "GET":
        if key and key in ["list of valid keys"] and not baddcookie:
            return f.render_template("index.jinja", args=r.args)
        elif badcookie:
            badcookie = f.make_response("timer is reset")
            badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
            return badcookie
        elif key:
            badcookie = f.make_response("bad")
            badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
            return badcookie
        else:
            print(r.form)
            return f.render_template("login.jinja")

@app.route("/keygen/",methods=["GET","POST"])
def keygen():
    pass