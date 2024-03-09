from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

with open("data.json") as f:
    data = json.load(f)

current_id = len(data)


def sort_results(skaters_data):
    # Sort results by year for each competition
    for skater_info in skaters_data.values():
        results = skater_info.get("results")
        if results:
            for competition, results_list in results.items():
                results_list.sort(key=lambda x: x["year"], reverse=True)
    return skaters_data


def parse_date(date_str):
    # Parse the string date into a datetime object
    date_obj = datetime.strptime(date_str, "%B %d, %Y")

    # Extract month, day, and year
    month = date_obj.strftime("%B")
    day = date_obj.day
    year = date_obj.year

    return month, day, year


data = sort_results(data)


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


@app.route("/edit/<int:id>")
def edit(id):
    skater = data.get(str(id))
    if skater:
        month, day, year = parse_date(skater["birthday"])
        return render_template(
            "edit.html",
            skater=skater,
            birth_month=month,
            birth_day=day,
            birth_year=year,
        )


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
    results = json_data["results"]

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
        "results": results,
    }
    data[str(new_id)] = new_skater_entry

    data = sort_results(data)

    # Send back the new skater entry's id
    return jsonify(id=new_id)


@app.route("/edit/edit_skater", methods=["POST"])
def edit_skater():
    json_data = request.get_json()
    print(json_data)
    id = json_data["id"]
    name = json_data["name"]
    image = json_data["image"]
    country = json_data["country"]
    discipline = json_data["discipline"]
    coach = json_data["coach"]
    began_skating = json_data["began_skating"]
    age = json_data["age"]
    birthday = json_data["birthday"]
    birthplace = json_data["birthplace"]
    results = json_data["results"]

    # Add new skater entry to the array with a new id
    new_skater_entry = {
        "id": id,
        "name": name,
        "image": image,
        "country": country,
        "discipline": discipline,
        "coach": coach,
        "began_skating": began_skating,
        "age": age,
        "birthday": birthday,
        "birthplace": birthplace,
        "results": results,
    }
    data[str(id)] = new_skater_entry

    data = sort_results(data)

    # Send back the new skater entry's id
    return jsonify(id=id)


if __name__ == "__main__":
    app.run(debug=True)
