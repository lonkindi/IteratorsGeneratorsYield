import requests
import json
import hashlib


class CountriesInWiki:
    def __init__(self, path):
        self.list_countries = list()
        self.path = path
        self.session = requests.session()
        self.counter = 0
        with open(path, encoding='utf-8') as file:
            self.j_file = json.load(file)
        for item in self.j_file:
            self.list_countries.append(item['translations']['rus']['common'])

    def __iter__(self):
        f = open('output.txt', 'w')
        f.close()
        return self

    def __next__(self):
        wrap = '\n'
        with open('output.txt', 'a', encoding='utf-8') as out_file:
            self.counter += 1
            if len(self.list_countries) == self.counter - 1:
                print('Ссылки на wiki по этим странам сформированы и выгружены в файл <output.txt>\n')
                self.counter = 0
                raise StopIteration
            item = self.list_countries[self.counter - 1]
            if self.counter == len(self.list_countries):
                wrap = ''
            country_link = item.replace(' ', '_')
            wiki_link = f"{item} - https://ru.wikipedia.org/wiki/{country_link}{wrap}"
            out_file.write(wiki_link)
            return (f'№ {self.counter} - {item}')


def my_md5(path):
    with open(path, encoding='utf-8') as input_file:
        while True:
            curr_str = input_file.readline()
            if not curr_str:
                break
            md5_hash = hashlib.md5(curr_str.strip().encode('utf-8')).hexdigest()
            yield md5_hash


if __name__ == '__main__':
    j_path = 'countries.json'
    countries_in_wiki = CountriesInWiki(j_path)
    print(f'Стран в файле: {len(countries_in_wiki.list_countries)} (см. ниже)')
    input('Для формирования ссылок и экспорта данных в файл введите любой символ => ')
    for item in countries_in_wiki:
        print(item)
    input('Чтобы посчитать md5 хеш строк файла <output.txt> введите любой символ => ')
    counter = 1
    for item in my_md5('output.txt'):
        print(f'№ {counter} = {item}')
        counter += 1
