import flask as f
r = f.request

app = f.Flask(__name__)

@app.route("/")
def index():
    key = r.cookies.get("key")
    baddcookie = key = r.cookies.get("badcookie")
    if key and key in ["list of valid keys"] and not baddcookie:
        return f.render_template("index.jinja", args=r.args)
    elif badcookie:
        badcookie = f.make_response("timer is reset")
        badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
        f.abort(401)
    elif key:
        badcookie = f.make_response("bad")
        badcookie.set_cookie("badcookie","you-did-a-bad",max_age=3600)
        f.abort(401)
    else:
        return f.render_template("login.jinja")

@app.route("/keygen/")
def keygen():
    r.a