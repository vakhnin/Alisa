import json
import os

INPUT_JSON = "input_images/data.json"


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

    if not errors:
        print("✅ Проверка прошла успешно — все файлы и описания совпадают.")

    return not errors


if __name__ == "__main__":
    # Пример: проверка папки site/images_large
    validate_gallery("site/images_large")
