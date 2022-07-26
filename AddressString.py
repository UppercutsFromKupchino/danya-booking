list_of_cities = [
    ["Лондон", "London"]
]


class AddressString:
    def __init__(self):
        with open("адресная строка.txt", "r", encoding="UTF-8") as file:
            self.string = file.read()

    def find_word(self):
        for city in list_of_cities:
            if self.string.find(str(city[0])) != -1:
                return city
        return False

    def replace_rus_to_eng(self):
        city = self.find_word()
        if city is not False:
            self.string = self.string.replace(city[0], city[1], 2)
        else:
            print("Введи город из предложенного списка")
