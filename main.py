import requests
import json
from pprint import pprint


class CountriesInWiki:
    def __init__(self, path):
        self.dict_countries = dict()
        self.list_countries = list()
        self.path = path
        self.session = requests.session()
        self.counter = 0
        with open(path, encoding='utf-8') as file:
            self.j_file = json.load(file)
        for item in self.j_file:
            country_rus = item['translations']['rus']['common']
            country_link = country_rus.replace(' ', '_')
            wiki_link = f"https://ru.wikipedia.org/wiki/{country_link}"
            self.dict_countries[item['translations']['rus']['common']] = wiki_link
            self.list_countries.append({item['translations']['rus']['common']: wiki_link})

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if len(self.dict_countries) == self.counter-1:
            self.counter = 0
            raise StopIteration
        return self.list_countries[self.counter - 1]


if __name__ == '__main__':
    j_path = 'countries.json'
    # response = requests.get('https://ru.wikipedia.org/wiki/Афганистан')
    # print(response.status_code)
    countries_in_wiki = CountriesInWiki(j_path)
    print(len(countries_in_wiki.list_countries))
    for item in countries_in_wiki:
        pprint(item)
