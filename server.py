from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)


data = {
    1: {
        "id": 1,
        "name": "Kaori Sakamoto",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Kaori_Sakamoto_4cc_2018.jpg/330px-Kaori_Sakamoto_4cc_2018.jpg",
        "description": "Kaori Sakamoto is a Japanese figure skater. She is the 2022 Olympic bronze medalist, a two-time World champion (2022, 2023), the 2023–24 Grand Prix Final champion, the 2018 Four Continents champion, a five-time ISU Grand Prix champion, and a four-time Japanese national champion. She is a bronze medalist in the 2022 Olympic team event.[a] At the junior level, she is the 2017 World Junior bronze medalist and the 2016–17 Junior Grand Prix Final bronze medalist.",
        "birth_year": 2000,
        "same_country": [5, 7],
    },
    2: {
        "id": 2,
        "name": "Nathan Chen",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Nathan_Chen_at_the_2018_Internationaux_de_France_-_Awarding_ceremony.jpg/330px-Nathan_Chen_at_the_2018_Internationaux_de_France_-_Awarding_ceremony.jpg",
        "description": "Nathan Wei Chen is an American figure skater. He is the 2022 Olympic champion, a three-time World champion (2018, 2019, 2021), the 2017 Four Continents champion, a three-time Grand Prix Final champion (2017, 2018, 2019), a ten-time Grand Prix medalist (8 golds, 1 silver, 1 bronze), the presumptive 2022 Olympic silver medalist in the team event,[note 1] the 2018 Olympic bronze medalist in the team event, and a six-time U.S. national champion (2017–22). At the junior level, Chen is the 2015–16 Junior Grand Prix Final champion, 2013–14 Junior Grand Prix Final bronze medalist, 2014 World Junior bronze medalist, and a six-time Junior Grand Prix medalist (5 golds, 1 silver).",
        "birth_year": 1999,
        "same_country": [4, 10],
    },
    3: {
        "id": 3,
        "name": "Alena Kostornaia",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/2019_Internationaux_de_France_Saturday_medals_ladies_8D9A2530.jpg/330px-2019_Internationaux_de_France_Saturday_medals_ladies_8D9A2530.jpg",
        "description": "Alena Sergeyevna Kostornaia is a Russian figure skater. She is the 2020 European champion, the 2019–20 Grand Prix Final champion, a six-time Grand Prix medalist (including gold at the 2019 Internationaux de France and the 2019 NHK Trophy), and the 2019 CS Finlandia Trophy champion. Competing domestically, she is a three-time Russian senior national medalist (silver 2020, bronze 2018 and 2019). She previously held the world record for the highest senior short program score in women's skating.",
        "birth_year": 2003,
        "same_country": [6, 8, 9],
    },
    4: {
        "id": 4,
        "name": "Karen Chen",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Karen_Chen_2017.jpg/330px-Karen_Chen_2017.jpg",
        "description": "Karen Chen is an American figure skater. She is a 2022 Olympic Games team event gold medalist, two-time CS U.S. Classic bronze medalist (2016, 2017), the 2015 CS Golden Spin of Zagreb bronze medalist, the 2017 U.S. national champion, 2022 U.S. national silver medalist, and a three-time U.S. national bronze medalist (2015, 2018, 2021). She is currently a student at Cornell University.",
        "birth_year": 1999,
        "same_country": [2, 10],
    },
    5: {
        "id": 5,
        "name": "Shoma Uno",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Uno_-_2018_Olympics.jpg/330px-Uno_-_2018_Olympics.jpg",
        "description": "Shoma Uno is a Japanese figure skater. He is a three-time Olympic medalist (2018 silver, 2022 bronze, 2022 team bronze), a two-time World champion (2022, 2023) and a two-time World silver medalist (2018, 2017), the 2019 Four Continents champion, the 2022–23 Grand Prix Final champion, a fourteen-time Grand Prix medalist (8 gold, 6 silver), the 2017 Asian Winter Games champion, and a six-time Japanese national champion (2016–2019, 2022–2023). At the junior level, Uno is the 2015 World Junior champion, the 2014–15 Junior Grand Prix Final champion, and 2012 Youth Olympic silver medalist.",
        "birth_year": 1997,
        "same_country": [1, 7],
    },
    6: {
        "id": 6,
        "name": "Evgenia Medvedeva",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Evgenia_Medvedeva_at_the_2018_Winter_Olympic_Games_-_Awarding_ceremony.jpg/330px-Evgenia_Medvedeva_at_the_2018_Winter_Olympic_Games_-_Awarding_ceremony.jpg",
        "description": "Evgenia Armanovna Medvedeva is a retired competitive Russian figure skater. She is the 2018 PyeongChang Olympic silver medalist (2018 ladies' singles, 2018 team event), a two-time world champion (2016, 2017), a two-time European champion (2016, 2017), a two-time Grand Prix Final champion (2015, 2016), a two-time Russian national champion (2016, 2017), silver medalist at the 2018 European Figure Skating Championships and bronze medalist at the 2019 World Championships. Earlier in her career, she won the 2015 World Junior Championships, the 2014 Junior Grand Prix Final, and the 2015 Russian Junior Championships.",
        "birth_year": 1999,
        "same_country": [3, 8, 9],
    },
    7: {
        "id": 7,
        "name": "Yuzuru Hanyu",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/2018_Winter_Olympics_-_Yuzuru_Hanyu_%28cropped%29.jpg/330px-2018_Winter_Olympics_-_Yuzuru_Hanyu_%28cropped%29.jpg",
        "description": "Yuzuru Hanyu is a Japanese figure skater and ice show producer. He is a two-time Olympic champion (2014, 2018), a two-time World champion (2014, 2017), a four-time Grand Prix Final champion (2013–2016), the 2020 Four Continents champion, the 2010 World Junior champion, the 2009–10 Junior Grand Prix Final champion, and a six-time Japanese national champion (2012–2015, 2020–2021). He has also medaled at five other World Championships, taking bronze in 2012 and 2021, and silver in 2015, 2016 and 2019, making him the only male single skater along with Jan Hoffmann to win seven world championship medals in the post-World War II era.",
        "birth_year": 1994,
        "same_country": [5, 1],
    },
    8: {
        "id": 8,
        "name": "Anna Shcherbakova",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/2020_12_27_anna_shcherbakova_%28cropped%29.jpg/330px-2020_12_27_anna_shcherbakova_%28cropped%29.jpg",
        "description": "Anna Stanislavovna Shcherbakova is a Russian figure skater. She is the reigning Olympic champion (2022), a World champion (2021), a European Champion (2022), and a three-time Russian national champion (2019–2021). She was the first woman figure skater to land a quad Lutz in senior competition and the first woman to land two quad Lutz jumps in a single program. She was also the first woman figure skater to land a quad flip in combination with a triple jump, as well as the first to land two quad flip jumps in a single program. She is the first Olympic champion in women’s single skating with quad jumps. The quad Lutz and quad flip are among the three most difficult jumps in figure skating, only behind the quad axel.[2] Additionally, she never finished below second place in her senior career.",
        "birth_year": 2004,
        "same_country": [3, 6, 9],
    },
    9: {
        "id": 9,
        "name": "Alina Zagitova",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Alina_Zagitova_at_the_World_Championships_2019_-_Awarding_ceremony_03.jpg/330px-Alina_Zagitova_at_the_World_Championships_2019_-_Awarding_ceremony_03.jpg",
        "description": "Alina Ilnazovna Zagitova is a Russian figure skater. She is the 2018 Olympic champion, the 2019 World champion, the 2018 European champion, 2017–18 Grand Prix Final champion, and the 2018 Russian national champion. Zagitova also won a silver medal in the team event at the 2018 Winter Olympics, representing the Olympic Athletes from Russia team.[8]",
        "birth_year": 2002,
        "same_country": [3, 6, 8],
    },
    10: {
        "id": 10,
        "name": "Ilia Malinin",
        "image": "https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcShJ_2V_2Ez1kZZkXjdbyw2aa7xZTl72n4dsj6jACD-heMi_WVG1iXVHCexAjCiLf3U",
        "description": "Ilia Malinin is an American figure skater. He is the 2023–24 Grand Prix Final champion, 2023 World bronze medalist, the 2022-23 Grand Prix Final bronze medalist, a four-time Grand Prix medalist (3 gold, 1 silver), a three-time ISU Challenger Series medalist (2 gold, 1 bronze), the 2023 and 2024 U.S. national champion, and the 2022 U.S. national silver medalist. At the junior level, Malinin is the 2022 World Junior champion, and a two-time Junior Grand Prix gold medalist. He holds the current world junior record for the men's short program, free skate, and combined score.",
        "birth_year": 2004,
        "same_country": [2, 4],
    },
}


def get_names():
    names = {}
    for id, skater in data.items():
        names[id] = skater["name"]
    return names


# ROUTES


@app.route("/")
def start():
    return render_template("home.html", names=get_names())


@app.route("/home")
def home():
    return render_template("home.html", names=get_names())


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form["search"]
        matching_skaters = []

        for skater_id, skater_info in data.items():
            if search_term.lower() in skater_info["name"].lower():
                matching_skaters.append(skater_info)
        return render_template(
            "search_results.html", searchTerm=search_term, result=matching_skaters
        )
    return render_template("home.html", names=get_names())


@app.route("/view/<int:id>")
def view(id):
    skater = data.get(id)  # Assuming 'data' is your dictionary containing all items
    if skater:
        return render_template("view.html", skater=skater)


# AJAX FUNCTIONS
# @app.route("/lookup", methods=["GET", "POST"])
# def lookup():

#     return jsonify(matching_skaters)


if __name__ == "__main__":
    app.run(debug=True)
