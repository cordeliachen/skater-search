from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json

app = Flask(__name__)

with open("data.json") as f:
    data = json.load(f)

current_id = len(data)


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


@app.route("/add")
def add():
    return render_template("add.html")


# AJAX FUNCTIONS
@app.route("/save_skater", methods=["POST"])
def save_skater():
    global data
    global current_id

    json_data = request.get_json()
    print(json_data)
    name = json_data["name"]
    image = json_data["image"]
    country = json_data["country"]
    discipline = json_data["discipline"]
    coach = json_data["coach"]
    began_skating = json_data["began_skating"]
    age = json_data["age"]
    birthday = json_data["birthday"]
    birthplace = json_data["birthplace"]

    # Add new skater entry to the array with a new id
    current_id += 1
    new_id = current_id
    new_skater_entry = {
        "id": new_id,
        "name": name,
        "image": image,
        "country": country,
        "discipline": discipline,
        "coach": coach,
        "began_skating": began_skating,
        "age": age,
        "birthday": birthday,
        "birthplace": birthplace,
        "results": {},
    }
    data[str(new_id)] = new_skater_entry

    # Send back the new skater entry's id
    return jsonify(id=new_id)


if __name__ == "__main__":
    app.run(debug=True)
