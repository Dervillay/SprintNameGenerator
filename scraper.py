from bs4 import BeautifulSoup
import requests

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

books = find_books()

for x in books:
    print (x)
    for y in books[x]:
        print (':' + y)
