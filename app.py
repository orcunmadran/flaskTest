from flask import Flask, render_template
from random import randint

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

@app.route("/loto")
def loto_route():
    
    i = 0
    secilenler = [0,0,0,0,0,0]
    goster = []
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i+=1
        goster.append(sorted(secilenler))
        i=0

    return render_template("loto.html", data=goster)

if __name__ == "__main__":
    app.run(debug=True)