from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = "rb_xss_lab_secret"

# In-memory comments list (only for demo)
comments_vuln = []
comments_safe = []


@app.route("/")
def index():
    return render_template("index.html")


# ------------------------------------------------
#  REFLECTED XSS (VULNERABLE)
# ------------------------------------------------
@app.route("/search")
def search():
    q = request.args.get("q", "")
    # Vulnerable: directly injecting user input into HTML
    return render_template("search.html", query=q)


# ------------------------------------------------
#  REFLECTED XSS (SECURE)
# ------------------------------------------------
@app.route("/search_secure")
def search_secure():
    q = request.args.get("q", "")
    # Safe: auto-escaped in template (no |safe, no raw HTML)
    return render_template("search_secure.html", query=q)


# ------------------------------------------------
#  STORED XSS (VULNERABLE)
# ------------------------------------------------
@app.route("/comments", methods=["GET", "POST"])
def comments():
    global comments_vuln
    if request.method == "POST":
        name = request.form.get("name", "anonymous")
        message = request.form.get("message", "")
        # Vulnerable: store raw HTML / script in list
        comments_vuln.append({"name": name, "message": message})
        return redirect(url_for("comments"))

    return render_template("comments.html", comments=comments_vuln)


# ------------------------------------------------
#  STORED XSS (SECURE)
# ------------------------------------------------
@app.route("/comments_secure", methods=["GET", "POST"])
def comments_secure():
    global comments_safe
    if request.method == "POST":
        name = request.form.get("name", "anonymous")
        message = request.form.get("message", "")
        # Safe: store plain text, template will escape it
        comments_safe.append({"name": name, "message": message})
        return redirect(url_for("comments_secure"))

    return render_template("comments_secure.html", comments=comments_safe)


# Simple route to show cookie stealing concept (demo only)
@app.route("/steal")
def steal():
    data = request.args.get("data", "")
    print("[*] Stolen cookie/data:", data)
    # Just show text (in real attack, attacker ke server par jayega)
    resp = make_response("Data received on attacker side (check server console).")
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
