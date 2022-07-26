import AddressString
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.string = AddressString.AddressString()
        self.string.replace_rus_to_eng()
        self.get_children_elements()

    def get_soup(self):
        # Создание супа
        response = requests.get(self.string.string, headers={'user-agent': 'YaBrowser/22.7.1.806'})
        soup = BeautifulSoup(response.text, 'html5lib')
        divs = soup.find_all('div', class_='c90a25d457')  # Список всех дивов, содержащих в себе нужные ссылки
        return divs

    def get_children_elements(self):
        self.refs = []
        divs = self.get_soup()
        for div in divs:
            self.refs.append(div.find('a').get('href'))  # Список ссылок

    # def
        # Поиск всех тегов <a>
        # children = []
        # for div in divs:
        #     children.append(div.findChildren('a', recursive=False))
        # print(children)
        # with open("govno.txt", "w", encoding="UTF-8") as file:
        #     file.write(soup.prettify())
