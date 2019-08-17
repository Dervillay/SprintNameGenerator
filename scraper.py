from bs4 import BeautifulSoup
import requests
import re

bookURL = 'http://www.fiction-food.com/p/banquet-of-books.html'
content = requests.get(bookURL)

soup = BeautifulSoup(content.text, 'html.parser')

# Functions need sanitising
def find_books():
    responses = []
    for line in soup.find_all('b'):
        if '<b><i>' in str(line):
            responses.append(str(line).replace('<b>', '')
                                      .replace('</b>', '')
                                      .replace('<i>', '')
                                      .replace('</i>', ''))
    return responses

def find_food_and_drink():
    responses = []
    for line in soup.find_all('a'):
        if '<a href' in str(line) and line.string != None:
            if len(line.string) > 3:
                responses.append(line.text.strip().encode('utf-8'))
    return responses[8:]


books = find_books()
foodAndDrink = find_food_and_drink()
