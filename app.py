from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Test!<br><a href='test'>go to Test... </a><br><a href='test2'>go to Test2... </a>"

@app.route("/test")
def test_route():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return render_template("test.html", data=data)

@app.route("/test2")
def test2_route():
    data = {
        "name": "Orçun",
        "age": 50,
        "city": "Ankara"
    }
    return render_template("test2.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)