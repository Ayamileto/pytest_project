# файл dicts.py
def get_val(collection, key, default='git'):
    if isinstance(collection, dict):  # Проверка, что collection является словарем
        if isinstance(key, str):  # Проверка, что key является строкой
            if key in collection:
                return collection[key]
            else:
                return default
        else:
            raise ValueError("Значение key должно быть типа STR")  # Исключение, если key не является строкой
    else:
        raise TypeError("В collection должен быть передан словарь")  # Исключение, если collection не является словарем

