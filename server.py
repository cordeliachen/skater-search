from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json

app = Flask(__name__)

with open("data.json") as f:
    data = json.load(f)


# ROUTES
@app.route("/")
def start():
    return render_template("home.html", data=data)


@app.route("/home")
def home():
    return render_template("home.html", data=data)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form["search"]
        matching_skaters = []

        for skater_id, skater_info in data.items():
            if (
                search_term.lower() in skater_info["name"].lower()
                or search_term.lower() in skater_info["country"].lower()
                or search_term.lower() in skater_info["discipline"].lower()
            ):
                matching_skaters.append(skater_info)
        return render_template(
            "search_results.html", searchTerm=search_term, results=matching_skaters
        )
    return render_template("home.html", data=data)


@app.route("/view/<id>")
def view(id):
    skater = data.get(id)
    if skater:
        return render_template("view.html", skater=skater)


@app.route("/view/<int:id>")
def view2(id):
    skater = data.get(str(id))
    if skater:
        return render_template("view.html", skater=skater)


# AJAX FUNCTIONS
# @app.route("/lookup", methods=["GET", "POST"])
# def lookup():

#     return jsonify(matching_skaters)


if __name__ == "__main__":
    app.run(debug=True)
