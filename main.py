from flask import Flask, render_template, request
import scraper

app = Flask(__name__)

@app.route("/")
def home():
    bookResults = scraper.find_books()
    filmResults = scraper.find_films()
    gameResults = scraper.find_games()

    anyBookResults = True
    anyFilmResults = True
    anyGameResults = True

    if request.args.get("letter") != None:

        for i in bookResults.copy():
            if not i.startswith(request.args.get("letter").upper()):
                del bookResults[i]

        for i in filmResults.copy():
            if not i.startswith(request.args.get("letter").upper()):
                del filmResults[i]

        for i in gameResults.copy():
            if not i.startswith(request.args.get("letter").upper()):
                del gameResults[i]

        if bookResults == {}:
            anyBookResults = False
        if filmResults == {}:
            anyFilmResults = False
        if gameResults == {}:
            anyGameResults = False

        return render_template("index.html", book_results = bookResults,
                                             film_results = filmResults,
                                             game_results = gameResults,
                                             any_book_results = anyBookResults,
                                             any_film_results = anyFilmResults,
                                             any_game_results = anyGameResults)
    else:
        return render_template("index.html", book_results = {},
                                             film_results = {},
                                             game_results = {})

if __name__ == "__main__":
    app.run(debug=True)
