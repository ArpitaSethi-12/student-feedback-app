from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        name = request.form.get("name")
        course = request.form.get("course")
        feedback = request.form.get("feedback")
        rating = request.form.get("rating")

        if name and course and feedback:

            feedbacks.append({
                "name": name,
                "course": course,
                "feedback": feedback,
                "rating": rating
            })

    return render_template(
        "index.html",
        feedbacks=feedbacks
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )