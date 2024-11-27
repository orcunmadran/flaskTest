from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Test!"

@app.route("/test")
def test_route():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return render_template("test.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)