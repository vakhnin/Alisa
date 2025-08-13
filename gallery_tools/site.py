import json
import os
import shutil

from gallery_tools.config import TEMPLATES_DIR


def build_site(data_json_path, template_html_path, output_html_path):
    # Загружаем список изображений
    with open(data_json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    # Загружаем переменные шаблона
    vars_path = os.path.join(TEMPLATES_DIR, "vars.json")
    if os.path.exists(vars_path):
        with open(vars_path, "r", encoding="utf-8") as f:
            vars_data = json.load(f)
    else:
        vars_data = {}

    # Генерируем HTML-элементы галереи
    gallery_items_html = "\n".join(
        f'<img src="{item["msrc"]}" '
        f'data-full="{item["src"]}" '
        f'data-desc="{item.get("description", "")}">'
        for item in items
    )

    # Читаем шаблон
    with open(template_html_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    # Подставляем переменные
    for key, value in vars_data.items():
        template_html = template_html.replace(f"{{{{{key}}}}}", value)

    # Подставляем галерею
    result_html = template_html.replace("{{GALLERY_ITEMS}}", gallery_items_html)

    # Копируем css и js
    output_dir = os.path.dirname(output_html_path)
    for folder in ["css", "js"]:
        src = os.path.join(TEMPLATES_DIR, folder)
        dst = os.path.join(output_dir, folder)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        if os.path.exists(src):
            shutil.copytree(src, dst)

    # Сохраняем HTML
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(result_html)

    print(f"✅ Сайт собран в {output_dir}")
