from bs4 import BeautifulSoup
import requests

# Scrapes book page and returns a dictionary mapping each book title to it's associated food and drinks
def find_books():
    URL = 'http://www.fiction-food.com/p/banquet-of-books.html'
    content = requests.get(URL)

    soup = BeautifulSoup(content.text, 'html.parser')

    responses = {}

    for line in soup.find_all('b'):

        if '<b><i>' in str(line):
            foodsAndDrinks = []
            currentFoodOrDrink = line.find_next_sibling('a')

            while '<b><i>' not in str(currentFoodOrDrink):
                if '<a href' in str(currentFoodOrDrink):
                    foodsAndDrinks.append(currentFoodOrDrink.text.strip().encode('utf-8'))
                if currentFoodOrDrink != None:
                    currentFoodOrDrink = currentFoodOrDrink.next_sibling
                else:
                    break

            responses[line.text.strip().encode('utf-8')] = foodsAndDrinks

    return responses

# Scrapes film & TV page and returns a dictionary mapping each book title to it's associated food and drinks
def find_films():
    URL = 'http://www.fiction-food.com/p/a-feast-of-film.html'
    content = requests.get(URL)

    soup = BeautifulSoup(content.text, 'html.parser')

    responses = {}

    for line in soup.find_all('b'):
        if '<b>' in str(line) and '*' not in str(line) and 'Click' not in str(line) and len(str(line)) > 8:
            films = []
            currentFilm = line.find_next_sibling('a')

            while '<b>' not in str(currentFilm):
                if '<a href' in str(currentFilm):
                    films.append(currentFilm.text.strip().encode('utf-8'))
                if currentFilm != None:
                    currentFilm = currentFilm.next_sibling
                else:
                    break

            responses[line.text.strip().encode('utf-8')] = films

    return responses

# Scrapes film & TV page and returns a dictionary mapping each book title to it's associated food and drinks
def find_games():
    URL = 'http://www.fiction-food.com/p/gourmet-games.html'
    content = requests.get(URL)

    soup = BeautifulSoup(content.text, 'html.parser')

    responses = {}

    strings = ['*', 'Top', 'Home']

    for line in soup.find_all('b'):


        if '<b>' in str(line) and all(x not in str(line) for x in strings) and len(str(line)) > 8:
            foodsAndDrinks = []
            currentFoodOrDrink = line.find_next_sibling('a')

            while '<b>' not in str(currentFoodOrDrink):
                if '<a href' in str(currentFoodOrDrink):
                    foodsAndDrinks.append(currentFoodOrDrink.text.strip().encode('utf-8'))
                if currentFoodOrDrink != None:
                    currentFoodOrDrink = currentFoodOrDrink.next_sibling
                else:
                    break

            responses[line.text.strip().encode('utf-8')] = foodsAndDrinks

    del responses['A B C D E F G H I J K L M N O P Q R S T U V W X Y Z']

    return responses
