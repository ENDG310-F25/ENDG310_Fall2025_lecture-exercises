from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Welcome to Flask!")

@app.route("/submit", methods=["POST"])
def submit():
    user_input = request.form.get("user_input")
    
    return render_template("response.html",message = f"{user_input}")

if __name__ == "__main__":
    app.run(debug=True)
