import flask as f
r = f.request

app = f.Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if r.method == "POST":
        if r.form["key"]:
            if r.form["key"] in ["list of valid keys"]:
                keyy = f.make_response("Granting access: Valid key")
                keyy.set_cookie("key",r.form["key"])
                return keyy
        return "y did u send this POST request?"
    elif r.method == "GET":
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
        return f.abort(401)

@app.route("/keygen/",methods=["GET","POST"])
def keygen():
    pass