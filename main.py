import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def simple_search(input_string: str, dataset_filename: str) -> None:
    '''
    Функция осуществляет простой поиск подстроки
    :param input_string: комментарий пользователя о банкомате
    :param dataset_filename: файл, по которому осуществляется поиск города
    :return: None
    '''

    cities = pd.read_csv(dataset_filename)  # Открываем файл со списком городов
    flag = True
    for i in range(len(cities)):
        # Берем из списка каждый город и проверяем, находится ли он в сообщении пользователя
        if flag and cities.iloc[i]['city'] in input_string.lower():
            flag = False
            print(f'Город - {cities.iloc[i]["Город"]}\n'
                  f'Координаты: {cities.iloc[i]["lat"]}, {cities.iloc[i]["lng"]}')
        # Если подошло несколько городов, то выведем об этот сообщение
        elif cities.iloc[i]['city'] in input_string.lower():
            print(f'\nВозможно, вы имели в виду:\n'
                  f'Город - {cities.iloc[i]["Город"]}\n'
                  f'Координаты: {cities.iloc[i]["lat"]}, {cities.iloc[i]["lng"]}')
    else:
        flag = True


def trie_search(input_string: str, dataset_filename: str):
    pass


def fuzzy_search(input_string: str, dataset_filename: str) -> None:
    '''
    Функция осуществляет неявный текстовый поиск
    :param input_string:
    :param dataset_filename:
    :return: None
    '''
    cities = pd.read_csv(dataset_filename)  # Открываем файл со списком городов
    cities_list = cities['Город'].tolist()
    process_res = []
    for word in input_string.split():
            process_res.append([word, process.extract(word, cities_list, limit=1)])

    # print(process_res)

    for elem in process_res:
        for i in range(len(cities)):
            if cities.iloc[i]['city'] in elem[0].lower():
                for city, prob in elem[1]:
                    print(f'\nC вероятностью {prob}%, вы имели в виду:\n'
                          f'Город - {city}\n'
                          f'Координаты: {cities[cities["Город"] == city].iloc[0]["lat"]}, {cities[cities["Город"] == city].iloc[0]["lng"]}')


# region Создание списка городов
#
# df = pd.read_excel('russian_cities.xlsx')
# # print(df.info())
# cities = df['Город'].tolist()
# new_cities = []
# for city in cities:
#     city = city.lower()
#     if 'ё' in city:
#         city = city.replace("ё", "е")
#     if city[-2:] in ["ый", "ий"]:
#         city = city[:-2]
#     elif city[-1] in ["ь", "а", "ы", "й"]:
#         city = city[0:-1]
#     new_cities.append(city)
#
# # print(cities)
# # print(new_cities)
# sample_string = sample_string.lower()
# df_new = df[['Город', 'lat', 'lng']]
# df_new.insert(1, 'city', new_cities)
# # print(df_new.head(3))
#
# df_new.to_csv('russian_cities_valid.csv')
# endregion


# print('🟨🟦🟩🟧🟥')
input_string = input('Введите строку: ')
simple_search(input_string, 'russian_cities_valid.csv')
print()

print()
fuzzy_search(input_string, 'russian_cities_valid.csv')
