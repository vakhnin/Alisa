import os
import shutil
import sys

from gallery_tools import convert, data, site, validate
from gallery_tools.config import (
    INPUT_DIR, OUTPUT_SITE_DIR,
    OUTPUT_LARGE_DIR, OUTPUT_THUMB_DIR,
    LARGE_SIZE, THUMB_SIZE, OUTPUT_JSON,
    TEMPLATE_FILE, OUTPUT_HTML
)


def prepare_site_folder():
    """Создаёт пустую папку site/"""
    if os.path.exists(OUTPUT_SITE_DIR):
        shutil.rmtree(OUTPUT_SITE_DIR)
    os.makedirs(OUTPUT_LARGE_DIR, exist_ok=True)
    os.makedirs(OUTPUT_THUMB_DIR, exist_ok=True)


if __name__ == "__main__":
    # 1. Подготовка папки site/
    prepare_site_folder()

    # 2. Конвертация изображений
    convert.process_folder(
        INPUT_DIR,
        OUTPUT_LARGE_DIR,
        OUTPUT_THUMB_DIR,
        large_max_size=LARGE_SIZE,
        thumb_size=THUMB_SIZE
    )

    # 2.1 Проверка данных и изображений
    errors = validate.check_images_and_data(INPUT_DIR, OUTPUT_LARGE_DIR, os.path.join(INPUT_DIR, "data.json"))
    if errors:
        print("❌ Ошибки при проверке:")
        for err in errors:
            print("   -", err)
        sys.exit(1)  # прерываем выполнение, сайт не собираем

    # 3. Генерация JSON
    data.generate_data_json(OUTPUT_LARGE_DIR, OUTPUT_THUMB_DIR, OUTPUT_JSON)

    # 4. Генерация HTML
    site.build_site(OUTPUT_JSON, TEMPLATE_FILE, OUTPUT_HTML)

    print("✅ Сайт готов в папке:", OUTPUT_SITE_DIR)
