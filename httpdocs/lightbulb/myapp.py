import flask as f
r = f.request

app = f.Flask(__name__)

@app.route("/")
def hello():
    return f.render_template("index.jinja", args=r.args)