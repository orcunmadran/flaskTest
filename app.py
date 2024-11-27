from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Test!<br><a href='test'>go to Test... </a>"

@app.route("/test")
def test_route():
    data = {
        "data1": "Open Resource Portal",
        "data2": "openresource.net"
    }
    return render_template("test.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)