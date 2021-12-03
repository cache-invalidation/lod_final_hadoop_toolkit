#!/bin/python3
import json
from bs4 import BeautifulSoup
from glob import glob

names_mask = [  {'name': 'Eвгени', 'surname': 'Медведев'},
                {'name': 'Игор', 'surname': 'Акинфеев'},
                {'name': 'Александр', 'surname': 'Овечкин'},
                {'name': 'Олег', 'surname': 'Тиньков'},
                {'name': 'Ольг', 'surname': 'Наумов'},
                {'name': 'Андре', 'surname': 'Андреев'},
                {'name': 'Алексе', 'surname': 'Картынник'},
                {'name': 'Игор', 'surname': 'Бухман'},
                {'name': 'Юри', 'surname': 'Дуд'},
                {'name': 'Григори', 'surname': 'Перельман'}]

names = [   {'name': 'Eвгения', 'surname': 'Медведева', 'patronymic':'Армановна'},
            {'name': 'Игорь', 'surname': 'Акинфеев', 'patronymic': 'Владимирович'},
            {'name': 'Александр', 'surname': 'Овечкин', 'patronymic': 'Михайлович'},
            {'name': 'Олег', 'surname': 'Тиньков', 'patronymic': 'Юрьевич'},
            {'name': 'Ольгa', 'surname': 'Наумовa', 'patronymic': 'Валерьевна'},
            {'name': 'Андрей', 'surname': 'Андреев', 'patronymic': 'Вагнерович'},
            {'name': 'Алексей', 'surname': 'Картынник', 'patronymic': ''},
            {'name': 'Игорь', 'surname': 'Бухман', 'patronymic': 'Анатольевич'},
            {'name': 'Юрий', 'surname': 'Дудь', 'patronymic': 'Александрович'},
            {'name': 'Григорий', 'surname': 'Перельман', 'patronymic': 'Яковлевич'}]

def decide_person(text):
    for i in range(len(names_mask)):
        person = names_mask[i]
        if person['surname'] in text:
            return names[i]
    return None

def main():
    articles = open('articles.json', 'w')

    articles_data = []

    filenames = glob('input_html/*')
    for filename in filenames:
        print('Processing ' + filename)
        file = open(filename, 'r') 
        try:
            page = file.read()
        except UnicodeDecodeError:
            file.close()
            continue
        link = page.split('\n')[1].split('saved from url')[1].split(')')[1].split()[0]
        print(link)

        soup = BeautifulSoup(page, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        file.close()

        text = soup.get_text()
        person = decide_person(text)
        if person is None:
            continue

        articles_data.append({'link': link, 'name': person['name'], 'surname': person['surname'], 'patronymic': person['patronymic'], 'text': text})
    articles_json = {'articles': articles_data}
    articles.write(json.dumps(articles_json))
    articles.close()

if __name__ == '__main__':
    main()
