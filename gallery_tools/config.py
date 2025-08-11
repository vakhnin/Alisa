import os

# Входная папка с исходными картинками
INPUT_DIR = "input_images"

# Папка готового сайта
OUTPUT_SITE_DIR = "site"

# Папки для картинок
OUTPUT_LARGE_DIR = os.path.join(OUTPUT_SITE_DIR, "images_large")
OUTPUT_THUMB_DIR = os.path.join(OUTPUT_SITE_DIR, "images_thumb")

# Размеры
LARGE_SIZE = (1200, 900)
THUMB_SIZE = (200, 150)

# Файлы
OUTPUT_JSON = os.path.join(OUTPUT_SITE_DIR, "data.json")
TEMPLATE_FILE = "templates/index.html"
OUTPUT_HTML = os.path.join(OUTPUT_SITE_DIR, "index.html")
