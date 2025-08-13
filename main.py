import os
import shutil

from gallery_tools import convert, data, site
from gallery_tools.config import (
    INPUT_DIR, OUTPUT_SITE_DIR,
    OUTPUT_LARGE_DIR, OUTPUT_THUMB_DIR,
    LARGE_SIZE, THUMB_SIZE, OUTPUT_JSON, TEMPLATE_FILE, OUTPUT_HTML
)
from gallery_tools.validate import validate_gallery


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
        INPUT_DIR, OUTPUT_LARGE_DIR, OUTPUT_THUMB_DIR,
        large_max_size=LARGE_SIZE, thumb_size=THUMB_SIZE
    )

    # 3. Проверка соответствия файлов и JSON
    if not validate_gallery(OUTPUT_LARGE_DIR):
        print("❌ Ошибки в данных. Исправьте их перед генерацией сайта.")
        exit(1)

    # 4. Генерация JSON
    data.generate_data_json(OUTPUT_LARGE_DIR, OUTPUT_THUMB_DIR, OUTPUT_JSON)

    # 5. Генерация HTML
    site.build_site(OUTPUT_JSON, TEMPLATE_FILE, OUTPUT_HTML)

    print("✅ Сайт готов в папке:", OUTPUT_SITE_DIR)
