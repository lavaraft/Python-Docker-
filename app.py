from flask import Flask, render_template, request, url_for 

app = Flask(__name__)

@app.route("/items", methods=["GET", "POST"])
def shoppingitems():
    return render_template("items.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)