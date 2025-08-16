import os
import json


def check_images_and_data(input_dir, large_dir, data_json_path):
    """
    Проверяет:
      1. Все ли файлы из data.json существуют в large_dir.
      2. Все ли файлы из large_dir имеют запись в data.json.
      3. Что у каждой записи есть date и description (description может быть пустым).
    Возвращает список ошибок (пустой если всё ок).
    """
    errors = []

    # Загружаем data.json
    if not os.path.exists(data_json_path):
        errors.append(f"Файл {data_json_path} не найден")
        return errors

    try:
        with open(data_json_path, "r", encoding="utf-8") as f:
            data_entries = json.load(f)
    except Exception as e:
        errors.append(f"Ошибка чтения {data_json_path}: {e}")
        return errors

    # Составляем множества id
    ids_in_json = set(entry["id"] for entry in data_entries if "id" in entry)

    ids_in_files = set()
    for file in os.listdir(large_dir):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            ids_in_files.add(os.path.splitext(file)[0].split("-")[0])

    # Проверка: id в JSON, но нет файла
    for id_ in ids_in_json:
        if id_ not in ids_in_files:
            errors.append(f"В JSON есть запись {id_}, но файла нет в {large_dir}")

    # Проверка: файл есть, но нет записи в JSON
    for id_ in ids_in_files:
        if id_ not in ids_in_json:
            errors.append(f"Файл {id_} есть в {large_dir}, но нет записи в JSON")

    # Проверка: обязательные поля
    for entry in data_entries:
        if "id" not in entry:
            errors.append("Запись без поля 'id'")
            continue
        if "date" not in entry:
            errors.append(f"Нет поля 'date' у {entry['id']}")
        if "description" not in entry:
            errors.append(f"Нет поля 'description' у {entry['id']}")

    return errors
