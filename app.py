from flask import Flask, render_template, request
from validator.validator import validate_submission

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/validate", methods=["POST"])
def validate():
    code = request.form.get("code", "")

    result = validate_submission(code)

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)