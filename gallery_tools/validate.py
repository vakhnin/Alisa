import json
import os
import re

INPUT_JSON = "input_images/data.json"

# Регулярка для формата даты YYYY-MM-DD
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_gallery(large_dir):
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        meta_data = json.load(f)

    ids_in_meta = [item["id"] for item in meta_data]
    files_in_folder = [
        os.path.splitext(f)[0].replace("-large", "")
        for f in os.listdir(large_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    ids_in_meta_set = set(ids_in_meta)
    files_in_folder_set = set(files_in_folder)

    errors = False

    # Файлы без описания
    missing_in_json = files_in_folder_set - ids_in_meta_set
    if missing_in_json:
        print(f"❌ В JSON нет описания для: {', '.join(sorted(missing_in_json))}")
        errors = True

    # Описания без файлов
    missing_files = ids_in_meta_set - files_in_folder_set
    if missing_files:
        print(f"❌ В папке нет файлов для: {', '.join(sorted(missing_files))}")
        errors = True

    # Дубликаты id
    duplicates = {x for x in ids_in_meta if ids_in_meta.count(x) > 1}
    if duplicates:
        print(f"❌ Дубликаты id в JSON: {', '.join(sorted(duplicates))}")
        errors = True

    # Проверка наличия date и description
    for item in meta_data:
        if not item.get("date"):
            print(f"❌ У записи с id={item['id']} отсутствует или пустой 'date'")
            errors = True
        elif not DATE_PATTERN.match(item["date"]):
            print(f"❌ У записи с id={item['id']} неверный формат даты (ожидается YYYY-MM-DD): {item['date']}")
            errors = True

        if "description" not in item:
            print(f"❌ У записи с id={item['id']} отсутствует поле 'description'")
            errors = True

    if not errors:
        print("✅ Проверка прошла успешно — все файлы и описания совпадают, поля заполнены корректно.")

    return not errors


if __name__ == "__main__":
    # Пример: проверка папки site/images_large
    validate_gallery("site/images_large")
