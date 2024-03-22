from flask import Flask,request,render_template
import joblib
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction", methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        review = request.form["review"]
        if not review:
            msg = "please enter a review"
            return render_template("home.html", msg = msg)
        else:
            model = joblib.load("Model/naive_bayes.pkl")
            prediction = model.predict([review])[0]
            return render_template("output.html",prediction = prediction)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000 ,debug=True)