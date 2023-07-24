+from operator import itemgetter


def word_count(file_name):
    # Проверка файла
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            words = file.read()
            file.close()
    except FileNotFoundError:
        return print("Ошибка. Файл не найден")
    arr = words.split()                                                    # Преобразование содержимого файла в массив
    # print(arr)  # для отладки

    # Составление словаря со словами из массива и количеством использования каждого слова
    words_cnt = {}
    for i in arr:
        count = 0
        for k in arr:
            if i == k:
                count += 1
            words_cnt.update({i: count})
    sorted_words_cnt = dict(sorted(words_cnt.items(), key=itemgetter(1)))  # Сортировка словаря по значениям ключей
    reversed_word_cnt = dict(reversed(sorted_words_cnt.items()))           # Переворот словаря
    return print(list(reversed_word_cnt.keys())[0])                        # Вывод на экран первый элемент словаря


word_count('task56.txt')